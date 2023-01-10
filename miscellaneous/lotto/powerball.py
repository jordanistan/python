import random

def simulate_drawing():
    # Use the top 20 most common white ball numbers
    white_balls = random.sample(range(1, 70), 5)

    # Use the top 5 most common powerball numbers
    powerball = random.choice(range(1, 27))
    return white_balls, powerball

# Define lists of all possible ball numbers
all_white_balls = list(range(1, 70))
all_powerballs = list(range(1, 27))

# Initialize dictionaries to store the number of times each ball has been drawn
white_balls_drawn = {i: 0 for i in all_white_balls}
powerballs_drawn = {i: 0 for i in all_powerballs}

# Run the simulation 100 times
for _ in range(100):
    white_balls, powerball = simulate_drawing()
    for ball in white_balls:
        white_balls_drawn[ball] += 1
    powerballs_drawn[powerball] += 1

# Sort the white balls by the number of times they were drawn
sorted_white_balls = sorted(white_balls_drawn.items(), key=lambda x: x[1], reverse=True)

# Generate 10 combinations of the top 20 white balls and the Powerball
for i in range(10):
    combination = [ball for ball, _ in sorted_white_balls[:20]] + [sorted(powerballs_drawn.items(), key=lambda x: x[1], reverse=True)[0][0]]

    # Print the combination in the Powerball format
    print(f"Playing combination {i+1}: {sorted(combination[:5])} {combination[5]}")
