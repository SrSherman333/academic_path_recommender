import matplotlib.pyplot as plt
from core.data_manager import WEEKLY_LOG
from core.analyzer import total_day, totals_activity, practical_proportion, recommend_route
from core.reporter import generate_report
from core.visualizer import create_graphics

def main():
    print("="*60)
    print("  ACADEMIC RECOMMENDATION SYSTEM")
    print("="*60)
    print("\nPlease enter the following information:\n")

    # Entry and validation
    while True:
        try:
            h = float(input("Available hours per day (in. 4.5): "))
            if h <= 0:
                print("Error: The times must be greater than 0")
                continue
        except ValueError:
            print("Error: Enter a valid number")
            continue
        break

    while True:
        try:
            pd = int(input("Programming difficulty (1-5, where 5 is very difficult): "))
            if pd < 1 or pd > 5:
                print("Error: Enter a value between 1 and 5")
                continue
        except ValueError:
            print("Error: Enter a valid number")
            continue
        break

    while True:
        try:
            md = int(input("Difficulty in mathematics (1-5): "))
            if md < 1 or md > 5:
                print("Error: Enter a value between 1 and 5")
                continue
        except ValueError:
            print("Error: Enter a valid number")
            continue
        break

    while True:
        try:
            r = int(input("Technical reading level (1-5, where 1 is low): "))
            if r < 1 or r > 5:
                print("Error: Enter a value between 1 and 5")
                continue
        except ValueError:
            print("Error: Enter an integer")
            continue
        break

    while True:
        try:
            Hmin = float(input("Minimum threshold of hours/day (Hmin, e.g. 3.0): "))
            if Hmin <= 0:
                print("Error: Hmin must be greater than 0")
                continue
        except ValueError:
            print("Error: Enter a valid number")
            continue
        break

    while True:
        try:
            Pmin = float(input("Minimum practice threshold (Pmin, 0.0-1.0, e.g. 0.3): "))
            if Pmin <= 0 or Pmin > 1:
                print("Error: Pmin must be between 0 and 1")
                continue
        except ValueError:
            print("Error: Enter a valid number")
            continue
        break

    # Matrix Processing
    print("\n" + "="*60)
    print("PROCESSING WEEKLY REGISTRATION...")
    print("="*60)

    # Calculate daily totals
    total_days = []
    total_weekly = 0
    weakest_day = 0
    min_hours = float('inf')

    for i, day in enumerate(WEEKLY_LOG):
        total_of_the_day = total_day(day)
        total_days.append(total_of_the_day)
        total_weekly += total_of_the_day

        # Check if it is the weakest day
        if total_of_the_day < min_hours:
            min_hours = total_of_the_day
            weakest_day = i + 1

    # Calculate totals by activity
    totals_act = totals_activity(WEEKLY_LOG)

    # Calculate practice ratio
    P = practical_proportion(totals_act)

    # Apply rules
    route, action, state = recommend_route(h, pd, md, r, P, Hmin, Pmin)

    # Generate report
    report = generate_report(total_days, totals_act, P, route, action, state)
    print(report)
    
    # Create graphics
    graphic = input("Do you want to generate the graphs? (yes/no): ")
    if graphic == "yes" or graphic == "Yes":
        create_graphics(total_days, Hmin, totals_act, P, Pmin)
    else:
        print("Canceling graphics generation")

    print("\n" + "="*60)
    print("PROCESS COMPLETED SUCCESSFULLY")
    print("="*60)
    print("\nReview the generated files:")
    print("1. recommendation_report.txt")
    print("2. line_graph.png")
    print("3. bar_chart.png")
    print("\n¡Thank you for using the referral system!")

if __name__ == "__main__":
    main()