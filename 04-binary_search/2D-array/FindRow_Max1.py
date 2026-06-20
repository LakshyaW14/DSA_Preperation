# Find Row With maximum 1s

# Brute Force Approach 

def Find_row_max_1s(mat):
    n =len(mat)
    m = len(mat[0])

    # Intialize 
    max_count, index = -1, -1
    # Traverse the mat 
    for row in range (n):
        count_row = 0
        for col in range(m):
            count_row += mat[row][col]
        
        if count_row > max_count:
            max_count = count_row 
            index = row
    
    return index

# TC O(n *m)
# SC O(1)

#---------------------------------------------------


# Optimal Solution 
# Intuition -> Linear row traversing with BS
# We can use Lower_Bound (1)
# Upper_Bound (0)
# First Occurence 
def Upper_Bound(arr, n, target):
    low = 0
    high = n - 1
    ans = n
    while ( low <= high):
        mid = ( low + high)//2
        if arr[mid] > target:
            ans=mid
            high = mid -1
        else:
            low = mid + 1
    return ans 

def Find_max_1s_Optimal (mat):
    n = len(mat)
    m = len(mat[0])

    # Intialize Variables
    max_count, index = 0, -1
    # Max_count is zero because if the number not exist in LB or UB it gives a hypothetical number n, then it goes 5-5 = 0 which is wrong 

    for row in range(n):
        count_ones = ( m - Upper_Bound(mat[row],m, 0) ) # number of 1s
        if count_ones > max_count:
            max_count = count_ones
            index = row
    return index 

# Time Complexity:O(n X logm), where n = given row number, m = given column number. We are using a loop running for n times to traverse the rows. Then we are applying binary search on each row with m columns.

# Space Complexity: O(1), no extra space is used.

# -----------------------------------------------

matrix = [[0, 0, 1, 1, 1 ],
          [0, 0, 0, 0, 0 ],
          [0, 0, 0, 1, 1],
          [0, 1, 1, 1, 1],
          [0, 1, 1, 1, 1]]

print(Find_row_max_1s(matrix))
print(Find_max_1s_Optimal(matrix))
