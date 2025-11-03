"""
Create a function that receives a (square) matrix and calculates the sum of both diagonals (main and secondary).

Example
[   // 3x3 matrix
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

// Should return 30: (1 + 5 + 9) + (3 + 5 + 7)
MatrixAlgorithms

level : 7kyu
"""

def sum_diagonals(matrix):
    size = len(matrix)
    total = 0
    for i in range(size):
        total += matrix[i][i]
        total += matrix[i][size-i-1]
    return total