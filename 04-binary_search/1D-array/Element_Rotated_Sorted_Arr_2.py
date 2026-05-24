# Search in Rotated Sorted Array part-1
# With Duplicates values


# Brute Force -> Linear Search

def Find_Element_Brute_2 (nums, x):
    for num in nums:
        if num == x:
            return True
    return False


# TC O(N)

# ----------------------------------------

# Optimal Solution 

# Key Follow up -> For duplicates values the conditions that stops the previous optimal sol is 
# If the values of ( nums[low] == nums[mid] === nums[high]) are Equal 
# We Can't identify the Sorted halves

def Find_Element_optimal_2 (nums, x):
    low, high = 0, len(nums)-1
    
    while ( low <= high):

        mid = ( low + high)//2
        
        # Edge Case
        if ( nums[mid] == x):
            return True 
        
        # THE EDGE Case -> ( The Duplicates Values)
        if ( nums[low] == nums[mid] == nums[high]):
            low = mid + 1
            high = mid - 1
            continue
    
        
    # For LEFT Half to be sorted 
        if ( nums[low] <= nums[mid] ):

            # Check if the TARGET Exist in left half 
            if ( nums[low] <= x < nums[mid]):

                # if exist, than eliminate the RIGHT Half
                high = mid -1
            
            else:
                low = mid + 1
                # Eliminate the LEFT half
        
    # For RIGHT Half to be sorted
        # ( nums[ mid] <= nums[high])
        else:
            # Check for Target
            if ( nums[mid] < x <= nums[high]):

                low = mid + 1
                # Eliminate the left 
            else:
                high = mid - 1
                # Eliminate the Right 

    # if not Found
    return False

#Time Complexity: O(logN) for the best and average case. O(N/2) for the worst case. Here, N = size of the given array.

# Space Complexity: O(1), no extra space used


# ---------------------------------

nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
print(Find_Element_Brute_2(nums,9))
print(Find_Element_optimal_2(nums,3))
