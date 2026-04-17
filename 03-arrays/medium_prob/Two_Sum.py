# Two Sum : Check if a pair with given sum exists in Array

# Brute Forch Approach( Two pointer )

def Two_sum (arr, target):
    n =len(arr)

    # Outer loop picks one element at a time 
    for i in range(n):

        # Inner loop searches for another element that compliments arr[i]
        for j in range(i,n):

            # if sum equals target, return " Yes "
            if arr[i] + arr[j] == target:
                return "Yes"
                # for returning indices 2nd variant
                # return [ i, j ]

    # no pair found, Return "No"
    return "No"

# Time Complexity: O(N²) because we use two nested loops to check every possible pair of elements in the array, \
# where N is the size of the array.

#Space Complexity: O(1) as we use a constant amount of extra space regardless of input size.

#---------------------------------------------------

# Better approach ( using  Hashmap )

def Two_sum_Hashmap(arr, target):

    # Dict to store the element -> index
    mp = {}

    # Iterate over all elements
    for i , num in enumerate(arr):
        compliment = target - num 
        # check if compliment exist in dict
        if compliment in mp:
            # Pair found 
            # return " Yes "
            # For 2nd variant 
            return  [ mp[compliment] , i]
        
        # Store current element and its index
        mp [num] = i
    # No pair found 
    return " No"

# Time Complexity: O(N) because we traverse the array only once, and each lookup or insertion in the hash map takes O(1) on average, where N is the size of the array.

# Space Complexity: O(N) since in the worst case we may store all elements of the array in the hash map.


#----------------------------------------------

# Optimal Approach

def Two_Sum_Optimal(arr,target):
    
    # create a list of tuples ( value, original index)
    # this preserves the index, unlike sort() doesn't
    nums_with_index = [ (num, idx) for idx, num in enumerate(arr)]

    # sort list based on the values ( to apply two pointer technique)
    nums_with_index.sort( key=lambda x : x[0])

    # intializes two pointers 
    left , right = 0, len(arr)-1

    # continue unitl pointers cross
    while left < right :
        Sum = nums_with_index[left][0] + nums_with_index[right] [0]

        if Sum == target:
            # return "Yes"
            return nums_with_index[left] [1], nums_with_index[right] [1]
        
        elif Sum < target:
            left +=1
        else:
            right -=1
    return (-1,-1)
        

# Time Complexity: O(N log N) due to sorting the array initially, \
# where N is the number of elements. The two-pointer traversal runs in O(N).

# Space Complexity: O(N) because we store the array elements along with their original indices in a separate list or vector for sorting, \
# maintaining original positions.

arr1 =[2,6,5,8,13]
target=11

# print(Two_Sum_Optimal(arr,target))

