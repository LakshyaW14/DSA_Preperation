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

# Optimal Sol 
# Intuition 1) Find the nearby index 2) Find the number 

def Find_Kth_Missing_Optimal (arr, K):
    low = 1 
    high = len(arr) - 1

    while ( low <= high):
        mid = ( low + high)//2

        # 1-> Finding the nearby Index 
        no_of_missing = arr[mid] - (mid+1)

        # if the No_of_missing num is smaller than required 
        # Move forward for higher num 
        if no_of_missing < K:
            low = mid + 1

        # if Greater num move Backwards 
        else:
            high = mid - 1
        # at the end ( high ) at the starting index of ans 


        # 2 -> Find the number within the Index  
        # arr[high] + ( k - missing)
        # 7 + ( 5 -3 ) -> 9 ans 

        # Return  (high + 1 + k ) or  low = high + 1
        return low + k

    
# TC O(logn )
# SC O(1)

# ------------------------------
        

vec = [4,7,9,10 ]
arr = [2,3,4,7,11]
k = 6
print(Kth_Missing_Num(vec, k))
print(Find_Kth_Missing_Optimal(arr, 5))