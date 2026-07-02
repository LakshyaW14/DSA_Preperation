# Find the Missing and Repeating number 

# Brute Force Approach 

def Find_Missing_Repeating(arr):
    # Intialize variable 
    repeating, missing = -1 , -1
    
    # Generating Num from 1 to n
    for i in range (1, len(arr) + 1 ):
        count = 0 
        
        # Iterating over the arr 
        for j in range (len(arr)):
            if arr[j] == i:
                count += 1
        # Repeating Condition 
        if count == 2:
            repeating = i
        
        # Missing condition 
        elif count == 0:
            missing = i

        # early break 
        if ( repeating != -1) and ( missing != -1):
            break

    return [repeating, missing ]

# Time Complexity O( n^2) where n is the size of array, and nested Loop 
# SC O(1) using constant amount of space for Var, regardless of input size 

# ---------------------------------------------

# Better - > hashing

def Find_Missing_Repeating_Better(arr):
    n = len(arr)
    repeating, missing = -1 , -1


    # Intialize a hash arr for counting occurrence 
    hash_arr = [0] * (n+1)

    # 
    for num in arr:
        hash_arr[num] += 1
    
    for i in range (1, n+1):
        if hash_arr[i] == 2:
            repeating = i

        elif hash_arr[i] == 0:
            missing = i

        # early break 
        if ( repeating != -1) and ( missing != -1):
            break

    return [ repeating, missing]
    

# TC O(2n)
# SC O(n) ae we are using a additional Hash arr 

# -----------------------------

arr = [ 2,3,4,1,1,6]
print(Find_Missing_Repeating(arr))
print(Find_Missing_Repeating_Better(arr))
