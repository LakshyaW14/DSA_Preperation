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

# Optimal Sol 1 without extra space 

"""Two Pointer"""
# The Two array are already sorted 

# Intuition -> Compare and Swap the places 
# the arr1 should have smalller Ele
# arr2 should have larger ele

def Merge_Sorted_Arr_Better(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    # [ 1 , 3 , 5 , 7]left    right[ 0 , 2 , 6 , 8 , 9]m
    left = n -1 
    right = 0

    while ( left >= 0) and ( right < m):

        # if the rigthmost element of arr1 is greater
        # than leftmost ele of arr2 
        if arr1[left] > arr2[right]:
            # swap 
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1 
            right += 1
        
        #if arr1[left] < arr2[right]
        else:
            break 
        # rest of the ele already min 
    
    # sort the Arr1 and arr2
    arr1.sort() , arr2.sort()
    return arr1 , arr2

# TC O(min(n,m)) + n logn + mlogm
# SC O( 1)

# ------------------------------------

num1 = [1,3,5,7]
num2 = [0,2,6,8,9]
print(merge_Sorted_Arr(num1, num2))
print(Merge_Sorted_Arr_Better(num1, num2))