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

#optimal Approach 


def Stock_Optimal(nums):
    # Intialize minimum number 
    min_price = float('inf')

    # Intialize max profit 
    max_profit = 0

    for num in nums:
        cost = num - min_price
        # if current price is less than min price, update min price
        if num < min_price:
            min_price = num

        # calculate profit and update max_profit if it's greater 
        else:
            max_profit = max(max_profit, cost)

    #return 
    return max_profit

# Time Complexity: O(n),This is because we are iterating through the array of prices exactly once. There are no nested loops or recursive calls.

# Space Complexity: O(1),Only two variables are used to store the minimum price and maximum profit, regardless of the input size

#-------------------------------------------------------


nums=[7,1,5,3,6,4]
print(Stock_Optimal(nums))
print(Stock_Buy_Sell(nums))