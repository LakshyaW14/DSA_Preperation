# Number of Subarrays with Given Sum 
# Brute Force 

def Count_SubArr (nums,target):
    # Initialize the count of subarray occurrence 
    count = 0

    # Traverse all start indices
    for i in range(len(nums)):
        # Traverse from start to end
        for j in range(i, len(nums)):
            s = 0
            for k in range (i,j+1):
                s += nums[k]
            if s == target:
                count +=1
    return count

# Time Complexity: O(N3), where N = size of the array.We are using three nested loops here. Though all are not running for exactly N times, the time complexity will be approximately O(N3).

# Space Complexity: O(1) as we are not using any extra space.

#---------------------------------------------------
# Better Approach

def Count_SubArr_better(nums,target):
    count = 0
    for i in range(len(nums)):
        s =0
        for j in range (i, len(nums)):
            s += nums[j]
            if s == target :
                count += 1
    return count 

#Time Complexity: O(n²),We use two nested loops to check all subarrays, where n is the size of the array.

# Space Complexity: O(1),Only a few extra variables are used, so constant extra space regardless of input size.

#------------------------------------------
#   Optimal Approach 
# using PREFIX SUM 

def Count_SubArr_Optimal (nums, target):

    #  To Store PreFix_sum Count 
    mp = {}

    count = 0
    pre_sum =0

    # Base Case : Prefix sum 0 has Occured once
    mp[0] = 1

    # traversing 
    for i in range (len(nums)):
        # Adding current element 
        pre_sum += nums[i]
        
        # Value to be excluded
        rem = pre_sum - target

        # if  rem -> prefix sum has been seen before 
        # add it to the result
        if rem in mp:
            count += mp[rem]

        # Update the Frequency of current prefix sum 
        
        mp[pre_sum] = mp.get(pre_sum,0) + 1
    
        
    return count 

# Time Complexity: O(n) We traverse the array once, where n is the size of the array. Each prefix sum operation and hashmap lookup is O(1) on average. if ordered mp is used O(n*logn)

# Space Complexity: O(n) In the worst case, all prefix sums are distinct and stored in the hashmap, so space grows linearly with input size.

#---------------------------------------------------------

nums=[3,1,2,4]
k = 6
print(Count_SubArr(nums,k))
print(Count_SubArr_better(nums,k))
print(Count_SubArr_Optimal(nums,k))

