# Find the Kth MIssing Number 

# Brute Force 
# Using Math 

# intuition - [ 1 2 3 (4) 5 6 (7) 8 (9) (10)]
def Kth_Missing_Num(arr, K):
    for num in arr:
        if num <= K:
            K += 1
        # if the number is greater than k
        else:
            break 

    return K

# TC O(n)
# SC O(1)

#-------------------------------------------


vec = [4,7,9,10 ]
k = 6
print(Kth_Missing_Num(vec, k))