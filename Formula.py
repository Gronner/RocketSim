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

def thrust(m_dt, v_p, s_e, p_p, p_amb):
    """
    Calculates the thrust the engine is producing based on the following inputs
    :param m_dt: Change of mass of propellant (Double)
    :param v_p: Velocity of propellant (Double)
    :param s_e: Surface area of the exit nozzle (Double)
    :param p_p: Pressure in the area of the nozzle (Double)
    :param p_amb: Pressure of the ambient (Double)
    :return: Thrust produced by the engine (Double) [N]
    """
    thrustnow = m_dt * v_p + s_e * (p_p - p_amb)
    return thrustnow


def drag(density, v_r, s_r, c_d):
    """
    Calculates the drag the rocket experiences based on the following inputs
    :param density: Density of the medium the rocket is travelling in (Double)
    :param v_r: Velocity of the rocket in travelling direction (Double)
    :param s_r: Surface area of the rocket that is exposed to drag (Double)
    :param c_d: Drag coefficient of the rocket (Double)
    :return: Drag experienced by the rocket (Double) [N]
    """
    dragnow = 1.0 / 2.0 * density * v_r**2 * s_r * c_d
    return dragnow


def gravity(m_p, m_r, distance):
    """
    Calculates the gravitational force between the planet and the rocket,
    raises an exception if distance is zero or force is negative
    :param m_p: Mass of the planet (Double)
    :param m_r: Mass of the rocket (Double)
    :param distance: Distance between the center of mass of the rocket and the planet (non-zero Double)
    :return: gravitational fore (positive Double) [N]
    """
    global G
    gravitynow = G * (m_p * m_r) / distance**2
    if gravitynow < 0:
        raise ValueError("No negative gravity possible!")
    return gravitynow


def pressure(p_h0, a, h1, h0, t_ho):
    """
    Calculates the pressure at a certain height
    :param p_h0: Pressure at the lower end of the atmosphere layer (Double)
    :param a: Temperature gradient for the atmosphere layer (Double)
    :param h1: Height of the rocket (Double)
    :param h0: Height of the lower end of the atmosphere layer (Double)
    :param t_ho: Temperature at the lower end of the atmosphere layer (Double)
    :return: Pressure at the height of the rocket [Pa]
    """
    global g
    global M
    global R
    expo = (M * g) / (R * a)
    heightdiff = h1 - h0
    quot = (a * heightdiff) / t_ho
    pressurenow = p_h0 * (1 - quot)**expo
    return pressurenow


def temperature(t_h0, a, h0, h1):
    """
    Calculates the temperature at a certain height
    :param T_h0: Temperature at the lowest point of the atmosphere layer (Double)
    :param a: Temperature gradient for the atmosphere layer (Double)
    :param h0: Height of the lower end of the atmosphere layer (Double)
    :param h1: Height of the rocket (Double)
    :return: Temperature at the height of the rocket (Double) [K]
    """
    heightdiff = h1 - h0
    temperaturenow = t_h0 * (1 - a*heightdiff)
    return temperaturenow


def density(p_h, t_h):
    """
    Calculates the atmospheres density at a certain height
    :param p_h: The pressure of the medium depending on the height (Double)
    :param t_h: The Temperature of the medium depending on the height (Double)
    :return: Density of the medium depending on the height of the rocket (Double) [kg/m^3]
    """
    global R
    global M
    densitynow = (p_h * M) / (R * t_h)
    return densitynow


def resultingforce(f_t, f_d, f_g):
    """
    Calculates the resulting force from the three main forces
    :param F_T: Force produced by thrust (Double)
    :param F_D: Force produced by drag (Double)
    :param F_G: Force applied by gravity (Double)
    :return: Sum of the three forces (Double) [N]
    """
    resultingforcenow = f_t + f_d + f_g
    return resultingforcenow


def angle(v_r, dx_dt, r_e, h_r):
    """
    Calculates the change of the angle of the rocket to the horizon
    :param v_r: Speed of the rocket (Double)
    :param dx_dt: Change of the position of the rocket (Double)
    :param r_e: Radius of the planet the rocket is orbiting (Double)
    :param h_r: Height of the rocket above the planet (Double)
    :return: Returns the new angle of the rocket to the horizon (Double) [grad]
    """
    anglenow = math.acos(1 / v_r * dx_dt * (r_e + h_r) / r_e)
    return math.degrees(anglenow)


def acceleration(f_r, m_r):
    """
    Calculates the acceleration of the rocket based on its mass and the force it's experiencing
    :param f_r: Resulting force of drag, thrust and gravity (Double)
    :param m_r: Mass of the rocket depending on parts and carried fuel (Double)
    :return: Acceleration of the rocket (Double) [m/s^2]
    """
    accelerationnow = f_r / m_r
    return accelerationnow


def velocity(v_0, d_t, a_r):
    """
    Calculates the velocity of the rocket at a certain time interval
    :param v_0: Velocity at the beginning of the time interval (Double)
    :param d_t: Duration of the interval (Double)
    :param a_r: Acceleration of the rocket during the interval (Double)
    :return: Velocity of the rocket at the end of the interval (Double) [m/s]
    """
    velocitynow = v_0 + d_t * a_r
    return velocitynow


def resx(res, angle_r):
    """
    Calculates the resulting force in x-direction
    :param res: resulting factor in rocket direction (Double)
    :param angle_r: angle the rocket is facing to the horizon (Double) [grad]
    :return: resulting factor in x-direction (Double) [N]
    """
    anglerad_r = math.radians(angle_r)
    resxnow = res * math.cos(anglerad_r)
    return resxnow


def resy(res, angle_r):
    """
    Calculates the resulting force in y-direction
    :param res: resulting factor in rocket direction (Double)
    :param angle_r: angle the rocket is facing to the horizon (Double) [grad]
    :return: resulting factor in y-direction (Double) [N]
    """
    anglerad_r = math.radians(angle_r)
    resynow = res * math.sin(anglerad_r)
    return resynow
