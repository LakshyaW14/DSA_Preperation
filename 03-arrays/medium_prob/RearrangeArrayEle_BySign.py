# Rearrange array elements by sign 

# Brute Force Approach 

def Rearrange_Elements(nums):

    # List to store the positive numbers
    pos = []
    # List to store the negatives numbers
    neg = []

    # iterating through array and separate Positives and negatives 
    for num in nums:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)

    # Place positives at even indices, negatives at odd indices

    for i in range (len(nums)//2):
        nums[2 * i] = pos[i]
        nums[2 * i +1] = neg[i]

    return nums

# Time Complexity: O(N+N/2) { O(N) for traversing the array once for segregating positives and negatives and another O(N/2) for adding those elements alternatively to the array, where N = size of the array A}.

# Space Complexity: O(N/2 + N/2) = O(N) { N/2 space required for each of the positive and negative element arrays, where N = size of the array A}.

#------------------------------------------------------

# optimal Approach 

def Rearrange_Elements_optimal 