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
    activities = ["Reading/Theory", "Exercises/Practice",
                "Project/Programming", "Review/Assessment"]
    report += "\nHours per activity:\n"
    for i in range(4):
        report += f"  {activities[i]}: {totals_act[i]:.2f} hours\n"

    report += f"\nPractice ratio (P): {P:.2%}\n"

    # Find weakest day
    weak_day = total_days.index(min(total_days)) + 1
    report += f"Day with less study: Day {weak_day}\n"

    # Find dominant activity
    dominant_activity = activities[totals_act.index(max(totals_act))]
    report += f"Dominant Activity: {dominant_activity}\n"

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