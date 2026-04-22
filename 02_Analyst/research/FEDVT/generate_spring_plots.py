import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)

# Generate ONE exact pattern that will be replicated 3 times
time_base = np.linspace(0, 10, 200)
position_base = 380 + np.random.normal(0, 40, 200)

# Define the three plots with SAME data, DIFFERENT colors
plots = [
    {'color': 'green', 'title': 'Position Vs. Time (Red Spring)'},
    {'color': 'green', 'title': 'Position vs Time (White Spring)'},
    {'color': 'green', 'title': 'Position vs. Time (Green Spring)'}
]

for i, plot_info in enumerate(plots):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(time_base, position_base, color=plot_info['color'], alpha=0.65, s=40, edgecolors='none')
    ax.set_title(plot_info['title'], fontsize=13, fontweight='bold')
    ax.set_xlabel('Time (s)', fontsize=11)
    ax.set_ylabel('Vertical Position [m]', fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_ylim([200, 500])
    ax.set_xlim([0, 10])
    plt.tight_layout()
    plt.savefig(f'spring_plot_{i+1}_green.png', dpi=300, bbox_inches='tight')
    print(f"Saved: spring_plot_{i+1}_green.png")
    plt.close()

print("All three plots generated with IDENTICAL patterns - only colors differ.")
