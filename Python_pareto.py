import matplotlib.pyplot as plt

def plot_pareto_chart(categories, values):
    """Generates a Pareto chart with bars and a cumulative line."""
    fig, ax1 = plt.subplots()
    
    # Bar chart
    ax1.bar(categories, values, color='skyblue')
    ax1.set_xlabel('Categories', color='skyblue')
    ax1.set_ylabel('Values', color='skyblue')
    ax1.tick_params(axis='y', colors='skyblue')
    
    # Line chart for cumulative values
    ax2 = ax1.twinx()
    cumulative_values = [sum(values[:i+1]) for i in range(len(values))]
    ax2.plot(categories, cumulative_values, color='red', marker='o')
    ax2.set_ylabel('Cumulative Values', color='red')
    ax2.tick_params(axis='y', colors='red')
    
    # Title and show plot
    plt.title('Pareto Chart')
    plt.show()

if __name__ == "__main__":
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
    values = [80, 20, 50, 30]
    plot_pareto_chart(categories, values)