import numpy as np

# Let's assume we already have the final probability distribution from Task 1
# This probability distribution will have values for S = 5 to S = 50

# For simplicity, we will regenerate the probability distribution of the dice
tetrahedron = np.ones(4) / 4     # 4-sided die (Tetrahedron)
cube = np.ones(6) / 6            # 6-sided die (Cube)
octahedron = np.ones(8) / 8      # 8-sided die (Octahedron)
dodecahedron = np.ones(12) / 12  # 12-sided die (Dodecahedron)
icosahedron = np.ones(20) / 20   # 20-sided die (Icosahedron)

# Perform the discrete convolution step-by-step
conv_tetra_cube = np.convolve(tetrahedron, cube)
conv_tetra_cube_octa = np.convolve(conv_tetra_cube, octahedron)
conv_tetra_cube_octa_dodeca = np.convolve(conv_tetra_cube_octa, dodecahedron)
final_conv = np.convolve(conv_tetra_cube_octa_dodeca, icosahedron)

# The probability distribution now contains probabilities for S = 5 to S = 50

# Define the winning condition: S ≤ 10 or S ≥ 45
# The sums range from 5 to 50, and the index in the final_conv array starts from 5.

# First, sum the probabilities for S ≤ 10
prob_less_than_or_equal_10 = np.sum(final_conv[:6])  # S = 5 to S = 10 (index 0 to 5)

# Now, sum the probabilities for S ≥ 45
prob_greater_than_or_equal_45 = np.sum(final_conv[40:])  # S = 45 to S = 50 (index 40 to end)

# Total winning probability
total_winning_probability = prob_less_than_or_equal_10 + prob_greater_than_or_equal_45

# Output the result
print(f"Probability of winning (S ≤ 10 or S ≥ 45): {total_winning_probability:.5f}")
