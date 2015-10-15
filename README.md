<h1>RocketSim</h1>
For my fifth semester I'm required to write a student research paper. It's aimed at modelling and simulating a rocket.

<h2>The Goal</h2>
As mentioned the goal is to modell a rocket mathematicly and simulate it with different properties.
At this moment the specifics are not set, but this will be done in the near future.
<p>This has to be finished till 2016.01.11</p>

<h2>Specification</h3>
The model shall be able to simulate a simple rocket on its way to an orbit and while expanding this orbit until the fuel runs out. The rocket will orbit around a single celestial body without any other bodys around this one. The model will count in the influence of the environment, like the drag from the atmosphere, flight, orbital and gravitational mechanics. All this will be done in a 2D space.
<p>Finally a real rocket will be modelled and the result will be compared with the real flight if possible</p>

<h2>The Math</h2>
<h3>Forces</h3>
<p><b>Thrust</b> ![Thrust formula](http://mathurl.com/phl3r84.png)</p> <!-- http://mathurl.com/phl3r84 -->
<p><b>Gravity</b> ![Gravity fromula](http://mathurl.com/pkwwy9z.png)</p> <!-- http://mathurl.com/pkwwy9z -->
<p><b>Drag</b> ![Drag fromula](http://mathurl.com/ojwnl7b.png)</p> <!-- http://mathurl.com/ojwnl7b -->
Those will be calculated vectorized with **Fx** and **Fy**. The resulting force is the sum of those forces. 
Acceleration can be calculated 
<h3>Boundary conditions</h3>
Thrust is dependent on used propellant and engine, but also on the pressure of the environment it is used in.

The relation between the distance of rocket and earths center of mass is already implemented with the formula for gravity.

Drag has different influcences. First the density of the medium the rocket is passing through. On earth this is dependent on the pressure and the temperature of the medium, which both are dependent of the altitude the rocket is in. This will be on one hand modelled with formulas but also with a layer model of the atmosphere.
