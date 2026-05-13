# Leaders in Array 

# Brute force Approach 

def Leaders_InArray(nums):
    ans=[]
    # Iterate over the entire array
    for i in range(len(nums)):
        leader = True
        # check if nums[i] is greater than all of his element in right 
        for j in range(i+1, len(nums)):
            # if any element, that means nums[i] isn't a Leader 
            if nums[i] < nums[j]:
                leader= False
                break
        # if Leader, add it to ans list 
        if leader:
            ans.append(nums[i])
        
    return ans
        
# Time Complexity: O(N^2), where N is the size of the input array. This is because we have a nested loop where the outer loop runs N times and the inner loop runs up to N times in the worst case.

# Space Complexity: O(1), as we are using only a constant amount of extra space for the answer array, which does not depend on the input size.



#------------------------------------------------
# Optimal Solution 

def Leaders_Optimal (nums):
    ans=[]
    
    # Last element always a leader
    # last ele is fixed, so max-val=nums[-1]
    max_val = float('-inf')

    # iterating Backwards starting for last second element 
    for i in range(len(nums)-1, -1, -1):
        # Checking element from right to left
        
        if nums[i] > max_val:
            ans.append(nums[i])
            max_val = nums[i]

    # ans.reverse() for matching the order
    return ans


# Time Complexity: O(N), where N is the size of the input array. This is because we traverse the array only once.

# Space Complexity: O(1), as we are using only a constant amount of extra space

#---------------------------------------------------

nums=[10, 22, 12, 3, 0, 6]
print(Leaders_InArray(nums))
print(Leaders_Optimal(nums))

        