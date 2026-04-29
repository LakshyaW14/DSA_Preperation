#Check if the array is sorted or not 

class Solution :

    # Brute Force Approach 

    def IsSorted(self, nums):
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                # if any element is smaller than the previous element, it's not sorted 
                if nums[i] > nums[j]:
                    return False
            return True
        
    # Time Complexity: O(N2), as it uses two nested loops to compare every pair of elements in the array.
    
    # Space Complexity: O(1), as no extra space is used apart from a few variables.

#--------------------------------------------------------
    # Optimal Approach 
    
    def IsSorted_2 (self, nums):

        for i in range ( 1 , len(nums)):
            if nums [i] < nums[i-1]:
                return  False
        return  True
    
    # Time Complexity: O(N), as it checks each adjacent pair once in a single pass through the array.
    
    # Space Complexity: O(1), as it uses constant extra space regardless of input size.
