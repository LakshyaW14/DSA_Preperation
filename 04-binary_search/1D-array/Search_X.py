# Binary Search 
# Iterative approach 

def BS (nums, target):
    n = len(nums)

    low = 0
    high = n -1

    # Travesing until low crosses high
    while low <= high :
        # middle index
        mid = (low + high )//2

        if nums[mid] == target:
            return mid
        
        # search in right Half
        elif nums[mid] < target:
            low = mid +1
        
        # search in left half
        else:
            high = mid -1
    # Target not found 
    return -1 


#Time Complexity: In the algorithm, in every step, we are basically dividing the search space into 2 equal halves.\
#  This is actually equivalent to dividing the size of the array by 2, every time. After a certain number of divisions, \
# the size will reduce to such an extent that we will not be able to divide that anymore and the process will stop. The number of total divisions will be equal to the time complexity. \
# So the overall time complexity is O(logN), where N = size of the given array.

# Space Complexity: 0(1), no extra space being used

# ----------------------------------------------

nums = [ 2,3,5,6,8,9,11,123]
print(BS(nums,11))