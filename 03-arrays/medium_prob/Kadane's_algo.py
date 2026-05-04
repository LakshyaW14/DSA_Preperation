# Maximum Subarray Sum 
# Brute Force Approach 
# Three nested loop
# 
def Kadane_algo (nums):

    # Initialize maximum sum with the smallest possible integers
    maxi = float ('-inf')
    
    # Iterate over Each starting index of subarray 
    for i in range(len(nums)):

        # Iterate over the ending index of subarray starting from i
        for j in range (i, len(nums) ):

            # To store the sum of current element
            s = 0
            #  Calculate the sum of subarray nums [i...j]
            for k in range (i, j+1):
                s += nums[k]

            # Update maxi with maximum of it's current value and the sum of the current subarray
            
            maxi = max(maxi, s)       
    return maxi 

# TC O(n^3)
# SC O(1)
# def Kadane_Algo (arr)


    
    pass

nums = [-2,1, -3, -4, -1, -2, 1, 5, 4]
print(Kadane_algo(nums))