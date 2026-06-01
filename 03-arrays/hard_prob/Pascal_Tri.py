# Generate Pascal Triangle 

# prob 01 -> Given row and col, tell the element at that place 
# prob 02 -> Print Nth row of the pascal's triangle
# Prob 03 -> print the Pascal's Triangle

def Get_Ele_Pascal_Tri(row, col):
    # Zero Based Indexing 
    n = row -1
    r = col -1

    res = 1
    # Computing c(n,r) using iterative formula
    for i in range(r):

        res *= ( n - i)
        res //= ( i + 1)
    
    return res

# TC O(r)
# SC O(1)




# print(Get_Ele_Pascal_Tri(5,3))

print(print_nth_row(3))


