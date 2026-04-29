
# Linear Search

def LinearSearch (arr, target):
    for i in range (len(arr)):
        if arr[i] == target:
                return i
    return -1    

arr=[1,2,5,7,9,23]

# Time Complexity: O(N), where N is the number of elements in the array. This is because we traverse the entire array to find the element.

# Space Complexity: O(1), as we are using a constant
print(LinearSearch(arr,91))