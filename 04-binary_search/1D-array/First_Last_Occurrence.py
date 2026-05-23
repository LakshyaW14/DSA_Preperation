# First and last occurrence in sorted array 

# Brute Force -> Linear Search 

def Get_Occurence(nums,x):
    #
    first, last = -1, -1
    for i in range(len(nums)):
        if nums[i] == x:
            if first == -1:
                first = i 
            else:
                last= i

    return first, last 

# TC O(n)
# SC O(1)

#--------------------------------------
# Better soltion  - > Lower Bound and upper Bound 


def lower_bound(nums,x):
    low, high  = 0, len(nums)-1
    ans = len(nums)
    while ( low <= high ):
        mid = ( low + high)//2

        if nums[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1 
    return ans

def upper_bound(nums, x):
    low, high = 0, len(nums)-1
    ans = len(nums)
    while ( low <= high ):
        mid = (low +high)//2
        if nums[mid] > x :
            ans = mid 
            high = mid - 1
        else:
            low = mid + 1
    return ans 

def Get_Occurrence_Better(nums,x):
    first = lower_bound(nums, x)
    if ( first == len(nums) ) or (nums[first] != x):
        return ( -1, -1)
    last = upper_bound(nums, x) - 1 # minus one to get the last occurring index 

    return (first, last)
    

# TC O(2 x logn)
# SC O(1)

# --------------------------------------------

# Optimal Solution  -> using binary Search 


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


# TC O(logn)
# SC O(1)

#-----------------------------

nums = [1,2,3,4,5,5,5,5,5,5,6,7,8]
print(Get_Occurence(nums, 5))
print(Get_Occurrence_Better(nums, 5))
print(Get_occurrence_Optimal(nums, 5))
