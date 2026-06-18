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

# Optimal Sol 

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



mat = [ [1, 2, 3, 4], 
       [5, 6, 7, 8],
        [9, 10, 11, 12] ]
target = 10

print(Search_Mat_optimal(mat,target))