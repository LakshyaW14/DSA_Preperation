# Longest Consecutive Sequence 
# Brute force Approach

class Solution:

    # Helper function to perform linear search 
    def Linear_Search(self,arr, target):
        found=False
        for num in arr:
            if num == target:
                found=True
        return found
    
    # 
    

    def LCS(self,nums):
        n = len(nums)
        
        # If array is empty
        if  n == 0:
            return 0
        
        # Intialize the longest Sequence length
        longest = 1

        # Iterating
        for i in range(len(nums)):  
            # TC -> O(n)
            # Current element
            x = nums[i]

            # Count of Occurence
            count = 1

            # Search for Consecutive Numbers   
            while (self.Linear_Search(nums, x+1)) :
                # TC -> O(n^2)
                # Move to the Next Number in the Sequence
                x += 1

                # Increment the count, if consecutive numbers occurs
                count +=1

            # Update the Longest Sequence Length
            longest= max(longest, count)

        return longest

# Time Complexity: O(n^3), where n is the number of elements in the array. This is because for each element, we may need to perform a O(n) linear search.\
#       O(n^2) in worst case  through the entire array to find consecutive  all numbers.
#     nums[1,2,3,4,5,6,7,.....,n]

# Space Complexity: O(1), as we are using a constant amount of extra space for variables

#-------------------------------------------

nums =  [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] 

sol = Solution()
print(sol.LCS(nums))

