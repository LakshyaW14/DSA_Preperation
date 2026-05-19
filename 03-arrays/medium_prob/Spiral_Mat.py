# Print the Matrix in Spiral Manner 
# Optimal Solution 
def Spiral_Mat (matrix):
    # Get Dimensions of matrix 
    row = len(matrix)
    col = len(matrix[0])

    # Result array 
    res = [] 

    # Intialize the four pointers ( Boundaries )
    left = 0 
    top = 0
    right = col -1
    bottom = row -1

    # loop within the valid boundaries 
    while(top <= bottom and left <= right):

        # Traverse the Top Row ( left -> right )
        for i in range ( left, right +1):
            res.append(matrix[top][i])
        # move top boundary down 
        top += 1

        # traverse the right col ( top -> bottom )
        for i in range (top, bottom+1):
            res.append(matrix[i][right])
        # move right boundary to left 
        right -= 1
        
        # check for remaining rows ( if only one row exist )
        if top <= bottom:
            # traverse the bottom row ( right-> left )
            for i in range ( right, left-1 , -1):
                res.append(matrix[bottom][i])
            # move bottom boundary up 
            bottom -= 1

        # check for remaining cols
        if left <= right:
            # traverse the left col ( bottom -> top)
            for i in range ( bottom , top -1 , -1):
                res.append(matrix[i][left])
            # move left boundary to right
            left += 1
        
    return res

#Time Complexity: O(m × n),Because we visit each element of the matrix exactly once, \
# where `m` is the number of rows and `n` is the number of columns.

# Space Complexity: O(1)We use only a few integer variables to keep track of boundaries (top, bottom, left, right). \
#     The `result` vector is part of the output, so it's not counted as extra space.


#---------------------------------------------------
matrix = [
    [ 1, 2, 3, 4 ,5],
    [  6, 7, 8,9,10 ],
    [ 11, 12, 13, 14, 15 ],
    [ 16, 17 ,18, 19, 20 ]
]
print(Spiral_Mat(matrix))