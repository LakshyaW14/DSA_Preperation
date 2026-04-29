# find the largest element from the array 
# Brute Force Approach

def sortArr(arr):
    arr.sort()
    return arr[-1]

# TC O(nlogn), where n is the size of the array, as we are sorting the array.
# SC O(1), as we are using a constant.

#-------------------------------------------------------

# optimal Approach 

def LargestElement(arr):
    n =len(arr)
    # initialize max with the first element of the array 
    max = arr[0]

    # iterate through the arr to find the maximum element
    for i in range (1, n):

        # if the current element is greater than max , update max
        if arr[i] > max:
            max = arr[i]

    return max

# TC O(n) Where N is the size of the array 
# SC O(1), as we are constant


arr=[2,4,7,199,12]
print(LargestElement(arr))

 
        