# find the majority Element ( > n/ 3) 


# Brute Force 
def Majority_Element_two (arr):
    ans = []
    n = len(arr)

    # First loop 
    for i in range (n):
        # Variable to store the frequency 
        count = 0
        # skip duplicates 
        if arr[i] in ans :
            continue

        for j in range (n ):
            if arr[i] == arr[j]:
                count += 1
        
        if count > ( n//3 ):
            ans.append(arr[i])

        # Early break -> at most only two elements 
        if len(ans) == 2 :
            break 
    return ans 

# TC O(n^2) nested loop 
# SC O(1)

# ----------------------------------------------


nums = [1, 2, 1, 1, 3,2, 2]  
print(Majority_Element_two(nums))
