# Minimum in Rotated Sorted Array 

# Brute Force Approach -> Linear search 

def Find_Minimum(nums):
    mini = float('inf')
    for num in nums:
        mini = min( mini, num)
    return mini

# Tc O(N)
#-------------------------------

# Optimal Approach -> Binary Search 

def Find_mini_Rotated_Sorted (nums):
    low, high = 0, len(nums)-1
    mini = float('inf')

    while ( low <= high):

        # if entire search space is already sorted
        if ( nums[low] <= nums[high] ):
            mini = min ( mini, nums[low])
            break 

        
        mid = ( low + high)//2
        
    # left half is sorted part
        if ( nums[low] <= nums[mid]):
            mini = min( mini, nums[low])

            # search in right half
            low = mid + 1
            
    # right half is sorted 
            # ( nums[mid] <= nums[high])
        else:
            # search in left half 
            high = mid -1
            mini = min( mini, nums[mid])


    return mini

# Time Complexity: O(logN), at every step the search space is reduced to half using binary search.
# Space Complexity: O(1), constant additonal space is used.

#------------------------

# Cleaner Version 

def Find_Minimum_Cleaner (nums):
    low, high = 0, len(nums)-1
    while ( low < high):

        mid = ( low + high)//2
        
        # Which half to discard i.e. Sorted half
        if ( nums[mid] > nums[high]):
            
            # Minimum lies in right half ( unsorted one)
            low = mid + 1
        # left Half 
        else:
            #  Minimum lies in left half ( including mid)
            high = mid

    # return the minimum element
    return nums[low]



nums = [7,8,9,10,1,2,3,4,5,6]
print(Find_Minimum(nums))
print(Find_mini_Rotated_Sorted(nums))
print(Find_Minimum_Cleaner(nums))