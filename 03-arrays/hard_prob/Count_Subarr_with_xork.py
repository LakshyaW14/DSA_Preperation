# Count Subarray with xor k

# Brute 

def Count_Subarr_Xor_Sum_Brute (arr, k):
    count = 0
    # First loop 
    for i in range (len(arr)):
        # Second  loop 
        for j in range (i, len(arr)):
            xr = 0
            # Third loop to traverse the subarray ( i -> j)
            for k in range (i, j + 1):
                xr ^= arr[k]
                # Condition 
                if xr == k:
                    count += 1
    return count 

# TC O(n^3) nearly 
# SC O(1)

#------------------------------------

# better Solution  

def Count_Subarr_Xor_Sum_Better (arr, k):
    # Variable to store the count 
    count = 0
    # first loop 
    for i in range (len(arr)):
        # Xor of arr elements 
        xr = 0
        # Second loop 
        for j in range(i,len(arr)):
            # 
            xr ^= arr[j]
            # if xor of ele equals to k, increment 
            if xr == k:
                count += 1
    # 
    return count 

# TC O( n^2) two nested Loops 
# SC O(1)
#--------------------------------


nums = [4, 2, 2,6 ,4 ]

print(Count_Subarr_Xor_Sum_Brute(nums, k=6))
print(Count_Subarr_Xor_Sum_Better(nums, k=6))