# Functions for the logic of the program
def total_day(daily_list):
    # Calculate the total number of hours in a day
    return sum(daily_list)

def totals_activity(matrix):
    # Calculate weekly totals by activity (sum by columns)
    totals = [0, 0, 0, 0]

    for day in matrix:
        for i in range(4):
            totals[i] += day[i]

    return totals

def practical_proportion(totals):
    # Calculate the proportion of practice hours (Exercises + Project)
    exercise_hours = totals[1]
    project_hours = totals[2]
    total_weekly = sum(totals)

    if total_weekly > 0:
        return (exercise_hours + project_hours) / total_weekly
    else:
        return 0.0

def recommend_route(h, pd, md, r, P, Hmin, Pmin):
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
    if pd >= 4 or P < Pmin:
        route = "Programming"
    elif md >= 4 and r >= 3:
        route = "Math"
    elif r <= 2:
        route = "Technical Reading"
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