# Rotate Matrix by 90 Degree
# Brute Force Approach 


# Intuition 
# row becomes col, after rotataion 
# so for first row of matrix, where n = 4 
# [0][0] -> [0][3]
# [0][1] -> [1][3]
# [0][2] -> [2][3]
# [0][3] -> [3][3]


def Rotate_matrix (matrix):

    # Get the size of the array 
    n = len(matrix)

    # create a new mat of same size to store the rotated result 
    ans= [[0] * n for _ in range(n)]
          

    # Traverse each element of original mat 

    for i in range(n):
        for j in range(n):
            # place the element at it's rotated position
            ans[j][n-1-i] = matrix[i][j]

    return ans




#Time Complexity: O(N²),Each element of the matrix is visited exactly once and placed into a new matrix, \
# so the time taken is proportional to the total number of elements.

# Space Complexity: O(N²),We use an additional matrix of the same size to store the rotated result, \
# leading to O(N²) extra space.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Helper Function 
def Print_Mat(mat):
    for row in mat:
        print(row)


print("original Array ->")
Print_Mat(matrix)
Rotated_Array= Rotate_matrix(matrix)
print("Rotated Mat ->")
Print_Mat(Rotated_Array)
