import matplotlib.pyplot as plt
import numpy as np
from src.core.data_manager import data_manager

def create_graphics(total_days, Hmin, totals_act, P, Pmin):
    print("Generating visualizations...")

    # 1. LINE GRAPH: DAILY TOTAL
    plt.figure(figsize=(10, 5))

    # Create chart
    days = list(range(1, 8))
    plt.plot(days, total_days, marker='o', linewidth=2, markersize=8,
                color='steelblue', label='Hours studied')

    # Reference line Hmin
    plt.axhline(y=Hmin, color='red', linestyle='--', linewidth=1.5,
                label=f'Minimum threshold ({Hmin} h/day)')

    # Highlight days below the threshold
    for i, total in enumerate(total_days):
        if total < Hmin:
            plt.annotate(f'{total:.1f}h', xy=(i+1, total), xytext=(0, -15),
                        textcoords='offset points', ha='center', color='red',
                        fontweight='bold')

    plt.title('DAILY EVOLUTION OF STUDY HOURS', fontsize=14, fontweight='bold')
    plt.xlabel('Day of the week', fontsize=12)
    plt.ylabel('Study hours', fontsize=12)
    plt.xticks(days)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('line_graph.png', dpi=150)
    print("✓ Line graph saved as 'line_graph.png'")

    # 2. BAR CHART: HOURS BY ACTIVITY
    plt.figure(figsize=(10, 5))

    activities_names = data_manager.activities
    num_activities = len(activities_names)
    
    colors = plt.cm.tab10(np.linspace(0, 1, num_activities))

    bars = plt.bar(activities_names, totals_act, color=colors, edgecolor='black')

    # Label values
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.2f}h', ha='center', va='bottom', fontweight='bold')

    # Show warning if P < Pmin
    if P < Pmin:
        plt.text(0.5, max(totals_act)*0.9, f'P = {P:.1%} < Pmin ({Pmin:.0%})',
                fontsize=12, color='red', ha='center',
                bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.5))

    plt.title('WEEKLY DISTRIBUTION BY ACTIVITY', fontsize=14, fontweight='bold')
    plt.xlabel('Activities', fontsize=12)
    plt.ylabel('Accumulated hours', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig('bar_chart.png', dpi=150)
    print("✓ Bar chart saved as 'bar_chart.png'")

    plt.show()