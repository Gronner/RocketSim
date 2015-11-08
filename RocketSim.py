"""
Author: Felix Braeunling

Description: This file contains the Flight class, that describes a setup flight and also contains
"""
import Formula
from Atmospheres import Atmosphere
from Datas import Data
from Layers import Layer
from Planets import Planet
from RocketParts import RocketPart, Tank


class Flight(object):

    def __init__(self, time_delta, planet, rocket, atmosphere, data):
        """
        Setup of a flight with it's parameters
        :param time_delta: Size of the time step the simulation use
        :param planet: Planet the flight will take place
        :param rocket: Rocket the flight will use
        :param atmosphere: Atmosphere of the planet
        :param data: Data object gained values will be saved in.
        :return:
        """
        self.time_delta = time_delta
        self.planet = planet
        self.rocket = rocket
        self.atmosphere = atmosphere
        self.data = data

    def __lt__(self, other):
        max_self = max(self.data.pos_rocket)
        max_other = max(other.data.pos_rocket)
        return Formula.vector_addition(max_self) < Formula.vector_addition(max_other)

    def simulate(self):
        """
        Runs the simulation and starts the calculations
        """
        # Save time
        if len(self.data.time) == 0:
            time_now = 0
        else:
            time_now = self.data.time[-1] + self.time_delta
        self.data.time.append(time_now)
        # Get the current height the rocket is at
        height_now = Formula.vector_addition(self.rocket.get_pos())
        self.data.heigth_rocket.append(height_now)  # Save current height
        # Get the temperature at the height of the rocket
        temp_low_now = self.atmosphere.get_layer(height_now).get_temp_low()
        temp_gradient_now = self.atmosphere.get_layer(height_now).get_temp_gradient()
        height_low_now = self.atmosphere.get_layer(height_now).get_height_low()
        temperature_now = Formula.temperature(temp_low_now, temp_gradient_now, height_now, height_low_now)
        self.data.temperature.append(temperature_now)  # Save current temperature
        # Get the pressure at the height of the rocket
        pressure_low_now = self.atmosphere.get_layer(height_now).get_pressure_low()
        pressure_now = Formula.pressure(pressure_low_now, temp_gradient_now, height_now, height_low_now, temperature_now)
        self.data.pressure.append(pressure_now)  # Save current pressure
        # Get the current force of gravity the rocket is experiencing
        gravity_now = Formula.gravity(self.planet.get_mass(), self.rocket.get_mass(), height_now)
        self.data.gravity.append(gravity_now)
        # Get the thrust the rocket is producing
        current_stage = self.rocket.get_current_stage()
        change_prop_mass = False
        if type(current_stage) == RocketPart:
            thrust_now = current_stage.get_thrust()
        else:
            thrust_now = Formula.thrust(current_stage.get_mass_change(), current_stage.get_velocity_exhaust,
                                        current_stage.get_surface_nozzle, current_stage.get_pressure_nozzle,
                                        pressure_now)
            change_prop_mass = True
        self.data.thrust.append(thrust_now)
        # Get the drag the rocket is experiencing
        density_now = Formula.density(pressure_now, temperature_now)
        velocity_before = Formula.vector_addition(self.rocket.get_velocity())
        drag_coefficient = self.rocket.rocket_parts[0].drag_coefficient
        drag_now = Formula.drag(density_now, velocity_before, self.rocket.get_surface(), drag_coefficient)
        self.data.drag.append(drag_now) # Save current drag
        # Get current resulting force and resulting force in x and y direction
        force_res_now = Formula.resulting_force(thrust_now, drag_now, gravity_now)
        self.data.force_res.append(force_res_now)  # Save current resulting force
        angle_rocket_now = self.rocket.get_angle()
        self.data.angle_rocket.append(angle_rocket_now)  # Save current angle of the rocket
        force_res_x_now = Formula.res_x(force_res_now, angle_rocket_now)
        force_res_y_now = Formula.res_y(force_res_now, angle_rocket_now)
        self.data.force_res_split([force_res_x_now, force_res_y_now]) # Save split resulting force
        # Get current acceleration
        acceleration_now = Formula.acceleration(force_res_now, self.rocket.get_mass())
        self.data.acceleration_rocket.append(acceleration_now) # Save current acceleration
        acceleration_x_now = Formula.res_x(acceleration_now, angle_rocket_now)
        acceleration_y_now = Formula.res_y(acceleration_now, angle_rocket_now)
        self.rocket.set_acceleration(acceleration_x_now, acceleration_y_now)
        # Change mass of the rocket
        if change_prop_mass:
            mass_propellant_now = current_stage.get_mass_propellant() - current_stage.get_mass_change()*self.time_delta
            if mass_propellant_now < 0:
                self.rocket.decouple()
            else:
                current_stage.set_mass_propellant(mass_propellant_now)
        # Get current velocity
        velocity_x_now = Formula.velocity(self.rocket.get_velocity()[0], self.time_delta, acceleration_x_now)
        velocity_y_now = Formula.velocity(self.rocket.get_velocity()[1], self.time_delta, acceleration_y_now)
        velocity_now = Formula.vector_addition([velocity_x_now, velocity_y_now])
        self.rocket.set_velocity(velocity_x_now, velocity_y_now)
        self.data.velocity_rocket.append(velocity_now)  # Save velocity of the rocket
        # Get the current position
        way_traveled_x_now = Formula.way(self.time_delta, velocity_x_now, acceleration_x_now)
        pos_x_now = Formula.position(self.rocket.get_pos()[0], way_traveled_x_now)
        way_traveled_y_now = Formula.way(self.time_delta, velocity_y_now, acceleration_y_now)
        pos_y_now = Formula.position(self.rocket.get_pos()[1], way_traveled_y_now)
        self.data.pos_rocket.append([pos_x_now, pos_y_now])
        self.rocket.set_pos(pos_x_now, pos_y_now)