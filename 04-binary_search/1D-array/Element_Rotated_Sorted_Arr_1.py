# Search in Rotated Sorted Array part-1
# only UNIQUE values

# Brute Force 
# Linear search 

def Find_element(nums,x):
    for num in nums:
        if num == x:
            return nums.index(num)
        
    return -1 

# Tc O(n)
#-------------------------------------

# Optimal solution 
# Follow up -> "Search" and "Sorted" give hint to use Binary Search 

# Intuition ->
# For Normal BS scenario-> Both the Two Halves Left and Right in sorted order 
# But For this problem -> Only either of one half is sorted 

# Key Follow Up -> IDENTIFY the Sorted half of the array 


def Find_Element_optimal (nums, x):
    low, high = 0, len(nums)-1
    
    while ( low <= high):

        mid = ( low + high)//2
        
        # Edge Case
        if ( nums[mid] == x):
            return mid 
        
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
    return -1



nums =  [7,8,9,1,2,3,4,5,6]
print(Find_element(nums, 1))
print(Find_Element_optimal(nums, 1))
