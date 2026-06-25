# Capacity to ship Packages within D days 

# Brute Force

def Days_Reg(arr, capacity):
    Day = 1
    Load = 0
    for wt in range ( len(arr)):
        # If Day 1 load is Greater than cap 
        if Load + arr[wt] > capacity:
            # Move to next day 
            Day +=1
            # Record the last weight
            Load = arr[wt]
        
        # if within the req cap, add it 
        else:
            
            Load += arr[wt]

    return Day

# Ans Range max(Arr) -> sum(arr)
def ship_Pakages(arr, Days):
    # Loop for different Capacities 
    low = max(arr)
    high = sum(arr)
    for cap in range ( low , high+1):
        if Days_Reg(arr, cap) <= Days:
            return cap
        
    return -1 

# TC O(n) x O(sum(Arr) - max(arr) +1)
# sc O(1)

# ----------------------------

weighs1 = [ 1,2,3,4,5,6,7,8,9,10]
weights2 =  [5, 4, 5, 2, 3, 4, 5, 6]
d = 5

print(ship_Pakages(weighs1, d))