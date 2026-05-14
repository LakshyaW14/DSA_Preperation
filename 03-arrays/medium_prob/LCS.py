# Longest Consecutive Sequence 
# Brute force Approach

class Solution:

    # Helper function to perform linear search O(N^2)
    def Linear_Search(self,arr, target):
        found=False
        for num in arr:
            if num == target:
                found=True
        return found
    

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


# Better Approach 
# Using Sorted Array 

    def LCS_Better (self,nums):
        n=len(nums)

        # return 0 if the array is empty
        if n == 0:
            return 0

        nums.sort()

        # the last smaller element
        last_smaller = float('-inf')

        # count current sequence length 
        count = 0

        # longest sequence length 
        longest = 1

        for i in range(n):
            # if consecutive element exist 
            if nums[i] - 1 == last_smaller:

                # update count for new sequence
                count +=1
                # update last smaller
                last_smaller = nums[i]

            # if no consecutive number exist (i.e. a new sequence is found )
            elif nums[i] != last_smaller:
                # reset counter for new sequence 
                count = 1
                # update last smaller 
                last_smaller = nums[i]
            
            # update longest
            longest= max(longest, count)
        return longest

#Time Complexity: O(n log n) + O(n), where n is the number of elements in the array. This is due to the sorting step, which is the most time-consuming operation in this approach.

# Space Complexity: O(1), as we are using only a constant amount of extra space.

#------------------------------

#Optimal solution 
# using SET ds 

    def LCS_Optimal(self,nums):
        n=len(nums)
        if n == 0:
            return 0
        
        #store the arr in set
        st=set(nums) # O(n)

        # Initialize the longest sequence length
        longest = 1 

        # Iterate through the set 
        for num in st:      # O(n)
            # Check if it is a starting number of sequence
            if ( num -1 ) not in st:
                # Intialize the count
                count =1
                # Staring element of the sequence
                x = num
                
                #Find the Consecutive numbers in set 
                while ( x+1 ) in st:
                    # Move to the Next Element in the sequence 
                    x += 1
                    # Increment the count 
                    count += 1
                
                # update the longest
                longest = max(longest, count)
        return longest 


# Time Complexity: O(n), where n is the number of elements in the array. This is because we traverse each element once to build the set and then again to find the longest consecutive sequence.

# Space Complexity: O(n), as we use a set to store the unique elements of the array, which in the worst case can be equal to the size of the input array.        

#-----------------------------------------


nums =  [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] 

sol = Solution()
print(sol.LCS(nums))
print(sol.LCS_Better(nums))
print(sol.LCS_Optimal(nums))


