import matplotlib.pyplot as plt
import pandas as pd

# Data from the table
data = {
    "Instance": ["Bin packing (n=50)", "Bin packing (n=50)", "Bin packing (n=50)", "Bin packing (n=50)", "Bin packing (n=50)",
                 "Bin packing (n=100)", "Bin packing (n=100)", "Bin packing (n=100)", "Bin packing (n=100)", "Bin packing (n=100)",
                 "Bin packing (n=200)", "Bin packing (n=200)", "Bin packing (n=200)", "Bin packing (n=200)", "Bin packing (n=200)",
                 "Knapsack (n=50)", "Knapsack (n=50)", "Knapsack (n=50)", "Knapsack (n=50)", "Knapsack (n=50)",
                 "Knapsack (n=100)", "Knapsack (n=100)", "Knapsack (n=100)", "Knapsack (n=100)", "Knapsack (n=100)",
                 "Knapsack (n=200)", "Knapsack (n=200)", "Knapsack (n=200)", "Knapsack (n=200)", "Knapsack (n=200)",
                 "Mix (n=50)", "Mix (n=50)", "Mix (n=50)", "Mix (n=50)", "Mix (n=50)",
                 "Mix (n=100)", "Mix (n=100)", "Mix (n=100)", "Mix (n=100)", "Mix (n=100)",
                 "Mix (n=200)", "Mix (n=200)", "Mix (n=200)", "Mix (n=200)", "Mix (n=200)"],
    "Solver": ["Greedy", "Greedy w. local search", "GRASP", "MILP I", "MILP II",
               "Greedy", "Greedy w. local search", "GRASP", "MILP I", "MILP II",
               "Greedy", "Greedy w. local search", "GRASP", "MILP I", "MILP II",
               "Greedy", "Greedy w. local search", "GRASP", "MILP I", "MILP II",
               "Greedy", "Greedy w. local search", "GRASP", "MILP I", "MILP II",
               "Greedy", "Greedy w. local search", "GRASP", "MILP I", "MILP II",
               "Greedy", "Greedy w. local search", "GRASP", "MILP I", "MILP II",
               "Greedy", "Greedy w. local search", "GRASP", "MILP I", "MILP II",
               "Greedy", "Greedy w. local search", "GRASP", "MILP I", "MILP II"],
    "Objective": [4952, 4952, 4968, 4911, 1739,
                  19568, 19568, 19880, 17269, None,
                  79100, 79100, 79678, 36460, None,
                  2105, 2105, 2105, 2106, 2106,
                  4606, 4606, 4611, 4611, 4611,
                  9905, 9905, 9906, 9906, 9906,
                  5982, 5982, 5994, 5998, None,
                  7230, 7230, 7230, 7230, None,
                  16907, 16907, 16907, 11007, None],
    "Time (s)": [0.08, 0.17, 301.49, 1800.10, 1811.23,
                 0.09, 0.53, 547.41, 1804.89, None,
                 0.81, 1.83, 747.56, 1801.10, None,
                 0.01, 0.01, 300.00, 0.22, 0.19,
                 0.01, 0.03, 300.07, 3.42, 0.14,
                 0.01, 0.05, 300.83, 27.64, 1.42,
                 0.01, 0.11, 602.20, 1800.51, None,
                 0.03, 0.74, 300.25, 1809.09, None,
                 0.39, 16.99, 302.90, 1800.16, None]
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to plot the data
def plot_data(df, title, instances):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.set_xlabel('Solver')
    ax1.set_ylabel('Objective')
    ax1.tick_params(axis='y')

    colors = {'Bin packing (n=50)': 'red', 'Bin packing (n=100)': 'blue', 'Bin packing (n=200)': 'green',
              'Knapsack (n=50)': 'red', 'Knapsack (n=100)': 'blue', 'Knapsack (n=200)': 'green',
              'Mix (n=50)': 'red', 'Mix (n=100)': 'blue', 'Mix (n=200)': 'green'}

    lines = []
    labels = []

    for instance in instances:
        df_instance = df[df["Instance"] == instance]
        line, = ax1.plot(df_instance["Solver"], df_instance["Objective"], marker='o', label=f"{instance} Objective", color=colors[instance])
        lines.append(line)
        labels.append(f"{instance} Objective")
    
    ax1.set_title(title)
    ax1.grid(True)

    ax2 = ax1.twinx()  
    ax2.set_ylabel('Time (s)')
    ax2.tick_params(axis='y')

    for instance in instances:
        df_instance = df[df["Instance"] == instance]
        line, = ax2.plot(df_instance["Solver"], df_instance["Time (s)"], marker='x', linestyle='dashed', label=f"{instance} Time", color=colors[instance])
        lines.append(line)
        labels.append(f"{instance} Time")

    # Create a single legend
    ax1.legend(lines, labels, loc='center left', bbox_to_anchor=(1.12, 0.5), borderaxespad=0.)

    fig.tight_layout()
    plt.show()

# Plot for Bin Packing
plot_data(df, "Bin Packing Performance", ["Bin packing (n=50)", "Bin packing (n=100)", "Bin packing (n=200)"])

# Plot for Knapsack
plot_data(df, "Knapsack Performance", ["Knapsack (n=50)", "Knapsack (n=100)", "Knapsack (n=200)"])

# Plot for Mix
plot_data(df, "Mix Performance", ["Mix (n=50)", "Mix (n=100)", "Mix (n=200)"])
