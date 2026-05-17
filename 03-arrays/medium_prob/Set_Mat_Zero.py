# Set Matrix Zero 
# Brute Force Approach 

class solution:
    
    def Set_Mat_Zero(self, matrix):
        # Get number or rows
        n = len(matrix)

        # Get number of cols
        m = len(matrix[0])

        # Helper Function to mark row
        def mark_row(row,col,matrix):
                
            for col in range(m):
                if matrix[row][col] != 0:
                    matrix[row][col] = -1
        
        # Helper function to mark col

        def mark_col(row,col,matrix):
            for row in range(n):
                if matrix[row][col] != 0:
                    matrix[row][col] = -1

        # First pass: mark each row and col
        for i in range (n): # row   (nxm)
            for j in range (m): # col

                # if current element is zero
                if matrix [i] [j] == 0:
                    # mark entire row 
                    mark_row(i,j,matrix)    #O(N)
                    # mark entire col
                    mark_col(i,j,matrix)    #O(M)

        # Second Pass: replace -1 with 0
        for i in range(n):      #O(nxm)
            for j in range(m):
                if matrix[i] [j] == -1:
                    matrix[i][j] = 0

# Time Complexity: O(m * n * (m + n)), We iterate through every cell (m * n), and for each zero, we potentially mark its entire row (O(n)) and column (O(m)), leading to O(m * n * (m + n)) overall.
#                   nearly about O(N^3) 
# Space Complexity: O(1), We are not using any extra data structures, only modifying the matrix in place (apart from a few variables).


#-----------------------------------------------------------------

# Better Approach 
# using hash arr 


    def SetMat_Better (self, matrix):
        # rows
        n = len(matrix)
        # col 
        m = len(matrix[0])

        # Hash Arrays for rows and col 
        row_arr = [0] * (m +1)
        col_arr = [0] * (n +1)

        # first Pass : mark rows ans col that needs to be a zero 
        for i in range(n):
            for j in range(m):
                # if element is zero, mark
                if matrix[i][j] == 0:
                    row_arr[i] = 1
                    col_arr[j] = 1


        # Second Pass: set zero to cells based on markers 
        for i in range (n):
            for j in range(m):
                # if row or col is marked, set zero
                if (row_arr[i] or col_arr[j]) == 1:
                    matrix[i][j] = 0

# Time Complexity: O (2(m × n)),We make two passes over the matrix.\
# First pass to identify rows and columns to be zeroed (O(m × n)).Second pass to update the matrix using the markers (O(m × n)).Total time is proportional to the number of cells in the matrix, so O(m × n).
# Space Complexity: O(m + n),We store two extra arrays one for m rows and one for n columns. /
# No other extra space is used besides these arrays.


#---------------------------------------------------------------------------


matrix = [[1,1,1,1],[1,0,1,1],[1,1,1,0]]
sol=solution()
# sol.Set_Mat_Zero(matrix)
sol.SetMat_Better(matrix)
for row in matrix:
    print(row)