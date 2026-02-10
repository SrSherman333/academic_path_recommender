from src.core.data_manager import data_manager
# Functions for the logic of the program
def total_day(daily_list):
    # Calculate the total number of hours in a day
    return sum(daily_list)

def totals_activity(matrix):
    # Calculate weekly totals by activity (sum by columns)
    totals = []
    
    for i in range(len(data_manager.activities)):
        totals.append(0)

    for day in matrix:
        for i in range(len(data_manager.activities)):
            totals[i] += day[i]
            
    return totals

def practical_proportion(totals):
    # Calculate the proportion of practice hours (Exercises + Project)
    indexs = []
    for i, value in enumerate(data_manager.activities):
        if data_manager.survey_data[value][0] == 2:
            indexs.append(i)
            
    totals_practice = 0
    for i in indexs:
        totals_practice += totals[i]
            
    total_weekly = sum(totals)

    if total_weekly > 0:
        return (totals_practice) / total_weekly
    else:
        return 0.0

def recommend_route(h, d, P, Hmin, Pmin):
    # Apply the rules to generate recommendations
    daily_average = h

    # Classify weekly status
    hours_day = daily_average >= Hmin
    fulfills_practice = P >= Pmin

    if hours_day and fulfills_practice:
        state = "Appropriate"
    elif hours_day or fulfills_practice:
        state = "In adjustment"
    else:
        state = "Critical"

    # Determine main route
    route = ""
    difficult_practice = {}
    for i, value in enumerate(data_manager.activities):
        if d[i] >= 4 and data_manager.survey_data[value][0] == 2:
            difficult_practice[value] = (data_manager.survey_data[value][0], d[i])
            
    difficult_theory = {}
    for i, value in enumerate(data_manager.activities):
        if d[i] >= 4 and data_manager.survey_data[value][0] == 1:
            difficult_theory[value] = (data_manager.survey_data[value][0], d[i])
    
    levels = []
    if P < Pmin and len(difficult_practice) > 0:
        levels.append(1)
    if P >= Pmin and len(difficult_practice) > 0:
        levels.append(2)
    if len(difficult_theory) > 0:
        levels.append(3)
    if len(difficult_practice) <= 0 and len(difficult_theory) <= 0:
        if P < Pmin:
            levels.append((4, 1))
        elif P >= Pmin:
            levels.append((4, 2))
            
    for i in levels:
        lst_activities = []
        if i == 1:
            for name, values in difficult_practice.items():
                lst_activities.append(f"{name}({values[1]})")
            activities = ",".join(lst_activities)
            route += f"CRITICAL PRIORITY: Focus intensively on {activities}\n"
        elif i == 2:
            for name, values in difficult_practice.items():
                lst_activities.append(f"{name}({values[1]})")
            activities = ",".join(lst_activities)
            route += f"FOCUS ON PRACTICE: Improvement {activities}\n"
        elif i == 3:
            for name, values in difficult_theory.items():
                lst_activities.append(f"{name}({values[1]})")
            activities = ",".join(lst_activities)
            route += f"REINFORCE THEORY: Strengthens {activities}\n"
        elif type(i) == tuple:
            if i[0] == 4 and i[1] == 1:
                route += "INCREASE GENERAL PRACTICE: Your practice ratio is low, but you don't have any specific weaknesses. Allocate more time to practice activities.\n"
            elif i[0] == 4 and i[1] == 2:
                route += "BALANCED PATH: Your difficulties are spread out. Maintain consistency and focus on gradually improving all areas.\n"

    # Determine secondary action
    if state == "Appropriate":
        action = "Maintain current pace"
    elif state == "In adjustment":
        if hours_day and not fulfills_practice:
            action = "Increase practice"
        else:
            action = "Increase daily study hours"
    else:
        action = "Review habits and redistribute time urgently"

    return route, action, state