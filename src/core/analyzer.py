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
    route = "Focus on "
    difficult = max(d)
    if difficult >= 4:
        max_difficult = {}
        for i, value in enumerate(data_manager.activities):
            if d[i] >= 4:
                max_difficult[value] = (data_manager.survey_data[value][0], d[i])
                
        for i, value in enumerate(max_difficult):
            if (max_difficult[value][0] == 2 and max_difficult[value][1] == difficult) or P < Pmin:
                route += f"|{value}| "
            elif max_difficult[value][0] == 1 and max_difficult[value][1] == difficult:
                route += f"|{value}|"
    else:
        route = "Balanced"

    # Determine secondary action
    if state == "Appropriate":
        action = "Maintain current pace"
    elif state == "In adjustment":
        if hours_day and not fulfills_practice:
            action = "Increase practice (exercises and projects)"
        else:
            action = "Increase daily study hours"
    else:
        action = "Review habits and redistribute time urgently"

    return route, action, state