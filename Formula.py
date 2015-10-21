"""
Author:         Felix Braeunling
Description:    This module contains the formulas for calculating the
                necessary values for the simulation on the basis of
                flight, orbital, gravitational mechanics, as well as
                other physical influences like drag.
"""

import math

G = 6.67408e-10     # Newton's gravity constant             [m^3/(kg*s^2)]
M = 0.02896         # Molar mass of atmosphere gasses       [kg/mol]
R = 8.314           # universal gas constant                [J/(K*mol)]
g = 9.807           # Earths gravitational acceleration     [m/s^2]


def thrust(mass_change, velocity_propellant, surface_nozzle, pressure_nozzle, pressure_ambient):
    """
    Calculates the thrust the engine is producing based on the following inputs
    :param mass_change: Change of mass of propellant (Double)
    :param velocity_propellant: Velocity of propellant (Double)
    :param surface_nozzle: Surface area of the exit nozzle (Double)
    :param pressure_nozzle: Pressure in the area of the nozzle (Double)
    :param pressure_ambient: Pressure of the ambient (Double)
    :return: Thrust produced by the engine (Double) [N]
    """
    return mass_change * velocity_propellant + surface_nozzle * (pressure_nozzle - pressure_ambient)


def drag(density_ambient, velocity_rocket, surface_rocket, drag_coefficient):
    """
    Calculates the drag the rocket experiences based on the following inputs
    :param density_ambient: Density of the medium the rocket is travelling in (Double)
    :param velocity_rocket: Velocity of the rocket in travelling direction (Double)
    :param surface_rocket: Surface area of the rocket that is exposed to drag (Double)
    :param drag_coefficient: Drag coefficient of the rocket (Double)
    :return: Drag experienced by the rocket (Double) [N]
    """
    return 1.0 / 2.0 * density_ambient * velocity_rocket**2 * surface_rocket * drag_coefficient


def gravity(mass_planet, mass_rocket, distance):
    """
    Calculates the gravitational force between the planet and the rocket,
    raises an exception if distance is zero or force is negative
    :param mass_planet: Mass of the planet (Double)
    :param mass_rocket: Mass of the rocket (Double)
    :param distance: Distance between the center of mass of the rocket and the planet (non-zero Double)
    :return: gravitational fore (positive Double) [N]
    """
    global G
    gravity_now = G * (mass_planet * mass_rocket) / distance**2
    if gravity_now < 0:
        raise ValueError("No negative gravity possible!")
    return gravity_now


def pressure(pressure_height_low, temp_gradient, height_rocket, height_low, temp_height_low):
    """
    Calculates the pressure at a certain height
    :param pressure_height_low: Pressure at the lower end of the atmosphere layer (Double)
    :param temp_gradient: Temperature gradient for the atmosphere layer (Double)
    :param height_rocket: Height of the rocket (Double)
    :param height_low: Height of the lower end of the atmosphere layer (Double)
    :param temp_height_low: Temperature at the lower end of the atmosphere layer (Double)
    :return: Pressure at the height of the rocket [Pa]
    """
    global g
    global M
    global R
    expo = (M * g) / (R * temp_gradient)
    height_diff = height_rocket - height_low
    quot = (temp_gradient * height_diff) / temp_height_low
    return pressure_height_low * (1 - quot)**expo


def temperature(temp_height_low, temp_gradient, heigth_low, height_rocket):
    """
    Calculates the temperature at a certain height
    :param temp_height_low: Temperature at the lowest point of the atmosphere layer (Double)
    :param temp_gradient: Temperature gradient for the atmosphere layer (Double)
    :param heigth_low: Height of the lower end of the atmosphere layer (Double)
    :param height_rocket: Height of the rocket (Double)
    :return: Temperature at the height of the rocket (Double) [K]
    """
    height_diff = height_rocket - heigth_low
    return temp_height_low * (1 - temp_gradient*height_diff)


def density(pressure_medium, temp_height):
    """
    Calculates the atmospheres density at a certain height
    :param p_h: The pressure of the medium depending on the height (Double)
    :param t_h: The Temperature of the medium depending on the height (Double)
    :return: Density of the medium depending on the height of the rocket (Double) [kg/m^3]
    """
    global R
    global M
    return (pressure_medium * M) / (R * temp_height)


def resulting_force(force_thrust, force_drag, force_gravity):
    """
    Calculates the resulting force from the three main forces
    :param force_thrust: Force produced by thrust (Double)
    :param force_drag: Force produced by drag (Double)
    :param force_gravity: Force applied by gravity (Double)
    :return: Sum of the three forces (Double) [N]
    """
    return force_thrust + force_drag + force_gravity


def angle(velocity_rocket, pos_change, radius_planet, height_rocket):
    """
    Calculates the change of the angle of the rocket to the horizon
    :param velocity_rocket: Speed of the rocket (Double)
    :param pos_change: Change of the position of the rocket (Double)
    :param radius_planet: Radius of the planet the rocket is orbiting (Double)
    :param height_rocket: Height of the rocket above the planet (Double)
    :return: Returns the new angle of the rocket to the horizon (Double) [grad]
    """
    angle_now = math.acos(1 / velocity_rocket * pos_change * (radius_planet + height_rocket) / radius_planet)
    return math.degrees(angle_now)


def acceleration(force_result, mass_rocket):
    """
    Calculates the acceleration of the rocket based on its mass and the force it's experiencing
    :param force_result: Resulting force of drag, thrust and gravity (Double)
    :param mass_rocket: Mass of the rocket depending on parts and carried fuel (Double)
    :return: Acceleration of the rocket (Double) [m/s^2]
    """
    return force_result / mass_rocket


def velocity(velocity_t0, duration_interval, acceleration_rocket):
    """
    Calculates the velocity of the rocket at a certain time interval
    :param velocity_t0: Velocity at the beginning of the time interval (Double)
    :param duration_interval: Duration of the interval (Double)
    :param acceleration_rocket: Acceleration of the rocket during the interval (Double)
    :return: Velocity of the rocket at the end of the interval (Double) [m/s]
    """
    return velocity_t0 + duration_interval * acceleration_rocket


def way(duration_interval, velocity_rocket, acceleration_rocket):
    """
    Calculates the change of the position of the rocket at a certain time
    :param duration_interval: Duration of the interval (Double)
    :param velocity_rocket: Velocity of the rocket during the interval (Double)
    :param acceleration_rocket: Acceleration of the rocket during the interval (Double)
    :return: Change in position of the rocket at the end of the time interval (Double) [m]
    """
    return duration_interval * velocity_rocket + 1.0 / 2.0 * acceleration_rocket * duration_interval**2


def res_x(factor_result, angle_rocket):
    """
    Calculates the resulting force in x-direction
    :param factor_result: resulting factor in rocket direction (Double)
    :param angle_rocket: angle the rocket is facing to the horizon (Double) [grad]
    :return: resulting factor in x-direction (Double) [N]
    """
    angle_rad_r = math.radians(angle_rocket)
    return factor_result * math.cos(angle_rad_r)


def res_y(factor_result, angle_rocket):
    """
    Calculates the resulting force in y-direction
    :param factor_result: resulting factor in rocket direction (Double)
    :param angle_rocket: angle the rocket is facing to the horizon (Double) [grad]
    :return: resulting factor in y-direction (Double) [N]
    """
    angle_rad_r = math.radians(angle_rocket)
    return factor_result * math.sin(angle_rad_r)


def position(pos_t0, way_traveled):
    """
    Calculates the new position of the rocket
    :param pos_t0: Last position of the rocket (Double)
    :param way_traveled: Length traveled of the rocket (Double)
    :return: New Position of the rocket
    """
    return pos_t0 + way_traveled

