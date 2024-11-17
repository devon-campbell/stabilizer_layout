from z3 import Solver, Bool, Xor, Sum, If, Or

# Define the pre-computed minimum Hamming distances for the matrices
precomputed_distances = {
    "G1": 3,  # Pre-computed Hamming distance for G1
    "G2": 2,  # Pre-computed Hamming distance for G2
    "G3": 2,  # Pre-computed Hamming distance for G3
    "G4": 5,  # Pre-computed Hamming distance for G4
    "G5": 2,  # Pre-computed Hamming distance for G5
    "G6": 3,  # Pre-computed Hamming distance for G6
    "G7": 3   # Pre-computed Hamming distance for G7
}

# List of matrices to test
matrices = {
    "G1": [
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1]
    ],
    "G2": [
        [1, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 1]
    ],
    "G3": [
        [1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1]
    ],
    "G4": [
        [1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1]
    ],
    "G5": [
        [1, 0, 1, 1, 0, 0, 1, 0, 1, 1],
        [0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 1]
    ],
    "G6": [
        [1, 0, 1, 1, 0, 1],
        [0, 1, 1, 0, 1, 0]
    ],
    "G7": [
        [1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 1, 1, 0, 0]
    ]
}

