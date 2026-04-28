
class Solution :

    # Sort an array of s, 1s and 2s

    # Brute Force approach : sort the array with sort function 
    def Sort (self,nums):
        return sorted(nums)
    # Tc - O(nlogn) for sorting the array , SC O(n) sorted function creates the new list of arr of size n

    #--------------------------------------------------------


    # Better Approach 

    def SortZeroOneTwo(self, nums):
        # initialize three variable for 0s, 1s and 2s
        count0 = count1 = count2 = 0 

        # Count Frequency of 0s, 1s and 2s 
        for num in nums :
            if num == 0:
                count0 +=1
            elif num == 1:
                count1 +=1
            else:
                count2 +=1

        # Overwrite the array with sorted values
        index =0 
        for _ in range ( count0):
            nums[index] = 0
            index +=1
        for _ in range ( count1):
            nums[index] = 1
            index +=1
        for _ in range (count2):
            nums [ index] = 2
            index +=1
        return nums


    # Time Complexity: O(2n),We traverse the array twice: once to count, once to overwrite. Each operation is O(n).

    # Space Complexity: O(1), We use only a constant number of counters regardless of the input size. No extra array is used.


    #------------------------------------------------------------------

    # Optimal approach ( Dutch National flag Algorithm)

    # We divide the array into three partitions using three pointers – low, mid, and high.
    # From 0 to low-1, we’ll keep only 0s
    # From low to mid-1, only 1s
    # From high+1 to n-1, only 2

    # The range from mid to high is the unsorted zone we’re scanning and fixing. At each step:

    def Sort_Zero_One_Two(self,nums):
        # Initialize the three pointers : low and mid at 0, high at the end
        low, mid, high = 0, 0, len(nums) -1

        # Traverse until mid crosses high 
        while ( mid <= high ):

            # if element is 0, swap with low, move both pointers forward 
            if nums[mid] == 0 :
                nums[low], nums[mid] = nums[mid], nums[low]
                low +=1
                mid +=1

                # if element is 1, just move the mid pointer 
            elif nums[mid] == 1:
                mid +=1

                # if element is 2, swap with high , move only high backward
            else:
                nums [mid], nums[high] = nums[high], nums[mid]
                high -= 1

                
    # Time Complexity: O(n) The array is traversed only once using the `mid` pointer. \
    # Each element is checked at most once, and swaps are done in constant time.

    # Space Complexity: O(1) Only a few integer pointers (`low`, `mid`, `high`) are used. \
    # Sorting is done in-place, requiring no additional space.


nums = [ 0,1,1,0,1,2,1,2,0,0,0]
obj = Solution()
obj.Sort_Zero_One_Two(nums)
print(nums)