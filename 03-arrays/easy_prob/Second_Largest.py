# Find Second Smallest and Second Largest Element in an array
# Brute Force Approach

def find_element(arr):
    n=len(arr)
    if n== 0 or n ==1:
        print(-1,-1)
        return 
    
    arr.sort()

    # small = arr[1]

    # large = arr[n-2]
    # print(" Second Smallest element is ", small)
    # print(" Second Largest element is ", large)

    # if duplicates are present 
    largest = arr[n-1]          #TC O(nlogn) + (n)
    Secondlargest = 0
    for i in range (n-2, -1, -1):
        if arr[i] != largest :
            Secondlargest = arr[i]
    return Secondlargest
        

# TC O(nlogn)
# SC O(1)


#----------------------------------------------------

# Better Approach 
def Get_Element(arr):

    # for largest element 
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num

    # for second_largest element 
    second_largest = 0
    for num in arr:
        if num != largest and num < largest:
            second_largest = num
    
    return [ largest, second_largest]

# TC O(2N) two iteration of n 


#-------------------------------------------------------
# optimal approach 
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
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num 

        # largest 
        # intuition -> 
        # large , second_large = int_min 
        # if num[i] > large 
        #second_ large = large and large = num[i]
        # and repeat
        if num > largest:
            second_largest = largest
            largest = num 
        elif num > second_largest and num != largest :
            second_largest = num 
    
    print(f"largest : {large} and second largest : {second_large} numbers ")
    print(f"smallest: {small} and second smallest : {second_small} numbers ")
    

    #O(n) → single traversal
    
    #O(1) → no extra space

# ---------------------------------------------------------------


# Brute -> Better -> Optimal 
# nlogn -> 2n -> n
arr=[2,9,9,9,9,9,9]
print(Get_Element(arr))
            






