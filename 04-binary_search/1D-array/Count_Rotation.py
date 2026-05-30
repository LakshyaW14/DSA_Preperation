

def Count_Rotation (nums):
    low, high = 0, len(nums)-1
    ans_idx = -1
    mini = float('inf')

    while ( low <= high):
        mid = ( low + high)//2

        if nums[low] <= nums[high]:
            if nums[low] < mini:
                mini = nums[low]
                ans_idx = low
            break

        # Left Half 
        if ( nums[low] <= nums[mid]):
            if nums[low] < mini:
                mini = nums[low]
                ans_idx = low
        # Right half 
        else:
            if nums[mid] < mini:
                mini = nums[mid]
                ans_idx = mid

    return ans_idx

arr= [4,5,6,7,0,1,2,3]
print(Count_Rotation(arr))