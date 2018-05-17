# RocketSim
This is the result of a student research thesis I did in my fifth bachelor semester.
The goal is to simulate the three basic forces **thurst, gravity and drag** acting on a rocket during it's ascent and descent.
I tried to compare how two-stage rockets perform in comparision with one-stage rockets using a rocket modelled after a sounding rocket.
## Modell
The simulation process does the following:
1. Calculate thurst, gravitational force and drag on the rocket using the values from the previous steps
2. Making use of the equations of motion to calculate acceleration, velocity and position in a two-dimensional space
3. Based on thurst and the ISP of the rocket calculate the used fuel
4. If a stage's fuel is depleted the stage is discared if possible
5. Increase the timestep and start 1.
6. The simulation ends when the rocket hits the ground again (y < 0)

Influences on the rocket behaviour that are modelled include:
* Change of air density through the earths atmosphere and thus the change in pressure the rocket is experiencing
* Change in weight, as fuel deplets 
* The dependence of the gravity on the distance between two attracting bodies of mass

The following factors are not included in the current state of the simulation:
* The rocket is currently only launched in Y-direction, reducing the problem to a one-dimensional one.
* This also avoids the problem of drag on a changing surface and the effect of sidewinds
* Stage changes take no time
* Only a two-body problem is solved, so other celestial bodies are not taken into account
* As a the parameters of a sounding rocket are used, no orbit is achived. This is also not possible as long as the rocket only travels in Y-direction 

The one stage rocket only makes use of a liquid fuel thruster, whereas the two-stage rocket uses a solid fuel booster as it's first stage.

## Approach
To modell the rocket in Python an object oriented approach is used. 
This allows an easy creation of simulation scenarios as well as easy logging of all the important data.
The classes used are:
* Rocket Parts
* The Rocket itself
* Planets 
* Atmospheric Layers
* An Atmosphere made of any combination of these layers
* A Data object for logging values important to the simulation evaluation

For the thesis real live data was used such as:
* A sounding rocket used in early space the Aerobee 150
* The composition of earth atmosphere
* Earths mass is used for the calculation of gravity

All forces are represented as vectors.

Two draw a comparision between two-stage and one stage rockets the maximum height reached was used as the deciding factor.
After initial simulations the single stage rockets seemed to perform better than two-stage rockets.
To prove this fact the distribution of fuel in both stages of the two-stage rocket was altered to calculate the optimal distribution of the same fuel mass between the two stages.
These simulations converged to a solution where all fuel was stored in the second stage, with the first stage discarded in the first time step, making it equivalent to a single stage rocket.

It has to be noted that the use case for two stage rockets is not a configuration where first and second stage are equal, but where they are adepted to the different environments they are used in, like the vacuum of space and earths atmosphere.

## The Thesis
The resulting thesis (in german) can be found in this repository as the thesis.pdf
