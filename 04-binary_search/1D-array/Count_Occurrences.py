
# Brute Force - > Linear Search 

def Count(nums,x):
    count =0
    for num in nums:
        if num == x:
            count += 1
    return count 

# TC O(N)
# Sc O(1)


# ---------------------------------------------------

# Optimal Solution 
# Simply using the First and last occurrence Binary Search Code 
# With little Modification 

# Count = Last_Occurence_idx - First_occurrence_idx + 1 

def First(nums,x):
    low, high = 0, len(nums)-1
    ans = -1
    while ( low <= high):
        mid =( low +high)//2
        
        # For first index, we need to always move to left 
        if nums[mid] == x:
            ans = mid
            high = mid -1       # To left 
        
        # then Normal BS Application 
        elif nums[mid] < x:
            low = mid + 1   # to right 
        else:
            high = mid -1

    return ans 

def Last (nums,x):
    low, high = 0, len(nums) -1
    ans  = -1 
    while( low <= high):
        mid = ( low + high)//2

        # For Last index, we need to always move to right
        if nums [mid] == x:
            ans = mid 
            low = mid + 1

        # BS application 
        elif nums[mid] < x:
            low = mid + 1
        else:
            high = mid -1 
    return ans 

def Get_occurrence_Optimal (nums,x):
    first_idx = First(nums, x)
    if ( first_idx == -1) :
        return ( -1, -1)
    last_idx = Last(nums, x)
    return (first_idx, last_idx )

 
def Count_Occurrences (nums,x):
    first_idx = First(nums, x)
    if ( first_idx == -1) :
        return ( -1 )
    last_idx = Last(nums, x)
    return ( last_idx - first_idx + 1)

nums = [1,2,3,4,5,5,5,5,5,5,6,7,8]
print(Count_Occurrences(nums,5))
print(Count(nums,5))


# TC O(logn)
# SC O(1)