# Maximum Product Subarray 

# Brute Force 

def Max_Prod_Subarr_Brute(arr):

    # Maximum product so far 
    maxi = float('-inf')

    # Loop for first index of subarray 
    for i in range (len(arr)):
        # loop for last index of subarray 
        for j in range (i , len(arr)):
            # To store the Product 
            prod = 1
            
            # traverse the subarr
            for k in range (i, j+1):
                prod *= arr[k]

                maxi = max(maxi , prod)


    return maxi 
# Tc O(n^3) nearly 
# SC O(1)
# -------------------------------------

# Better Solution 

def Max_Prod_Subarr_Better(arr):
    maxi = float('-inf')

    # First loop 
    for i in range (len(arr)):
        prod = 1
        for j in range ( i, len(arr)):
            prod *= arr[j]

            maxi = max(maxi, prod)
    return maxi 

# TC O(N^2)
# SC O(1)

# --------------------------------------

# Optimal Sol 
# 1st approach -> best intuitive, clear Observation 
# 2nd approach -> Kadane's algo 

def Max_Prod_Subarr_Optimal ( arr):
    n = len(arr)

    maxi = float('-inf')
    # Intialize two pointers 
    prefix , suffix = 1, 1

    for i in range (n) :

        # if zero occurs
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1 

        # Add Elements 
        prefix *= arr[i]
        suffix *= arr[ n-i-1] 

        # maxi result 
        maxi = max( maxi, max( prefix, suffix))

    return maxi 

# TC O(n) Traversing only once
# Sc O(1)


nums = [ 2, 3, -3, 4, 5 ]
nums2 = [ 1, 4, 5, 0, 2, 5, 0] # with zero 
nums3 = [-3, 2, -3 , -3 ,1]    # Odd number of negatives values
print (Max_Prod_Subarr_Brute(nums))
print (Max_Prod_Subarr_Better(nums))
print (Max_Prod_Subarr_Optimal (nums))

print (Max_Prod_Subarr_Optimal (nums2))
print (Max_Prod_Subarr_Optimal (nums3))
