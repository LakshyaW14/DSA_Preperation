# Merge Two sorted arrays without extra space 

# Brute Force with extra space 


def merge_Sorted_Arr(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i,j = 0, 0
    temp =[]
    # merge arr1 and arr2 to form temp in sorted order 
    # filling the the temp with number of arr1 and arr2 in sorted order  
    # Runs for min(n,m)

    # arr1 0 to n-1
    # arr2 0 to m-1

    while ( i < n) and ( j < m):
        if ( arr1[i] <= arr2[j]):
            temp.append(arr1[i])
            i += 1
        
        else:
            temp.append(arr2[j])
            j += 1

    # The left out element in arr1
    while ( i < n):
        temp.append(arr1[i])
        i += 1

    # the left out Element in arr2
    while ( j < m ):
        temp.append(arr2[j])
        j += 1

    # Copy Back 
    # Filling back in arr1 and arr2 in sorted order 
    for  i in range ( n + m):

        if i < n :
            arr1[i] = temp[i]
        else:
            arr2[i-n] = temp[i]
    
    return arr1, arr2

# TC merge + copyback O(n+m) + O(n +m) ->> O(n+m)
# SC temp array O(n+m)

# ----------------------------------------------

num1 = [1,3,5,7]
num2 = [0,2,6,8,9]
print(merge_Sorted_Arr(num1, num2))