import numpy as np

# Define the probability distributions for each die
# Each die has an array where all outcomes have equal probability
# The probability distribution arrays represent the outcomes of the dice

tetrahedron = np.ones(4) / 4     # 4-sided die (Tetrahedron)
cube = np.ones(6) / 6            # 6-sided die (Cube)
octahedron = np.ones(8) / 8      # 8-sided die (Octahedron)
dodecahedron = np.ones(12) / 12  # 12-sided die (Dodecahedron)
icosahedron = np.ones(20) / 20   # 20-sided die (Icosahedron)


# Perform the discrete convolution step-by-step
# Convolve the first two dice: Tetrahedron and Cube
conv_tetra_cube = np.convolve(tetrahedron, cube)

# Convolve the result with the Octahedron
conv_tetra_cube_octa = np.convolve(conv_tetra_cube, octahedron)

# Convolve the result with the Dodecahedron
conv_tetra_cube_octa_dodeca = np.convolve(conv_tetra_cube_octa, dodecahedron)

# Finally, convolve the result with the Icosahedron
final_conv = np.convolve(conv_tetra_cube_octa_dodeca, icosahedron)

# Print the final probability distribution for the sum of the five dice
# The sum starts from 5 (1+1+1+1+1), so we adjust the index accordingly
print("Probability distribution for the sum of the Platonic dice:")
for i, prob in enumerate(final_conv, start=5):
    print(f"Sum {i}: Probability = {prob:.5f}")