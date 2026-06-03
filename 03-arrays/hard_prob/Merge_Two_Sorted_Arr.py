# Brute Force 

def merge_Sorted_Arr(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i,j = 0, 0
    ans =[]
    index = 0
    while ( i <= n) and ( j <= m):
        if ( arr1[i] <= arr2[j]):
            ans[index] = arr1[i]
            index += 1
            i += 1
        
        else:
            ans[index] = arr2[j]
            index += 1
            j += 1
    
    while ( i <= n):
        ans[index] = arr1[i]
        index += 1
        i += 1

    while ( j <= m ):
        ans[index] = arr2[j]
        index += 1
        j += 1

    for  i in range ( n + m):
        if i < n :
            arr1[i] = ans[i]
        else:
            arr2[i-n] = ans[i]

    return arr1, arr2

num1 = [1,3,5,7]
num2 = [0,2,6,8,9]
print(merge_Sorted_Arr(num1, num2))