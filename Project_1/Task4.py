import numpy as np
import matplotlib.pyplot as plt

# Function to simulate the dice rolls and estimate the probability of winning
def monte_carlo_simulation(num_trials):
    # Number of sides for each die (Platonic solids)
    tetrahedron_sides = 4     # 4-sided die (Tetrahedron)
    cube_sides = 6            # 6-sided die (Cube)
    octahedron_sides = 8      # 8-sided die (Octahedron)
    dodecahedron_sides = 12   # 12-sided die (Dodecahedron)
    icosahedron_sides = 20    # 20-sided die (Icosahedron)

    # Counter for the number of wins
    wins = 0

    # Monte Carlo simulation for 'num_trials' trials
    for _ in range(num_trials):
        # Roll each die (random number between 1 and the number of sides)
        roll_tetrahedron = np.random.randint(1, tetrahedron_sides + 1)
        roll_cube = np.random.randint(1, cube_sides + 1)
        roll_octahedron = np.random.randint(1, octahedron_sides + 1)
        roll_dodecahedron = np.random.randint(1, dodecahedron_sides + 1)
        roll_icosahedron = np.random.randint(1, icosahedron_sides + 1)

        # Calculate the sum of the five dice
        dice_sum = (roll_tetrahedron + roll_cube + roll_octahedron +
                    roll_dodecahedron + roll_icosahedron)

        # Check if the sum meets the winning condition (S ≤ 10 or S ≥ 45)
        if dice_sum <= 10 or dice_sum >= 45:
            wins += 1  # Increment the win counter

    # Estimated probability of winning
    return wins / num_trials

# List of different values of N (number of trials)
trial_values = [10, 100, 1000, 10000, 100000]

# To store the estimated probabilities for each N
estimated_probabilities = []

# Perform Monte Carlo simulation for each value of N
for N in trial_values:
    estimated_probability = monte_carlo_simulation(N)
    estimated_probabilities.append(estimated_probability)
    print(f"Estimated probability of winning after {N} trials: {estimated_probability:.5f}")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(trial_values, estimated_probabilities, marker='o', linestyle='-', color='b', label='Estimated Probability')
plt.xscale('log')  # Use logarithmic scale for the number of trials (N)
plt.xlabel('Number of Trials (N)')
plt.ylabel('Estimated Probability of Winning')
plt.title('Convergence of Estimated Winning Probability with Increasing Trials')
plt.grid(True)
plt.legend()
plt.show()
