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
            if row[mid] == target :
                return mid
            elif row[mid] < target:
                low = mid + 1
            else:
                high = mid + 1
        return -1 
            
    # traverse every row of mat 
    index = -1          # O(n)
    for row in range(n):
        index = BS(row,target)
        if index != -1 :
            return row , index 
    return -1,-1


# Time Complexity O( n * logm)
# Space Complexity O(1)

