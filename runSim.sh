rm -r Results/*_*
rm -r Results_2/*_*
python RocketSim_150A.py
python RocketSim.py
cd Results
python ploting.py
cd ..
cd Results_2
python ploting.py
cd ..
echo "Finished running the simulation!"
