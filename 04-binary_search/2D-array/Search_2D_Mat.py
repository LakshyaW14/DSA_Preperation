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
    

mat = [ [1, 2, 3, 4], 
       [5, 6, 7, 8],
        [9, 10, 11, 12] ]
target = 13

# TC O( n x m)
# SC O(1)

#---------------------------------------------------------------


print(search_mat(mat,target))