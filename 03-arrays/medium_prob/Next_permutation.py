
def Stock (nums):
    profit = 0
    mini = float('inf')
    for i in range (len(nums)): # Selling days 

        cost = nums[i] - mini

        if nums[i] < mini:
            mini = nums[i]

        else:
            profit = max(cost, profit)
        
    return profit




num= [7,9, 1, 5, 4,10,13]
nums=[7,1,5,3,6,4]
print(Stock(nums) )