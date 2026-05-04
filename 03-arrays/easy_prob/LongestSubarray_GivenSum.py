
# Longest Subarray with given Sum K(Positives)

# Brute Force Array 

def Longest_Subarray (nums, k):
    n = len(nums)
    max_length = 0
    
    # Starting index
    for i in range (len(nums)):
        # Ending Index 
        for j in range (i+1, len(nums)):
            
            # Add all elements of Subarray 
            # Subarray = nums[ i:j]
            s= 0
            for k in range (i, j+1):# Subarray Traversing 
                s += nums[k]

                if ( s ==k):
                  max_length = max(max_length, j-i+1)
    return max_length   


# Time Complexity: O(n3), where n is the size of the array. \
#     This is because we have three nested loops: one for the starting index, one for the ending index, and one for calculating the sum of the subarray.

# Space Complexity: O(1), as we are using a constant amount of space for variables \
#     and not using any additional data structures that grow with input size.


# N^3 -> N^2
# Best Appraoch for Brute Force 

    # for i in range(len(nums)):
    #     s=0
    #     for j in range (i, len(nums)):
    #         s += nums[j]
    #         if s == k:
    #             max_length= max(max_length, j-i+1)
    # return max_length

#-------------------------------------------------------------
# Better  Appraoch 
"""Hashing"""
""" Prefix Sum """
# Only for Positives and also works for Negatives 

def LongestSubarray_Hashing(nums,k):
    # Running Prfix Sum 
    s=0
    # Best length so far 
    maxi = 0

    # PreSum map -> First index Seen
    mp = {}

    # Iterate Over the array 
    for i in range (len(nums)):
        # Update Running Prefix sum 
        s += nums[i]

        # Subarray from 0 to 1
        if s == k:
            # Update best length
            maxi = max (maxi , i + 1)
        
        # Subarray in between 
        # Else-> check if this sum was seen before  
        rem = s -k
        if rem in mp :
            # if seen the length becomes -> Previous index + ( 1 and i)
            length = i - mp[rem]
            maxi = max (maxi, length)

        # First time seeing this sum 
        # Store the Prefix Sum (Only first Occurrence )
        if s not in mp:
            mp[s] = i
    # Return Best length 
    return maxi 

# time complexity O(n x 1) avg case -> no collisions ( unordered map ) each hashmap lookup + insertion takes O(1) on avg
# O( n x n ) worst case  Only if all hash operations degrade (extremely unlikely in practice)
# check all subarrays

# Space Complexity O(n)


#--------------------------------------------

# Optimal Approach 
""" Two Pointers """
# Positives and Zeroes 
# Oneline Intuition -> Grow right, if sum > k, trim left 

def LongestSubarray_TwoPointer(nums,  k):

    # Intialize Two pointers to mark the start and end of the window
    left, right = 0, 0

    # Max length so far of the sub array 
    maxi = 0

    # To store the Sum of elements on the window 
    s = 0

    # iterate through the array 
    while right < len(nums):
        
        s += nums[right]

        # if the sum exceeds k, shrink the window
        while ( left <= right ) and s > k :
            s -= nums[left]
            left += 1
        
        # if the Sum is equal to k
        if s == k:
            # Update the Max_Length 
            maxi = max(maxi, right-left+1)

        # Update the right pointer 
        right += 1
        
    
    # Return the Max length 
    return maxi 

# Time Complexity: O(2N), where N is the size of the array. The algorithm traverses the array once with two pointers, making it linear in time complexity.
# The Inner Loop won't run for n times all the time

# Space Complexity: O(1), as it uses a constant amount of space.



# Important Constraint (Very Important for Interviews)

# This two-pointer / sliding window approach ONLY works when:

#  -> All elements in nums are non-negative

# Why?
# Because shrinking the window reduces the sum predictably.
# If negatives exist → sum can behave unpredictably → sliding window fails.

# For arrays with negative numbers, you must use:
# ->  Prefix Sum + Hashing (your previous approach)
        

#--------------------------------------------

nums = [10, 5, 2, 7, 1, 9]
print(LongestSubarray_TwoPointer(nums, 15))