# count number of successful missions
def successful_missions(mission_success):

    counter = 0

    for x in mission_success:
        if x:
            counter += 1
    
    return counter


#_________________________________________________________________________________


# calculate success rate
def success_rate(mission_success):

    rate = float((successful_missions(mission_success) / len(mission_success)) * 100)

    return rate


#_________________________________________________________________________________


# print missions before 2000
def pre2000_missions(mission_names, mission_years):

    print("Missions launched before the year 2000:")

    for x in range(len(mission_names)):

        if mission_years[x] < 2000:

            print(f"- {mission_names[x]}")