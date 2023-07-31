import matplotlib.pyplot as plt
import csv
from datetime import datetime
from matplotlib.animation import FuncAnimation

csv_file = 'data_log.csv'

# Function to update the graph with new data
def update_graph(i):
    # Read data from CSV and store in lists
    timestamps = []
    people_counts = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:  # Ensure valid row data with timestamp and people count
                timestamp_str, people_count_str = row
                try:
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                    people_count = float(people_count_str)
                    timestamps.append(timestamp)
                    people_counts.append(people_count)
                except ValueError:
                    pass  # Ignore invalid rows

    # Clear previous plot and update the graph
    plt.cla()
    plt.plot(timestamps, people_counts, marker='o', linestyle='-', color='b')
    plt.xlabel('Time')
    plt.ylabel('People Count')
    plt.title('People Count Over Time')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

# Create the animated graph
ani = FuncAnimation(plt.gcf(), update_graph, interval=5000)  # Update every 5 seconds

# Show the plot
plt.show()
