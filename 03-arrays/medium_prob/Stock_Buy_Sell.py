# Stock Buy and Sell 
# Brute Force Approach

def Stock_Buy_Sell(nums):
    # Intialize max_profit to 0
    max_profit = 0

    # Loop through each DAY as potential BUY day
    for i in range(len(nums)):

        #Loop through future days as potential to SELL day
        for j in range(i+1, len(nums)):

            #calculate profit
            profit = nums[j] - nums[i]
            # Update max profit if higher
            max_profit=max(max_profit, profit)
    # return max profit
    return max_profit


# Time Complexity: O(n²) Because for each element, we are checking every future element nested loops.

# Space Complexity: O(1) No extra space used, only variables for storing max profit.

#---------------------------------------------------
nums=[7,1,5,3,6,4]
print(Stock_Buy_Sell(nums))