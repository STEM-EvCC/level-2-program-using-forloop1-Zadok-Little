from counting_functions import *

mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# Counts the total number of space missions.
print(f"Total number of missions: {len(mission_names)}")
print(f"Number of successful missions: {successful_missions(mission_success)}")
print(f"Success rate: {success_rate(mission_success):.2f}%")
pre2000_missions(mission_names, mission_years)