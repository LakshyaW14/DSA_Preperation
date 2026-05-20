# Lower Bound  
# Brute Force Approach 


# Smallest Index such that ( nums[idx] >= x )
def Lower_Bound (nums, x):
    for i in range (len(nums)):
        if nums[i] >= x:
            # First index Where Element is >= x
            return i
    # if x is greater than all element
    return len(nums)


# Time Complexity: O(N), where N = size of the given array.
# Space Complexity: O(1), no extra space used.
# ---------------------------------


# Optimal Approach
def Lower_Bound_Optimal (nums,x):
    low = 0
    high = len(nums) -1

    # Default value if value not found
    ans = len(nums)

    while low <= high:
        mid = (low + high )//2

        if nums[mid] >= x:
            ans = mid
            # move to left 
            high = mid - 1
        else:
            # Move to right
            low = mid + 1

    return ans

# Time Complexity: O(logn), used for typical binary search
# Space Complexity: O(1), no extra space used

#----------------------------------------

nums = [3, 5, 8, 15, 19]
print(Lower_Bound(nums,9))
print(Lower_Bound_Optimal(nums,))
