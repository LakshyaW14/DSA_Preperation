# The number that appears once, other twice 

# Brute Force Approach 

def FindNum (nums):

    # First element 
    for i in range (len(nums)):
        # checking if the other similar element exist
        # occurence count variable  
        count =0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count +=1
        if count == 1:
            return nums[i] 

# Tc O(n^2) nested loops
#Sc O(1)

#-------------------------------------------------

# Better Appraoch 
"""Hashing"""

def FindNum_hashing(nums):
    
    # find max value to create hash_arr
    maxi = max(nums)

    #  create Hash array and intialize 
    hash_arr = [0] * ( maxi +1)

    # Storiong the frequency of the element
    for num in nums:
        hash_arr[num] += 1
    # searching for single occurring element
    for num in nums:
        if hash_arr[num] == 1:
            return num
        
# Time Complexity: O(N)+O(N)+O(N), where N = size of the array. One O(N) is for finding the maximum, the second one is to hash the elements and the third one is to search the single element in the array.

# Space Complexity: O(maxElement+1) where maxElement = the maximum element of the array.

#---------------------------------------------------

# optimal Approach 
"""Xor"""

def FindNum_Xor(nums):
    xor = 0

    # xor all elements -> duplicates numbers cancels out 
    for num in nums:
        xor ^= num
    
    return xor 
        

# Time Complexity: O(N). Where N is the size of the array

# Space Complexity: O(1). No extra space used

#--------------------------------------------------
nums = [1,2,4,1,2]
print(FindNum_Xor(nums))