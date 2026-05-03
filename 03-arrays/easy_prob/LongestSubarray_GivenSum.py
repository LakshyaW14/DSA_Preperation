
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
# Optimal Appraoch 
"""Hashing"""
# Only for Positives and Negatives 

def LongestSubarray_Hashing(nums,k):
    # Running Prfix Sum 
    s=0
    # Best length so far 
    maxi = 0

    # PreSum map -> First index Seen
    mp = {}

    # Iterate Over the array 
    for i in range (len(nums)):
        # Update Running sum 
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



nums = [10, 5, 2, 7, 1, 9]
print(LongestSubarray_Hashing(nums, 15))