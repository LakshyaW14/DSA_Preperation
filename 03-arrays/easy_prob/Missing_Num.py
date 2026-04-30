# find the Missing number 
# Brute force Approach
def Find_Missing_Num (nums):
    n = len(nums )

    # Iterate from 1 to n and check if the current element is present or not 
    for i in range (1, n +1):
        found = False
        for j in range (n-1) :
            if nums[j] == i :
                found = True
                break 
        if not found :
            return i 

# Time Complexity O(N ^2), we using two nested loops
# Space Complexity O(1)


# ----------------------------------------------
# Better Approach 
""" Hashing"""

def Missing_Num (nums):
    # Length of given array + 1
    n = len(nums) + 1

    # hash aarr
    hash_arr = [0] * (n+1)

    # Store the frequencies of element 
    for i in range (n-1):
        hash_arr[nums[i]] +=1
    
    # Search for missing number in hash array 
    for i in range (1, n+1):
        if hash_arr[i] == 0:
            return i

# Time Complexity O(N) + O(N) -> O(2N)
# Space Complexity O(N)


#------------------------------------------------
# Optimal Approach 
# 01 - using Sum of n natural numbers formula 

def Missing_Optimal_Sum (nums):
    n= len(nums) +1
    # Sum of n natural numbers 
    Sum = (n *(n+1)) //2
    
    # Variable to store the added sum of n numbers
    add = 0
    # adding element of array
    for num in nums:
        add += num

    return ( Sum - add )

# Time Complexity O(N)
# Space O(1)


# Catch - > XOR is better than sum approach 
# in sum approach if the input is like 10 ^5 the sum becomes 10^10, eventually we need a bigger datastructure 
# XOR of all numbers is not big at all 


#----------------------------------------
# 02 - > using XOR Operator 

# 2^2 = 0
# 0^0 = 0
# 0^2 = 2

def Missing_optimal_XOR (nums):
    xor1, xor2=0,0
    n =len(nums) +1
    # for i in range (1, n+1 ):
    #     xor1 ^= i
    #O(n^2) need to solve in one iteration 

    for j in range ( n-1):
        xor1 ^= (j+1)
        xor2 ^= nums[j]
    xor1 ^= n
    
    return xor1 ^ xor2

nums = [2,1,5,4]
print(Missing_optimal_XOR (nums))