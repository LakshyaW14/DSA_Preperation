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
        
        # if count_row > max_count: max_count = count_row 
        max_count = max(max_count, count_row)
        index = row
    
    return index

# TC O(n *m)
# SC O(1)

#---------------------------------------------------

matrix = [[0, 0, 1, 1, 1 ],
          [0, 0, 0, 0, 0 ],
          [0, 0, 0, 1, 1],
          [0, 0, 1, 1, 1],
          [0, 1, 1, 1, 1]]

print(Find_row_max_1s(matrix))
