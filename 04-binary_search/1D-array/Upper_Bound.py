# Upper Bound ->
# Smallest Index such that ( nums[i] > x)

# Iterative Appraoch 
# linear Search 
def Upper_Bound (nums, x):
    for i in range(len(nums)):
        if nums[i] > x:
            return i # First ele > x
    return len(nums)

# Time Complexity: O(N), where N = size of the given array.
# Space Complexity: O(1), no extra space used.

# ----------------------------------

#  BS
def Upper_Bound_Optimal (nums, x):
    low = 0
    high = len(nums) -1 
    ans = len(nums)
    # Default ans 
    while low <= high :

        mid = ( low + high )//2
        # 
        if nums[mid] > x:
            ans = mid
            high = mid - 1 # Search left 
        # search right 
        else:
            low = mid + 1
    return ans
        
# Time Complexity: O(logn), used for typical binary search
# Space Complexity: O(1), no extra space used


# ------------------------------------

nums = [3,5,8,9,15,19]
print(Upper_Bound(nums,9))
print(Upper_Bound_Optimal(nums,9))