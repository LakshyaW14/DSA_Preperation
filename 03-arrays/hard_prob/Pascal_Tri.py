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

# -----------------------------------------

# Optimal Solution 

def Generate_Row(row):
    ans_row = []
    res = 1 
    ans_row.append(1)
    for i in range(row):
        res *= row - i
        res //= i + 1
        ans_row.append(res)
    return ans_row

def Pascal_Tri (n):
    ans = []
    for i in range(n):
        ans.append(Generate_Row(i))
    return ans 




# print(Get_Ele_Pascal_Tri(5,3))

print(Pascal_Tri(5))


