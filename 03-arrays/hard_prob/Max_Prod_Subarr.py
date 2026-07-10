# Maximum Product Subarray 

# Brute Force 

def Max_Prod_Subarr(arr):

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

nums = [ 2, 3, -3, 4, 5 ]
print (Max_Prod_Subarr(nums))