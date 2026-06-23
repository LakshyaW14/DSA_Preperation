# Find Single Element in Sorted Array 

# Brute Force 

def Find_single_Ele_Brute (arr):
    n = len(arr)
    # Edge Cases 
    if n == 1:
        return arr[0]
    
    for i in range (n):
        if (arr[i] != arr[i-1] )and( arr[i] != arr[i+1]):
            return arr[i]
        if i == 0:
            if arr[0] != arr[1]:
                return arr[0]
        if i == n -1:
            if arr[n-1] != arr[n-2]:
                return arr[n-1]
            
    return -1

# TC O(n)
# SC O(1)

#--------------------------

# Optimal Sol 

def Find_Single_Ele (arr):
    n = len(arr)

    # Edge Cases 
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    # Trimed Search Space 
    low = 1 
    high = n-2
    while ( low <= high):
        mid = ( low + high )//2

        if ( arr[mid] != arr[mid-1] ) and ( arr[mid] != arr[mid +1]):
            return arr[mid]

        #  Element is in Right Half And Left Half should eliminated 
        # ( Even, Odd ) indexing of pairs
        elif  ( mid % 2 != 0 and arr[mid-1] == arr[mid]) or ( mid %2 == 0 and arr[mid+1] == arr[mid]):
            low = mid + 1
        
        # Element is in left Half, eliminate the right 
        # ( Odd, Even ) Pair
        else:
            high = mid - 1
    
    return -1


# TC O(logn)
# SC O(1)

#----------------------------------------

a = [ 1,1,2,2,3,3,4,5,5,6,6]
b= [1,2,2]
c = [ 1,1,2]
d = [1]

print(Find_Single_Ele(a))
print(Find_Single_Ele(d))