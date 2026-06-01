# Set Matrix Zero 
# Brute Force Approach 

class solution:
    
    def Set_Mat_Zero(self, matrix):
        # Get number or rows
        n = len(matrix)

        # Get number of cols
        m = len(matrix[0])

        MARK = None
        # Or MARk = float('inf') for matrix2 and matrix3 Edge Case 

        # Helper Function to mark row
        def mark_row(row,col,matrix):
                
            for col in range(m):
                if matrix[row][col] != 0:
                    matrix[row][col] = MARK
        
        # Helper function to mark col

        def mark_col(row,col,matrix):
            for row in range(n):
                if matrix[row][col] != 0:
                    matrix[row][col] = MARK

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
                if matrix[i] [j] == MARK:
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
        row_arr = [0] * n
        col_arr = [0] * m

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


# Optimal Approach

# like Better Appraoch -> move the hasharray inside the matrix ( like a inplace modification )

    def SetMat_Optimal (self, matrix):

        # Important Intuition follow-up
        # col[] = matrix[0][]
        # row[] = matrix[][0]
        
        # Zero filling intuition 
        # first-> subarray excluding(row and col hash-arrays)
        # second-> col_arr

        # Get Dimensions of Matrix
        n = len(matrix)
        m = len(matrix[0])

        # variable for marking the  first col of matrix
        col0 = 1
        # y col0 is needed

        #cannot represent BOTH:
            # whether first row should be zero
            # whether first column should be zero
        # So:
            # matrix[0][0] → first row marker
            # col0 → first column marker

        # This is the key intuition.

        # First Pass: marking the hash arr of row and col 
        for i in range( n):
            for j in range( m):
                if matrix[i][j] == 0:
                    # Mark the i-th row
                    matrix[i][0] = 0

                    # mark the j-th col
                    if j == 0:
                        col0 = 0

                    # when j != 0:
                    else:     
                        matrix[0][j] = 0

        # Second Pass :
        # Sub array marking zero 
        # set zero in INNER Matrix, ignoring the hash-array 
        for i in range(1,n):
            for j in range(1, m):
                if matrix[i][j] != 0:       # this step can be removed, coz assigning zero again costs nothing -> simpliflies logic
                    # check for col and row
                    if ( matrix[i][0] == 0 ) or (matrix[0][j]==0):
                        matrix[i][j] = 0
                  
        # print(col0)

        # handle the top first row, that dependent on mat[0][0] to be set zero 
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        
        # handle the first col, that dependent on the variable col0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0


#Time Complexity: O(m × n),We iterate over the entire matrix a constant number of times (first pass for markers, second pass for zeroing, final pass for first row/col), where m = number of rows and n = number of columns.

# Space Complexity: O(1),No extra space is used apart from a few boolean flags; all marker information is stored within the first row and column of the matrix itself.
 

# -------------------------------------------------------

# cleaner version of optimal solution 

    def cleaner_Set_Mat(self, matrix):

        n = len(matrix)
        m = len(matrix[0])


        # Flag to track if first row should be zeroed
        first_row_zero = False
        # similarly 
        first_col_zero = False

        # Check for zero in row 
        for j in range(m):
            if matrix[0][j] == 0: 
                first_row_zero = True
                break
        # col check 
        for i in range(n):
            if matrix[i][0] == 0: 
                first_col_zero = True
                break
        # use first row and col as markers 
        for i in range(1,n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # set inner array cells to zero based on markers  
        for i in range(1,n):
            for j in range(1, m):
                if (matrix[i][0] == 0) or (matrix[0][j]) == 0:
                    matrix[i] [j] = 0


        # zero the first row if needed
        if first_row_zero:
            for j in range(m):
                matrix[0][j] = 0

        # zero the first col if needed
        if first_col_zero:
            for i in range(n):
                matrix[i][0] = 0
                       
# Tc and Sc same as Optimal Sol


#------------------------------------------------------------------------------------

matrix = [[1,1,1,1,1],[1,1,0,1,1],[0,1,1,1,1]]
matrix2 = [[-1,2,3]]
matrix3 = [[-1,1,1],[1,0,1],[1,1,-1]]
sol=solution()
sol.Set_Mat_Zero(matrix3)
# sol.SetMat_Better(matrix)
# sol.SetMat_Optimal(matrix)
# sol.cleaner_Set_Mat(matrix)

for row in matrix3:
    print(row)