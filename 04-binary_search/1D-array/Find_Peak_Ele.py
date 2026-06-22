# Find Peak element 

# Brute Force -> Linear Search 

# Hypothetically the -1 and n idx of arr is set to - infinity

def Peak_Ele(arr):
    n =len(arr)
    for i in range(n):
        if ( i == 0 or arr[i] > arr[i+1]) and ( i == n-1 or arr[i] > arr[i-1]):
            return i 
        
# Tc O(n)
# SC O(1)

#-----------------------------------------------

# Optimal Solution 
# Binary search 

def Peak_Ele_Optimal (arr):
    n = len(arr)
   
    # manual Edge Cases
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n-1] > arr[n-2]:
        return n-1
    
    # 0 and n-1 idx already checked 
    low = 1
    high = n-2
    while ( low <= high ):
        mid = ( low + high )//2

        # The mid is the peak Element
        if arr[mid-1] < arr[mid] > arr[mid + 1]: 
            return mid
        
        # mid is in increasing curve  low -> mid -> peak always in right 
        elif arr[mid-1] < arr[mid]:
            low = mid + 1
        
        # Mid is in Decreasing Curve  peak -> mid -> high peak always in left 
        elif arr[mid + 1] < arr[mid]:
            high = mid - 1

        # MId is in between of two greater Elements ( or between two peaks )
        # peak -> mid <- peak , either move to any direction 
        # Works for both multiple and single peak 
        else:
            low = mid + 1 
        

    return -1 
# TC O(logn)
# SC O(1)
# --------------------------------------------


arr = [ 1,2,3,4,5,6,7,8,5,1]
arr2 = [ 1]
arr3 = [ 1,5,1,2,1]

print(Peak_Ele(arr3))
print(Peak_Ele_Optimal(arr3))

