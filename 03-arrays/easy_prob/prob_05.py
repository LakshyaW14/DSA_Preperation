# Find Second Smallest and Second Largest Element in an array
# Brute Force Approach

def find_element(arr):
    n=len(arr)
    if n== 0 or n ==1:
        print(-1,-1)
        return 
    
    arr.sort()

    small = arr[1]

    large = arr[n-2]
    print(" Second Smallest element is ", small)
    print(" Second Largest element is ", large)

# TC O(nlogn)
# SC O(1)

#-------------------------------------------------------
# Better approach 
def getElements(arr):
    n =len(arr)

    # edge case 
    if n ==0 or n ==1 :
        print (-1, -1)
        return 
    # intialize variables to track the smallest, second_smallest, largest, second_largest
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')

    for num in arr:
        # Smallest 

        # or small = min( small , num) update the smallest element
        if num < small:
            second_small = small
            small = num
        elif num < second_small and num != small:
            second_small = num 

        # largest 
        # intuition -> 
        # large , second_large = int_min 
        # if num[i] > large 
        #second_ large = large and large = num[i]
        # and repeat
        if num > large:
            second_large = large
            large = num 
        elif num > second_large and num != large :
            second_large = num 
    
    print(f"largest : {large} and second largest : {second_large} numbers ")
    print(f"smallest: {small} and second smallest : {second_small} numbers ")
    

    #O(n) → single traversal
    
    #O(1) → no extra space

# ---------------------------------------------------------------


arr=[2,5,1,6,7,9]
print(getElements(arr))
            






