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
from Rockets import Rocket


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
        self.distance = Formula.vector_addition(self.rocket.get_pos())

    def __lt__(self, other):
        max_self = max(self.data.pos_rocket)
        max_other = max(other.data.pos_rocket)
        return Formula.vector_addition(max_self) < Formula.vector_addition(max_other)

    def simulate(self):
        """
        Runs the simulation and starts the calculations
        """
        # Save time
        time_now = self.data.time[-1] + self.time_delta
        self.data.time.append(time_now)
        # Get the current height the rocket is at
        height_now = Formula.vector_addition(self.rocket.get_pos())-self.planet.get_radius()
        distance_now = Formula.vector_addition(self.rocket.get_pos())
        self.data.heigth_rocket.append(height_now)  # Save current height
        # Get the temperature at the height of the rocket
        temp_low_now = self.atmosphere.get_layer(height_now).get_temp_low()
        temp_gradient_now = self.atmosphere.get_layer(height_now).get_temp_gradient()
        index_layer = self.atmosphere.get_layers().index(self.atmosphere.get_layer(height_now))
        height_low_now = self.atmosphere.calc_height_below(index_layer)
        temperature_now = Formula.temperature(temp_low_now, temp_gradient_now, height_now, height_low_now)
        self.data.temperature.append(temperature_now)  # Save current temperature
        # Get the pressure at the height of the rocket
        pressure_low_now = self.atmosphere.get_layer(height_now).get_pressure_low()
        pressure_now = Formula.pressure(pressure_low_now, temp_gradient_now, height_now, height_low_now, temperature_now)
        self.data.pressure.append(pressure_now)  # Save current pressure
        # Get the current force of gravity the rocket is experiencing
        gravity_now = Formula.gravity(self.planet.get_mass(), self.rocket.get_mass(), distance_now)
        self.data.gravity.append(gravity_now)
        # Get the thrust the rocket is producing
        current_stage = self.rocket.get_current_stage()
        change_prop_mass = False
        if type(current_stage) == RocketPart:
            thrust_now = current_stage.get_thrust()
        else:
            thrust_now = Formula.thrust(current_stage.get_mass_change(), current_stage.get_velocity_exhaust(),
                                        current_stage.get_surface_nozzle(), current_stage.get_pressure_nozzle(),
                                        pressure_now)
            change_prop_mass = True
        self.data.thrust.append(thrust_now)
        # Get the drag the rocket is experiencing
        density_now = Formula.density(pressure_now, temperature_now)
        self.data.density.append(density_now)  # Save density
        velocity_before = Formula.vector_addition(self.rocket.get_velocity())
        drag_coefficient = self.rocket.rocket_parts[0].drag_coefficient_part
        drag_now = Formula.drag(density_now, velocity_before, self.rocket.get_surface(), drag_coefficient)
        self.data.drag.append(drag_now)  # Save current drag
        # Get forces split in x and y direction
        angle_rocket_now = self.rocket.get_angle()
        self.data.angle_rocket.append(angle_rocket_now)  # Save current angle of the rocket
        thrust_now_x = Formula.res_x(thrust_now, angle_rocket_now)
        thrust_now_y = Formula.res_y(thrust_now, angle_rocket_now)
        gravity_now_x = Formula.res_x(gravity_now, angle_rocket_now)
        gravity_now_y = Formula.res_y(gravity_now, angle_rocket_now)
        drag_now_x = Formula.res_x(drag_now, angle_rocket_now)
        drag_now_y = Formula.res_y(drag_now, angle_rocket_now)
        # Get current resulting force and resulting forces in x and y direction
        force_res_now_x = Formula.resulting_force(thrust_now_x, gravity_now_x, drag_now_x)
        force_res_now_y = Formula.resulting_force(thrust_now_y, gravity_now_y,drag_now_y)
        force_res_now = Formula.vector_addition([force_res_now_x, force_res_now_y])
        self.data.force_res.append(force_res_now)  # Save current resulting force
        self.data.force_res_split.append([force_res_now_x, force_res_now_y])  # Save split resulting force
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
            self.rocket.set_mass()
        self.data.mass_rocket.append(self.rocket.get_mass())
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
        self.data.pos_x_rocket.append(pos_x_now)  # Save x position of the rocket
        self.data.pos_y_rocket.append(pos_y_now)  # Save y position of the rocket
        self.rocket.set_pos(pos_x_now, pos_y_now)
        # Get distance to planet core
        self.distance = Formula.vector_addition([pos_x_now, pos_y_now])
        print height_now/1000.0

    def get_distance(self):
        """
        :return: Distance of the rocket to the planets core [m]
        """
        return self.distance


def main():
    """
    Declare you planet, atmosphere with its layers, the rocket with its parts, the data object and the time delta here
    and run the simulation
    :return:
    """
    # Setup here
    sim_planet = Planet(pos_planet=[0.0, 0.0], mass_planet=5.974e+24, radius_planet=12756.32*1000)
    sim_planet_radius = sim_planet.get_radius()
    sim_layer_one = Layer(pressure_low=100000, width_layer=18000.0, temp_gradient=-0.00065, temp_low=279.0)
    sim_atmosphere = Atmosphere()
    sim_atmosphere.add_layer(sim_layer_one)
    sim_data = Data(data_file="./Results/Test_one.csv")
    sim_rocket_part_one = RocketPart(mass_part=100000.0, surface_part=1.2, drag_coefficient_part=0.34)
    sim_tank_one = Tank(mass_part=100.0, surface_part=0.0, drag_coefficient_part=0.0, mass_propellant=1000.0, mass_change_tank=0.34,
                        velocity_exhaust_tank=30.0, surface_nozzle=0.8, pressure_nozzle=26000000.0)
    sim_rocket = Rocket(pos=[sim_planet_radius, 0.0], velocity=[0.0, 0.0], acceleration=[0.0, 0.0])
    sim_rocket.append_part(sim_rocket_part_one)
    sim_rocket.append_part(sim_tank_one)
    sim_rocket.set_mass()
    sim_rocket.set_surface()
    sim_time_step = 0.1  # [s] Timestep the simulation uses
    sim_flight = Flight(sim_time_step, sim_planet, sim_rocket, sim_atmosphere, sim_data)
    sim_max_step = 100000  # Maximum time steps the simulation should run
    # Running the simulation
    current_step = 0
    sim_flight.data.pos_x_rocket.append(sim_rocket.get_pos()[0])
    sim_flight.data.pos_y_rocket.append(sim_rocket.get_pos()[1])
    sim_flight.data.velocity_rocket.append(sim_rocket.get_velocity()[0])
    sim_flight.data.acceleration_rocket.append(sim_rocket.get_acceleration()[0])
    sim_flight.data.mass_rocket.append(sim_rocket.get_mass())
    sim_flight.data.angle_rocket.append(sim_rocket.get_angle())
    sim_flight.data.gravity.append(Formula.gravity(sim_planet.get_mass(), sim_rocket.get_mass(), sim_planet_radius))
    sim_flight.data.force_res.append(-1*sim_flight.data.gravity[0])
    sim_flight.data.temperature.append(sim_atmosphere.get_layer(0.0).get_temp_low())
    sim_flight.data.pressure.append(sim_atmosphere.get_layer(0.0).get_pressure_low())
    sim_flight.data.density.append(sim_atmosphere.get_layer(0).get_density_now(0.0, 0.0))
    print "Simulation starting"
    while (not (sim_flight.get_distance() < sim_planet_radius)) and (not (current_step > sim_max_step)):
        sim_flight.simulate()
        current_step += 1
    print "Simulation ended!"
    sim_flight.data.write_csv()
    print "Saved to CSV!"
if __name__ == "__main__":
    main()