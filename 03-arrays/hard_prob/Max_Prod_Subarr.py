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


nums = [ 2, 3, -3, 4, 5 ]
print (Max_Prod_Subarr_Brute(nums))
print (Max_Prod_Subarr_Better(nums))