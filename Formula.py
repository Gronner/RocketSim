"""
Author:         Felix Braeunling
Description:    This module contains the formulas for calculating the
                necessary values for the simulation on the basis of
                flight, orbital, gravitational mechanics, as well as
                other physical influences like drag.
"""

G = 6.67408e-10     # Newton's gravity constant             [m^3/(kg*s^2)]
M = 0.02896         # Molar mass of atmosphere gasses       [kg/mol]
R = 8.314           # universal gas constant                [J/(K*mol)]
g = 9.807           # Earths gravitational acceleration     [m/s^2]

def thrust(m_dt, v_p, a_e, p_p, p_amb):
    """
    Calculates the thrust the engine is producing based on the following inputs
    :param m_dt: Change of mass of propellant (Double)
    :param v_p: Velocity of propellant (Double)
    :param a_e: Surface area of the exit nozzle (Double)
    :param p_p: Pressure in the area of the nozzle (Double)
    :param p_amb: Pressure of the ambient (Double)
    :return: Thrust produced by the engine (Double) [N]
    """
    thrustnow = m_dt * v_p + a_e * (p_p - p_amb)
    return thrustnow


def drag(density, v_r, a_r, c_d):
    """
    Calculates the drag the rocket experiences based on the following inputs
    :param density: Density of the medium the rocket is travelling in (Double)
    :param v_r: Velocity of the rocket in travelling direction (Double)
    :param a_r: Surface area of the rocket that is exposed to drag (Double)
    :param c_d: Drag coefficient of the rocket (Double)
    :return: Drag experienced by the rocket (Double) [N]
    """
    dragnow = 1.0 / 2.0 * density * v_r**2 * a_r * c_d
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


def temperature(T_h0, a, h0, h1):
    """
    Calculates the temperature at a certain height
    :param T_h0: Temperature at the lowest point of the atmosphere layer (Double)
    :param a: Temperature gradient for the atmosphere layer (Double)
    :param h0: Height of the lower end of the atmosphere layer (Double)
    :param h1: Height of the rocket (Double)
    :return: Temperature at the height of the rocket (Double) [K]
    """
    heightdiff = h1 - h0
    temperaturenow = T_h0 * (1 - a*heightdiff)
    return temperaturenow