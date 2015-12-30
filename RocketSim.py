"""
Author: Felix Braeunling

Description: This file contains the Flight class, that describes a setup flight and also contains
"""
import Formula
import os
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

    def get_max_height(self):
        return max(self.data.pos_x_rocket) - self.planet.get_radius()

    def simulate(self):
        """
        Runs the simulation and starts the calculations
        """
        # Save time
        time_now = self.data.time[-1] + self.time_delta
        if time_now > 140.0:
            pass
        self.data.time.append(time_now)
        # Get the current height the rocket is at
        height_now = Formula.vector_addition(self.rocket.get_pos())-self.planet.get_radius()
        descending = False
        if height_now < self.data.heigth_rocket[-1]:
            descending = True
        distance_now = Formula.vector_addition(self.rocket.get_pos())
        self.data.heigth_rocket.append(height_now)  # Save current height
        # Get the temperature at the height of the rocket
        temp_low_now = self.atmosphere.get_layer(height_now).get_temp_low()
        temp_gradient_now = self.atmosphere.get_layer(height_now).get_temp_gradient()
        index_layer = self.atmosphere.get_layers().index(self.atmosphere.get_layer(height_now))
        height_low_now = self.atmosphere.calc_height_below(index_layer)
        temperature_now = Formula.temperature(temp_low_now, temp_gradient_now, height_low_now, height_now)
        self.data.temperature.append(temperature_now)  # Save current temperature
        # Get the pressure at the height of the rocket
        pressure_low_now = self.atmosphere.get_layer(height_now).get_pressure_low()
        pressure_now = Formula.pressure(pressure_low_now, temp_gradient_now, height_now, height_low_now, temp_low_now)
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
        if descending:
            rocket_desc = -1
        else:
            rocket_desc = 1
        drag_now = rocket_desc * Formula.drag(density_now, velocity_before, self.rocket.get_surface(), drag_coefficient)
        self.data.drag.append(abs(drag_now))  # Save current drag
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
        self.data.force_res.append(force_res_now_x)  # Save current resulting force
        self.data.force_res_split.append([force_res_now_x, force_res_now_y])  # Save split resulting force
        # Get current acceleration
        acceleration_x_now = Formula.acceleration(force_res_now_x, self.rocket.get_mass())
        acceleration_y_now = Formula.acceleration(force_res_now_y, self.rocket.get_mass())
        acceleration_now = Formula.vector_addition([force_res_now_x, force_res_now_y])
        self.data.acceleration_rocket.append(acceleration_x_now) # Save current acceleration
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
        self.data.velocity_rocket.append(velocity_x_now)  # Save velocity of the rocket
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
        print height_now

    def get_distance(self):
        """
        :return: Distance of the rocket to the planets core [m]
        """
        return self.distance


def run_sim(sim_flight, flight_name, max_step, sim_time_step):
    """Runs the simulation for one flight, with all setup and tear down operations
    :param flight: Flight object, that will be simulated (Flight)
    :param flight_name: Name of the flight (String)
    :param max_step: Maximum iterations in on simulation (Integer)
    :param sim_time_step: Time delta for each simulation step (Integer)
    """
    current_step = 0
    sim_flight.data.pos_x_rocket.append(sim_flight.rocket.get_pos()[0])
    sim_flight.data.pos_y_rocket.append(sim_flight.rocket.get_pos()[1])
    sim_flight.data.velocity_rocket.append(sim_flight.rocket.get_velocity()[0])
    sim_flight.data.acceleration_rocket.append(sim_flight.rocket.get_acceleration()[0])
    sim_flight.data.mass_rocket.append(sim_flight.rocket.get_mass())
    sim_flight.data.angle_rocket.append(sim_flight.rocket.get_angle())
    sim_flight.data.gravity.append(Formula.gravity(sim_flight.planet.get_mass(), sim_flight.rocket.get_mass(), sim_flight.planet.radius_planet))
    sim_flight.data.force_res.append(-1*sim_flight.data.gravity[0])
    sim_flight.data.temperature.append(sim_flight.atmosphere.get_layer(0.0).get_temp_low())
    sim_flight.data.pressure.append(sim_flight.atmosphere.get_layer(0.0).get_pressure_low())
    sim_flight.data.density.append(sim_flight.atmosphere.get_layer(0).get_density_now(0.0, 0.0))
    print "Simulation starting"
    while sim_flight.get_distance() >= sim_flight.planet.get_radius() and current_step <= max_step:
        sim_flight.simulate()
        current_step += 1
    #Setting end point data
    sim_flight.data.time.append(sim_flight.data.time[-1]+sim_time_step)
    sim_flight.data.heigth_rocket.append(0.0)
    sim_flight.data.pos_x_rocket.append(sim_flight.planet.get_radius())
    sim_flight.data.pos_y_rocket.append(0.0)
    sim_flight.data.velocity_rocket.append(0.0)
    sim_flight.data.acceleration_rocket.append(0.0)
    sim_flight.data.mass_rocket.append(sim_flight.rocket.rocket_parts[-1].get_mass())
    sim_flight.data.angle_rocket.append(0.0)
    sim_flight.data.thrust.append(0.0)
    sim_flight.data.drag.append(0.0)
    sim_flight.data.gravity.append(sim_flight.data.gravity[0])
    sim_flight.data.force_res.append(sim_flight.data.gravity[0])
    sim_flight.data.force_res_split.append([sim_flight.data.gravity[0], 0.0])
    sim_flight.data.temperature.append(sim_flight.data.temperature[0])
    sim_flight.data.pressure.append(sim_flight.data.pressure[0])
    sim_flight.data.density.append(sim_flight.data.density[0])
    print "Simulation ended! Last Step: "+str(current_step)
    if not os.path.exists("./Results_2/{}".format(flight_name)):
        os.makedirs("./Results_2/{}".format(flight_name))
    sim_flight.data.write_csv()
    print "Saved to CSV! In Folder {}".format(flight_name)


def main():
    """
    Declare your planet, atmosphere with its layers, the rocket with its parts, the data object and the time delta here
    and run the simulation
    :return:
    """
    # Setup here
    sim_max_step = 100000  # Maximum time steps the simulation should run
    sim_time_step = 0.1  # [s] Timestep the simulation uses
    earth = Planet(pos_planet=[0.0, 0.0], mass_planet=5.974e+24, radius_planet=12756.32/2.0*1000)
    earth_radius = earth.get_radius()
    troposphere = Layer(pressure_low=101325.0, width_layer=18000.0, temp_gradient=-0.0065, temp_low=288.15)
    stratosphere = Layer(pressure_low=16901.37, width_layer=32000.0, temp_gradient=0.0031875, temp_low=171.15)
    mesosphere = Layer(pressure_low=1.02, width_layer=30000.0, temp_gradient=-0.003333, temp_low=273.15)
    thermosphere = Layer(pressure_low=0.04, width_layer=420000.0, temp_gradient=-0.000405, temp_low=173.15)
    exosphere = Layer(pressure_low=0.0, width_layer=9999999999.0, temp_gradient=0.0, temp_low=3.0)
    earth_atmosphere = Atmosphere()
    earth_atmosphere.add_layer(troposphere)
    earth_atmosphere.add_layer(stratosphere)
    earth_atmosphere.add_layer(mesosphere)
    earth_atmosphere.add_layer(thermosphere)
    earth_atmosphere.add_layer(exosphere)
    # Set maximum propellant mass
    A150_mass_propellant = 484.8076
    # Calculate A150 one tank:
    sim_flight_name = "A150_OneTank"
    sim_data = Data(data_file="./Results_2/{}/Results_Data.csv".format(sim_flight_name))
    sim_data.name = "Einstufig"
    A150_payload = 0.0  # kg moegliche Nutzlast
    A150_nose_cone = RocketPart(mass_part=7.0+2.31336+A150_payload, surface_part=0.1140, drag_coefficient_part=0.27)
    A150_liquid_tank = Tank(mass_part=116.1216, surface_part=0.0, drag_coefficient_part=0.0, mass_propellant=A150_mass_propellant, mass_change_tank=9.394,
                        velocity_exhaust_tank=1417.32, surface_nozzle=0.0275, pressure_nozzle=101325.0)
    A150 = Rocket(pos=[earth_radius, 0.0], velocity=[0.0, 0.0], acceleration=[0.0, 0.0])
    A150_booster = Tank(mass_part=28.1232, surface_part=0.0, drag_coefficient_part=0.0, mass_propellant=117.6074, mass_change_tank=47.1733,
                        velocity_exhaust_tank=1747.6074, surface_nozzle=0.0434, pressure_nozzle=101325.0)
    A150.append_part(A150_nose_cone)
    A150.append_part(A150_liquid_tank)
    A150.append_part(A150_booster)
    A150.set_mass()
    A150.set_surface()
    sim_flight = Flight(sim_time_step, earth, A150, earth_atmosphere, sim_data)
    # Running the simulation
    run_sim(sim_flight, sim_flight_name, sim_max_step, sim_time_step)

    # Calculate A150 two tanks 1
    sim_flight_name = "A150_RefTankA"
    sim_data = Data(data_file="./Results_2/{}/Results_Data.csv".format(sim_flight_name))
    sim_data.name = "Stufe 1 leer"
    A150_payload = 0.0  # kg moegliche Nutzlast
    A150_nose_cone = RocketPart(mass_part=7.0+2.31336+A150_payload, surface_part=0.1140, drag_coefficient_part=0.27)
    A150_liquid_tank_one = Tank(mass_part=116.1216, surface_part=0.0, drag_coefficient_part=0.0, mass_propellant=A150_mass_propellant, mass_change_tank=9.394,
                        velocity_exhaust_tank=1417.32, surface_nozzle=0.0275, pressure_nozzle=101325.0)
    A150_liquid_tank_two = Tank(mass_part=116.1216, surface_part=0.0, drag_coefficient_part=0.0, mass_propellant=0, mass_change_tank=9.394,
                        velocity_exhaust_tank=1417.32, surface_nozzle=0.0275, pressure_nozzle=101325.0)
    A150 = Rocket(pos=[earth_radius, 0.0], velocity=[0.0, 0.0], acceleration=[0.0, 0.0])
    A150_booster = Tank(mass_part=28.1232, surface_part=0.0, drag_coefficient_part=0.0, mass_propellant=117.6074, mass_change_tank=47.1733,
                        velocity_exhaust_tank=1747.6074, surface_nozzle=0.0434, pressure_nozzle=101325.0)
    A150.append_part(A150_nose_cone)
    A150.append_part(A150_liquid_tank_one)
    A150.append_part(A150_liquid_tank_two)
    A150.append_part(A150_booster)
    A150.set_mass()
    A150.set_surface()
    sim_flight_a = Flight(sim_time_step, earth, A150, earth_atmosphere, sim_data)
    # Running the simulation
    run_sim(sim_flight_a, sim_flight_name, sim_max_step, sim_time_step)

    # Calculate A150 two tanks 1
    sim_flight_name = "A150_RefTankB"
    sim_data = Data(data_file="./Results_2/{}/Results_Data.csv".format(sim_flight_name))
    sim_data.name = "Stufe 2 leer"
    A150_payload = 0.0  # kg moegliche Nutzlast
    A150_nose_cone = RocketPart(mass_part=7.0+2.31336+A150_payload, surface_part=0.1140, drag_coefficient_part=0.27)
    A150_liquid_tank_one = Tank(mass_part=116.1216, surface_part=0.0, drag_coefficient_part=0.0, mass_propellant=0, mass_change_tank=9.394,
                        velocity_exhaust_tank=1417.32, surface_nozzle=0.0275, pressure_nozzle=101325.0)
    A150_liquid_tank_two = Tank(mass_part=116.1216, surface_part=0.0, drag_coefficient_part=0.0, mass_propellant=A150_mass_propellant, mass_change_tank=9.394,
                        velocity_exhaust_tank=1417.32, surface_nozzle=0.0275, pressure_nozzle=101325.0)
    A150 = Rocket(pos=[earth_radius, 0.0], velocity=[0.0, 0.0], acceleration=[0.0, 0.0])
    A150_booster = Tank(mass_part=28.1232, surface_part=0.0, drag_coefficient_part=0.0, mass_propellant=117.6074, mass_change_tank=47.1733,
                        velocity_exhaust_tank=1747.6074, surface_nozzle=0.0434, pressure_nozzle=101325.0)
    A150.append_part(A150_nose_cone)
    A150.append_part(A150_liquid_tank_one)
    A150.append_part(A150_liquid_tank_two)
    A150.append_part(A150_booster)
    A150.set_mass()
    A150.set_surface()
    sim_flight_b = Flight(sim_time_step, earth, A150, earth_atmosphere, sim_data)

    # Running the simulation
    run_sim(sim_flight_b, sim_flight_name, sim_max_step, sim_time_step)

    # Searching for optimal tank setup
    divisor = 2
    count = 0
    sim_opt_max_step = 40

    propellant_step = A150_mass_propellant/sim_opt_max_step
    while count < sim_opt_max_step:
        sim_flight_name = "A150_TankSetup_{0:03d}".format(count)
        sim_data = Data(data_file="./Results_2/{}/Results_Data.csv".format(sim_flight_name))
        A150_mass_propellant_tank_one = propellant_step*count
        A150_mass_propellant_tank_two = A150_mass_propellant - propellant_step*count
        sim_data.name = "Stufe 1: {0:.2f} kg Stufe 2: {1:.2f} kg".format(A150_mass_propellant_tank_two, A150_mass_propellant_tank_one)
        A150 = Rocket(pos=[earth_radius, 0.0], velocity=[0.0, 0.0], acceleration=[0.0, 0.0])
        A150_liquid_tank_one_split = Tank(mass_part=116.1216, surface_part=0.0, drag_coefficient_part=0.0,
                                    mass_propellant=A150_mass_propellant_tank_one, mass_change_tank=9.394,
                                    velocity_exhaust_tank=1417.32, surface_nozzle=0.0275, pressure_nozzle=101325.0)
        A150_liquid_tank_two_split = Tank(mass_part=116.1216, surface_part=0.0, drag_coefficient_part=0.0,
                                    mass_propellant=A150_mass_propellant_tank_two, mass_change_tank=9.394,
                                    velocity_exhaust_tank=1417.32, surface_nozzle=0.0275, pressure_nozzle=101325.0)
        A150_booster = Tank(mass_part=28.1232, surface_part=0.0, drag_coefficient_part=0.0, mass_propellant=117.6074, mass_change_tank=47.1733,
                        velocity_exhaust_tank=1747.6074, surface_nozzle=0.0434, pressure_nozzle=101325.0)
        A150.append_part(A150_nose_cone)
        A150.append_part(A150_liquid_tank_one_split)
        A150.append_part(A150_liquid_tank_two_split)
        A150.append_part(A150_booster)
        A150.set_mass()
        A150.set_surface()
        sim_flight_p = Flight(sim_time_step, earth, A150, earth_atmosphere, sim_data)
        # Running the simulation
        run_sim(sim_flight_p, sim_flight_name, sim_max_step, sim_time_step)

        count += 1


    # Calculate A150 one tank, no booster:
    sim_flight_name = "A150_NoBooster"
    sim_data = Data(data_file="./Results_2/{}/Results_Data.csv".format(sim_flight_name))
    sim_data.name = "Einstufig ohne Booster"
    A150_payload = 0.0  # kg moegliche Nutzlast
    A150_nose_cone = RocketPart(mass_part=7.0+2.31336+A150_payload, surface_part=0.1140, drag_coefficient_part=0.27)
    A150_liquid_tank = Tank(mass_part=116.1216, surface_part=0.0, drag_coefficient_part=0.0, mass_propellant=A150_mass_propellant, mass_change_tank=9.394,
                        velocity_exhaust_tank=1417.32, surface_nozzle=0.0275, pressure_nozzle=101325.0)
    A150 = Rocket(pos=[earth_radius, 0.0], velocity=[0.0, 0.0], acceleration=[0.0, 0.0])
    A150.append_part(A150_nose_cone)
    A150.append_part(A150_liquid_tank)
    A150.set_mass()
    A150.set_surface()
    sim_flight_nb = Flight(sim_time_step, earth, A150, earth_atmosphere, sim_data)
    # Running the simulation
    run_sim(sim_flight_nb, sim_flight_name, sim_max_step, sim_time_step)

    print "Optimization has ended after {} iterations, Results available".format(count-1)



if __name__ == "__main__":
    main()