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

matrix = [[1,1,1,1],[1,0,1,1],[1,1,1,0]]
sol=solution()
sol.Set_Mat_Zero(matrix)
for row in matrix:
    print(row)