# Floor and Ceil in Sorted Array 

class FloorCeilFinder:

    # Floor -> <= x
    def Find_Floor(self, nums, x):
        low, high = 0, len(nums)-1
        ans = -1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] <= x:
                ans = nums[mid]
                low = mid +1
                # To Right
            else:
                high = mid - 1
                # To left                 
        return ans

    
    # Ceil -> Lower Bound -> >=x

    def Find_Ceil(self,nums,x):
        low, high = 0, len(nums)-1
        ans = - 1

        while low <= high:
            mid = ( low + high )//2

            if nums[mid] >= x:
                ans = nums[mid]
                high = mid -1 
                # To Left 

            else:
                # To right 
                low = mid + 1
        return ans 
    
    def Get_Floor_and_Ceil(self,arr,x):
        floor = self.Find_Floor(arr,x)
        ceil = self.Find_Ceil(arr,x)
        return floor, ceil
    

# Time Complexity:O(logN), where N = size of the given array. We are using the Binary Search algorithm

# Space Complexity: O(1). No extra space used   

#----------------------------------------------

arr = [3, 4, 4, 7, 8, 10]
x= 5
finder = FloorCeilFinder()

f, c = finder.Get_Floor_and_Ceil(arr,x)
print(f"the Floor and Ceil of Number [{x}] are: {f} {c}")
