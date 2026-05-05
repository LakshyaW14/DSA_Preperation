# Rearrange array elements by sign 
# Positive numbers and negative numbers are equal in number 
# len(pos) == len(neg)
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

def Rearrange_Elements_optimal(nums):
    n = len(nums)

    ans = [0] * n # Intialize result array with zeroes

    # Even index for positive numbers 
    pos_idx = 0

    # Odd index for negative numbers 
    neg_idx = 1

    for num in nums :
        if num < 0:
            # Place negative at odd indices 
            ans[neg_idx] = num
            neg_idx += 2
        else:
            # Place pos at even indices
            ans[pos_idx] = num
            pos_idx += 2
    return ans


# Time Complexity: O(N) { O(N) for traversing the array once and substituting positives and negatives simultaneously using pointers, where N = size of the array A}.

# Space Complexity: O(N) { Extra Space used to store the rearranged elements separately in an array, where N = size of array A}.

nums = [ 3,1, -2, -5, 2, -4 ]
print(Rearrange_Elements(nums))
print(Rearrange_Elements_optimal(nums))



#-------------------------------------------------

# Second Variant -> len(pos) != len(neg )
# using modfified brute force approach 


def Rearrange_Ele (nums):
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

    # Two conditions if len(pos) != len(neg)
    # pos = [ 3,1,4,5] -> len 4
    # neg = [-2, -1] -> len 2

    if len(pos) > len(neg):
        for i in range (len(neg)):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]

        # for left overs numbers 
        idx = len(neg) *2
        for i in range (len(neg), len(pos)):
            nums[idx] = pos[i]
            idx +=1


    # if len(pos) < len(neg)
    else:
        for i in range (len(pos)):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]

        # for left overs numbers 
        idx = len(pos) *2
        for i in range (len(pos), len(neg)):
            nums[idx] = neg[i]
            idx +=1

    return nums

num = [ 3, -2, 5, 6, -1, 8]
print(Rearrange_Ele(num))
