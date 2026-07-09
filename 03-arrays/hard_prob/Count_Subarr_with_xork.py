# Count Subarray with xor k

# better Solution  

def Count_Subarr_Xor_Sum(arr, k):
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

print(Count_Subarr_Xor_Sum(nums, k=6))