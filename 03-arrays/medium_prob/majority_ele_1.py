# Find the Majority Element that occurs more than N/2 times

# Brute force approach 
#  

class Solution :

    def Majority_element_1 (self, nums: list[int]) -> int:

        n =len(nums)

        # Iterate through each element of the array 
        for i in range (n):
            # counter to count the occurrence of nums[i]
            count = 0 

            #count the frequency of the nums[i] in the array 
            for j in range (n):

                if nums[i] == nums[j]:
                    count +=1

            # check if the freq is greater than n/2
            if count > ( n/2 ):
                return nums[i]
        return -1
    


# Time Complexity: O(N^2), where N is the size of the input array. \
#     This is because we are using a nested loop to count the occurrences of each element.

# Space Complexity: O(1), as we are using a constant amount of space for the counters and indices.            


#-----------------------------------------------

# Better Approach ( Hashing )

    def Majority (self, nums):
        n = len(nums)

        # hash map to store the frequency of element 
        mp ={}

        # Count Occurrence of element 
        for num in nums:
            if num in mp :
                mp[num] += 1
            else:
                mp[num] = 1

        """ Iterate through the map to find the majority element """
        for num, count in mp.items():
            if count > n // 2 :
                return num

        # for num in nums:
        #     mp[num] = mp.get(num,0) +1
        # for num in nums:
        #     if mp[num] > n// 2 :
        #         return num
        return -1


# Time Complexity: O(N), where N is the size of the input array. \
#     This is because we are iterating through the array once to count occurrences and then iterating through the hashmap to find the majority element.


# Space Complexity: O(N), as we are using a hashmap to store the counts of each element,\
#       which can take up to N space in the worst case.

#-------------------------------------------------------------------

# Optimal Approach ( Moor's Voting Algorithm)


    def Majority_Optimal (self,nums):
        n =len(nums)

        # Count Pointer 
        count = 0

        #Element pointer 
        ele = 0

        # Applying the Algo
        for num in nums:
            if count == 0 :
                count = 1
                ele = num
            
            elif ele == num:
                count +=1
            else:
                count -=1
            
        """ Checking if the stored element is the majority element """
        count_1 = nums.count(ele)

        # Return element if it is a Majority element
        if count_1 > ( n // 2):
            return ele
        
        return -1


# Time Complexity: O(N), where N is the size of the input array. This is because we are iterating through the array once to find the potential majority element and then again to verify it.

# Space Complexity: O(1), as we are using only a constant amount of extra space.

#------------------------------------------------------------

nums =[7, 0, 0, 1, 7, 7, 2, 7, 7]  
obj = Solution()
print(obj.Majority_Optimal(nums))

