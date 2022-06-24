"""
Sa inversam liniile cu coloanele matricei
"""

my_matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

for i in range(len(my_matrix)):  # ROW
    for j in range(len(my_matrix[i])):  # COLUMN
        print(my_matrix[j][i], end=" ")
    print()
