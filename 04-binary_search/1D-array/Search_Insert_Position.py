# Search insert Position 
# Lower Bound 
def Insert_Position(nums,x):
    low = 0
    high = len(nums) -1
    ans = len(nums) # default answer 

    while low <= high:
        mid = ( low + high)//2

        if nums[mid] >= x:
            ans = mid
            # Potential Answer 
            high = mid - 1  # look on left side 
        
        # look on right side 
        else:
            low = mid + 1
    return ans 

# Time Complexity O(logn)
# Space Complexity O(1)

nums = [1,2,4,7]
print(Insert_Position(nums, 3))