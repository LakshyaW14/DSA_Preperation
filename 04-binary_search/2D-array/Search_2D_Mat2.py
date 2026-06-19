# Search in 2D matrix - 2

# Brute force approach 
# Linear Search 

def Search_linear(mat,target):
    n = len(mat)
    m = len(mat[0])

    for row in range(n):
        for col in range(m):
            if mat[row][col] == target:
                return True 
    return False

# O(n * m)

# --------------------------------------------
# Better Appraoch 

def Search_better (mat, target):

    n = len(mat)
    m = len(mat[0])
    def BS(arr, target):            # O(logm)
        low = 0
        high = m-1
        while ( low <= high):
            mid = ( low + high)//2
            if arr[mid] == target :
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1 
            
    # traverse every row of mat 
    index = -1                     # O(n)
    for row in range(n):
        index = BS(mat[row],target)
        if index != -1 :
            return row , index 
    return -1,-1


# Time Complexity O( n * logm) where N = given row number, M = given column number. We are traversing all rows and it takes O(N) time complexity. 
# And for all rows, we are applying binary search. So, the total time complexity is O(N*logM).
# Space Complexity O(1)

#----------------------------------------------

# optimal Sol 

def Search_2D_Mat_Optimal (mat, target):
    n = len(mat)
    m = len(mat[0])

    row, col = 0, m-1

    # Intuition -> Only Two Ways sideways or downwards 
    # if target is smaller --> move to sideways 
    # if greater --> move to downwards 

    while ( row < n ) and ( col >= 0):
        # if the Corner Ele is Target 
        if mat[row][col] == target :
            return row,col
        
        # target is greater than corner element
        elif mat[row][col]  < target :
            row += 1

        else:
            col -= 1
    return False 

# TC O( n + m ) where N = given row number, M = given column number. We are starting traversal from (0, M-1), and at most, we can end up being in the cell (M-1, 0). So, 
# the total distance can be at most (N+M). So, the time complexity is O(N+M).
# SC O(1)

#--------------------------

matrix= [[1,  4,   7 ,  11],
         [2,   5,   8,   12],
         [3,   6,   9,   16],
         [10, 13,  14,  17]]

print(Search_2D_Mat_Optimal(matrix, target=10))
