from src.core.data_manager import data_manager
# Function to generate a text report with metrics and recommendations
def generate_report(total_days, totals_act, P, route, action, state):
    report = "\n" + "="*60 + "\n"
    report += "         ACADEMIC RECOMMENDATION REPORT\n"
    report += "="*60 + "\n\n"

    report += "WEEKLY METRICS:\n"
    report += "-"*40 + "\n"

    # Show totals per day
    report += "Hours per day:\n"
    for i, total in enumerate(total_days, 1):
        report += f"  Day {i}: {total:.2f} hours\n"

    report += f"\nWeekly total: {sum(total_days):.2f} hours\n"

    # Show totals by activity
    activities = data_manager.activities
    report += "\nHours per activity:\n"
    for i, value in enumerate(activities):
        report += f"  {value}: {totals_act[i]:.2f} hours\n"

    report += f"\nPractice ratio (P): {P:.2%}\n"

    # Find weakest day
    weak_day = min(total_days)
    weakest_days = []
    for i, value in enumerate(total_days):
        if weak_day == value:
            weakest_days.append(i+1)
            
    if len(weakest_days) == 1:
        report += f"Day with less study: Day {weakest_days[0]}\n"
    elif len(weakest_days) == 7:
        report += "Day with less study: They dedicate the same amount of time to each day\n"
    else:
        days = ", ".join(map(str, weakest_days))
        report += f"Day with less study: Days {days} (tied)\n"

    # Find dominant activity
    dominant_activity = []
        
    dominant_value = max(totals_act)
    for i, value in enumerate(totals_act):
        if dominant_value == value:
            dominant_activity.append(data_manager.activities[i])
            
    if len(dominant_activity) == 1:
        report += f"Dominant Activity: {dominant_activity}\n"
    elif len(dominant_activity) == len(totals_act):
        report += "Dominant Activity: All activities have the same level of dedication\n"
    else:
        num_activities = ", ".join(dominant_activity)
        report += f"Dominant Activity: {num_activities}\n"

    report += "\n" + "RECOMMENDATIONS:" + "\n"
    report += "-"*40 + "\n"
    report += f"Suggested route: {route}\n"
    report += f"Weekly status: {state}\n"
    report += f"Specific action: {action}\n"

    report += "\n" + "="*60 + "\n"

    # Save to file
    try:
        with open("recommendation_report.txt", "w", encoding="utf-8") as f:
            f.write(report)
        print("✓ Report saved as 'recommendation_report.txt'")
    except:
        pass

    return report