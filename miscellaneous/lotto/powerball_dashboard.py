import random
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Function to generate all possible combinations of 5 numbers
def generate_combinations():
    combinations = []
    for i in range(1, 70):
        for j in range(i+1, 70):
            for k in range(j+1, 70):
                for l in range(k+1, 70):
                    for m in range(l+1, 70):
                        combinations.append([i, j, k, l, m])
    return combinations

# Function to draw 5 numbers from the list of combinations
def draw_numbers(combinations):
    return random.choice(combinations)

# Function to compare a player's numbers to the drawn numbers
def compare_numbers(player_numbers, drawn_numbers):
    matches = 0
    for num in player_numbers:
        if num in drawn_numbers:
            matches += 1
    return matches

# Define the player's numbers
player_numbers = [1, 2, 3, 4, 5]

# Run the simulation and store the results in a DataFrame
combinations = generate_combinations()
results = []
matches = 0
for i in range(10):  # Change this to the number of simulations you want to run
    drawn_numbers = draw_numbers(combinations)
    num_matches = compare_numbers(player_numbers, drawn_numbers)
    if num_matches >= 3:
        matches += 1
    results.append([i+1, drawn_numbers, num_matches])

df = pd.DataFrame(results, columns=["Drawing", "Drawn Numbers", "Matches"])

# Create the dashboard
fig = make_subplots(rows=1, cols=2)

# Add the table of results
fig.add_trace(go.Table(
    header=dict(values=list(df.columns), fill_color='paleturquoise', align='left'),
    cells=dict(values=[df[col] for col in df.columns], fill_color='lavender', align='left')
))

# Add the bar chart of matches
fig.add_trace(go.Bar(
    x=df["Drawing"],
    y=df["Matches"],
    name="Matches"
))

# Update the layout
fig.update_layout(
    title="Powerball Simulation Results",
    xaxis_title="Drawing",
    yaxis_title="Matches"
)

# Show the dashboard
fig.show()

# Calculate and display the probability of winning
probability = matches / 10
print(f"Probability of winning with 3 or more numbers: {probability:.2f}")
