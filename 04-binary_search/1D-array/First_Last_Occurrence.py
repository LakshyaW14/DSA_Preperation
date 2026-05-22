# First and last occurrence in sorted array 

# Brute Force -> Linear Search 

def Get_Occurence(nums,x):
    #
    first, last = -1, -1
    for i in range(len(nums)):
        if nums[i] == x:
            if first == -1:
                first = i 
            else:
                last= i

    return first, last 

# TC O(n)
# SC O(1)

#--------------------------------------

nums = [1,2,3,4,5,5,5,5,5,5,6,7,8]
print(Get_Occurence(nums, 5))