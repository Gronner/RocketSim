"""
Author:         Felix Braeunling
Description:    This module contains the formulas for calculating the
                necessary values for the simulation on the basis of
                flight, orbital, gravitational mechanics, as well as
                other physical influences like drag.
"""


def thrust(m_dt, v_p, a_e, p_p, p_amb):
    """
    Calculates the thrust the engine is producing based on the
    following inputs
    :param m_dt: Change of mass of propellant (Double)
    :param v_p: Velocity of propellant (Double)
    :param a_e: Surface area of the exit nozzle (Double)
    :param p_p: Pressure in the area of the nozzle (Double)
    :param p_amb: Pressure of the ambient (Double)
    :return: Thrust produced by the engine (Double)
    """
    thrustnow = m_dt * v_p + a_e * (p_p - p_amb)
    return thrustnow


def drag(density, v_r, a_r, c_d):
    """
    Calculates the drag the rocket experiences based on the
    following inputs
    :param density: Density of the medium the rocket is travelling in (Double)
    :param v_r: Velocity of the rocket in travelling direction (Double)
    :param a_r: Surface area of the rocket that is exposed to drag (Double)
    :param c_d: Drag coefficient of the rocket (Double)
    :return: Drag experienced by the rocket (Double)
    """
    dragnow = 1.0/2.0 * density * v_r**2 * a_r * c_d
    return dragnow
