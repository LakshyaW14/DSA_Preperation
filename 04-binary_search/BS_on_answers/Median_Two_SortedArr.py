# Median of two Sorted Array 

# Brute Force 

def Median_Two_Sorted_Arr(arr1, arr2):
    n1 = len(arr1)
    n2 = len( arr2)
    N = n1 + n2
    arr3 = []
    i,j = 0, 0
    while ( i < n1) and ( j < n2):
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i += 1

        else:
            arr3.append(arr2[j])
            j += 1
    
    # if element are left in arr1
    while ( i< n1):
        arr3.append(arr1[i])
        i += 1
    
    # If element are left in arr2 
    while ( j < n2):
        arr3.append(arr2[j])
        j += 1
    
    print(arr3)
    # Odd Length 
    if N % 2 == 1:
        return arr3[N//2]
    else:
        return arr3[(N//2)-1], arr3[N//2]

#TC O(N)
# SC O(n)

#---------------------------------------------------

a = [ 1,3,4,7,10,12]
b = [ 2,3,6,15]
print(Median_Two_Sorted_Arr(a,b))