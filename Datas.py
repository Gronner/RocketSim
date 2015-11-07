"""
Author:         Felix Braeunling
Description:    This class is used to store any values generated during the calculations and saves
                them for later plotting
"""

import csv


class Data(object):

    def __init__(self, data_file):
        self.data_file = data_file
        self.time = []  # [s]
        self.pos_rocket = []  # [(m, m)] for x and y coordinates
        self.velocity_rocket = []  # [m/s]
        self.acceleration_rocket = []  # [m/s^2]
        self.mass_rocket = []  # [kg]
        self.heigth_rocket = []  # [m]
        self.angle_rocket = []  # [grad]
        self.thrust = []  # [N]
        self.drag = []  # [N]
        self.gravity = []  # [N]
        self.force_res = []  # [N]
        self.force_res_split = []  # [(N, N)] for x and y direction
        self.temperature = []  # [K]
        self.pressure = []  # [Pa]
        self.density = []  # [kg/m^3]

    def add_data(self, time, pos_rocket, velocity_rocket, acceleration_rocket, mass_rocket, height_rocket,
                 angle_rocket, thrust, drag, gravity, force_res, force_res_split, temperature, pressure, density):
        """
        Appends new data values to their list
        :param time: Time the simulation ran (Double)
        :param pos_rocket: Position of the rocket as coordinates (Tuple -> (Double, Double))
        :param velocity_rocket: Velocity of the rocket (Double)
        :param acceleration_rocket:  Acceleration of the rocket (Double)
        :param mass_rocket: Mass of the rocket (Double)
        :param height_rocket: Height of the above the planet surface (Double)
        :param angle_rocket: Angle of the rocket to the horizon (Double)
        :param thrust: Thrust of the rocket (Double)
        :param drag: Drag the rocket is experiencing (Double)
        :param gravity: Gravity between the rocket and the planet (Double)
        :param force_res: Resulting force affecting the rocket (Double)
        :param force_res_split: Resulting force split in x and y direction (Tuple -> (Double, Double)
        :param temperature: Temperature of the ambient (Double)
        :param pressure: Pressure of the ambient (Double)
        :param density: Density of the medium the rocket is in (Double)
        """
        self.time.append(time)
        self.pos_rocket.append(pos_rocket)
        self.velocity_rocket.append(velocity_rocket)
        self.acceleration_rocket.append(acceleration_rocket)
        self.mass_rocket.append(mass_rocket)
        self.heigth_rocket.append(height_rocket)
        self.angle_rocket.append(angle_rocket)
        self.thrust.append(thrust)
        self.drag.append(drag)
        self.gravity.append(gravity)
        self.force_res.append(force_res)
        self.force_res_split.append(force_res_split)
        self.temperature.append(temperature)
        self.pressure.append(pressure)
        self.density.append(density)

    def write_csv(self):
        """
        Writes the saved data in a csv file
        """
        with open(self.data_file, 'wb') as csv_file:
            data_writer = csv.writer(csv_file, delimiter=',')
            data_writer.writerow(self.time)
            data_writer.writerow(self.pos_rocket)
            data_writer.writerow(self.velocity_rocket)
            data_writer.writerow(self.acceleration_rocket)
            data_writer.writerow(self.mass_rocket)
            data_writer.writerow(self.heigth_rocket)
            data_writer.writerow(self.angle_rocket)
            data_writer.writerow(self.thrust)
            data_writer.writerow(self.drag)
            data_writer.writerow(self.gravity)
            data_writer.writerow(self.force_res)
            data_writer.writerow(self.force_res_split)
            data_writer.writerow(self.temperature)
            data_writer.writerow(self.pressure)
            data_writer.writerow(self.density)

    def read_csv(self):
        """
        Reads saved data from an csv-file
        """
        with open(self.data_file, 'rb') as csv_file:
            data_reader = csv.reader(csv_file, delimiter=',')
            new_data = []
            for row in data_reader:
                new_data.append(row)
            self.time = new_data[0]
            self.pos_rocket = new_data[1]
            self.velocity_rocket = new_data[2]
            self.acceleration_rocket = new_data[3]
            self.mass_rocket = new_data[4]
            self.heigth_rocket = new_data[5]
            self.angle_rocket = new_data[6]
            self.thrust = new_data[7]
            self.drag = new_data[8]
            self.gravity = new_data[9]
            self.force_res = new_data[10]
            self.force_res_split = new_data[11]
            self.temperature = new_data[12]
            self.pressure = new_data[13]
            self.density = new_data[14]
