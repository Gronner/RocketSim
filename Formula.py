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
    :param v_p: velocity of propellant (Double)
    :param a_e: Surface Area of the exit nozzle (Double)
    :param p_p: Pressure in the area of the nozzle (Double)
    :param p_amb: Pressure of the ambient (Double)
    :return: Thrust produced by the engine (Double)
    """
    thrustnow = m_dt * v_p + a_e * (p_p - p_amb)
    return thrustnow
