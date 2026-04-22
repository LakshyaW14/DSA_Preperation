# Move all Zeros to the end of the array

def move_Zero_to_end (nums):

    temp =[0] * len(nums)
    # Pointer to fill temp 
    index =0

    # Traverse input array 
    for num in nums :
        # if non- zero element, copy to temp
        if num != 0:
            temp[index] = num
            index +=1
        
    # Copy temp back to original array 
    for i in range (len(nums)):
        nums[i] = temp[i]
    
    # return updated array 
    return nums
    # or just return Temp, if don't want to modify the original array 


# Time Complexity: O(N), we can move all zeroes to end in linear time.
# Space Complexity: O(N), additional space used for temporary array.

#-------------------------------------------------------

# Optimal Approach ( Two Pointers )
def Move_Zeros_(nums):
    # Pointer to first zero 
    j = -1

    # Find the first zero 
    for i in range (len(nums)):
        if nums[i] == 0:
            j=i
            break

        # If no zeros are found 
    if j == -1:
            return -1
        
        # Starts from next index of first zero
    for i in range (j+1, len(nums)):
        # If current element is non-zero 
        if nums[i] != 0:
            # swap with nums[j]

            nums[i], nums[j] = nums[j], nums[i]
            # move J to next zero 
            j+=1
    return nums

# Time Complexity: O(N), we can move all zeroes to end in linear time.
# Space Complexity: O(1), constant additional space is used.



arr=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
print(Move_Zeros_(arr))