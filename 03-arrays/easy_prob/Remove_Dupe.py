

# Remove Duplicates in-place from Sorted Array

# optimal approach
# functions to remove the duplicates from sorted array in place 

# two pointers approach

def remove_duplicate(arr):
    # list is empty , return 0
    if not arr:
        return 0
    
    # pointer for last unique element
    i = 0
    
    # traverse the list 
    for j in range (1, len(arr)):
        # if current element is different from the last unique element 
        if arr[i] != arr[j]:
            # move the pointer forward 
            i+=1
            # place the unique element in next position 
            arr[i] = arr[j]

    # i is the last index of unique element , coount = i+1
    return i+1

# Time Complexity: O(N), We traverse the entire original array only once.
# Space Complexity: O(1), constant additional space is used to check unique elements.


#----------------------------------------------------------------
# BRute force approach

def remove_duplicates_set (arr):
    # set to store the unique elements 
    k = set()

    #pointer for unique element 
    i =0

    for num in arr:
        # if num is not in k, it's unique
        if num not in k:
            # add num to set 
            k.add(num)

            # overwrite arr[i] with this num
            arr[i] =num

            # move the i forward
            i +=1
    return i

# Time Complexity: O(N), We traverse the entire array and insert elements into set.
# Space Complexity: O(N), additional space used to store elements in set.

#----------------------------------------------------------------

arr = [1,1,2,2,3,3,3,4,4,4,4]

k=remove_duplicate(arr)

print("Unique count :", k)
print(" array after removing the duplicates : ", arr[0:k])

#-------------------------------------------------------------------
