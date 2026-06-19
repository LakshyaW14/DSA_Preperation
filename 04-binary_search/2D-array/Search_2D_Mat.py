# Search in 2D matrix - Variation 1

# Brute force - > Linear Search 

def search_mat(mat, target):
    row = len(mat)
    col = len(mat[0])
    for i in range(row):
        for j in range (col):
            if mat[i][j] == target:
                return True
    return False
    



# TC O( n x m)
# SC O(1)

#---------------------------------------------------------------


# Better Approach 

def BS(low, high, target):
    while ( low <= high):
        mid = ( low + high )//2

        if mid == target :
            return True
        elif mid > target:
            high = mid -1
        else:
            low = mid + 1
    return False

def Search_Mat_Better (mat, target):
    row = len(mat)
    col = len(mat[0])

    
    # Loop for Traversing correct rows 
    for i in range(row):
        if mat[i][0] <= target <= mat[i][col-1]:
            # If the row with target exist, use BS to find the target 
            return BS(mat[i][0], mat[i][col-1], target)
        
    return False

# TC O(n x logm)
# SC O(1)

#----------------------------------------------------------------

# Optimal Sol ( Better for interview )

def Search_Mat_optimal (mat, target ):
    n = len(mat)
    m = len(mat[0])

    #  intial range 
    low = 0 
    high = n * m - 1

    # perform BS
    while low <= high:
        mid = (low + high )//2

        # convert 1D Index to 2d Indices
        row = mid // m
        col = mid % m

        if mat[row][col] == target :
            return True
        elif mat[row][col] < target :
            low = mid + 1
        else:
            high = mid - 1

    return False


# Time Complexity: O(log(NxM)), where N = given row number, M = given column number.We are applying binary search on the imaginary 1D array of size NxM.

# Space Complexity: O(1) as we are not using any extra space.


# ---------------------------------------------

# Optimal Sol 2

def BS_optimal(mat, target ):
    n = len(mat)
    m = len(mat[0])

    start_row = 0 
    end_row= n -1

    def Search_row(row, mat, target ): # O(logm ) Runs For only One time 
        low = 0
        high = m -1 
        while ( low <= high ):
            mid = ( low + high )//2 
            if mat[row][mid] == target:
                return True
            elif mat[row][mid] < target :
                low = mid + 1
            else:
                high = mid - 1
        return False
     
    while ( start_row <= end_row):      # O(logn ) Find the Correct row 
        mid_row = ( start_row + end_row)//2

        if mat[mid_row][0] <= target <= mat[mid_row][m-1] :
            return Search_row(mid_row, mat, target)
        elif mat[mid_row][m-1] <  target:
            start_row = mid_row + 1
        else:
            end_row = mid_row - 1
    return False 

# TC O(logn + logm)
# SC O(1)


mat = [ [1, 2, 3, 4], 
       [5, 6, 7, 8],
        [9, 10, 11, 12] ]
target = 10

print(BS_optimal(mat,target))