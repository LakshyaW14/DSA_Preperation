
# Count Maximum Consecutive One's in the array

def max_consecutive_one(nums):
    # Initialize two variable 
    # to store the current streak of 1
    count = 0

    # stores the max streak of 1 so far 
    max_streak = 0
    for num in nums :
        if num == 1 :
            count +=1
            max_streak = max(max_streak, count)
        else: 
            count= 0
    return max_streak

# Time Complexity: O(N), since we scan the array once.

# Space Complexity: O(1), as only constant extra variables are used.

nums=[1,1,0,1,1,1,0,1,1,1,1]
print(max_consecutive_one(nums))