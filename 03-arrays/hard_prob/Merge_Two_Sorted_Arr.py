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

# Better without extra space 

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
# Three pointer 
# arr1 = [ 1, 3, 5, 0, 0, 0] where placeholder values is used 
# arr2 = [ 2, 4, 6 ] 

def Merge_sorted_arr_Optimal2(arr1, arr2):
    m = len(arr2)   # 3
    n= len(arr1) - m    # 4

    # n = length of valid elements only 
    # Intialize three pointers 
    i = n -1
    j = m - 1
    k =  m + n -1
    
    # merge From back to avoid overwriting 
    while ( i>= 0 ) and  ( j >= 0):

        # if a1 ele is greater than a2 ele, place at a1[k] place 
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1

        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1

    # if element remain in arr2 
    while ( j >= 0):
        arr1[k] = arr2[j]
        j -= 1
        k -= 1
    # No need to copy the leftover ele of arr1 , already sorted

    return arr1


#  TC O(n + m) we traverse both the arr once 
# SC O(1)

#------------------------------------

# Optimal sol 

"""Gap Method from Shell Sort """
# Intuition -> compare and swap until right within the Boundaries 
# if not Restart -> Reduce Gap 
# Gap // 2


# helper Function to swap elements 

def swapifgreater(arr1, arr2, idx1, idx2):
    if arr1[idx1] > arr2[idx2]:
        # Swap 
        arr1[idx1], arr2[idx2] = arr2[idx2],arr1[idx1]  


def Merge_Sorted_Arr_Optimal(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    length = n + m

    gap = (length//2) + (length % 2)

    while ( gap > 0):
        left = 0 
        right = left + gap 

        while ( right < length):

            # left pointer in arr1 and right  pointer in Arr2
            if ( left < n) and ( right >= n):
                swapifgreater( arr1 , arr2, left, right-n)

            # both pointer in arr2
            elif ( left >= n):
                swapifgreater( arr2, arr2, left-n , right-n)

            # Both pointer in arr1 
            else:   
                swapifgreater ( arr1, arr1, left , right)
            
            left += 1 
            right += 1

        # if gap equals to 1 
        if gap == 1:
            break 
        gap = ( gap // 2) + ( gap % 2)

    return arr1, arr2

# Time Comp -> Outer Loop O(logn) Inner Loop O(N) N = n +m
# O(n+m)log(n+m)

# Space complexity O(1)

# ---------------------------------------

num1 = [1,3,5,7]
num2 = [0,2,6,8,9]

arr1 = [-5, -2, 4, 5, 0, 0, 0] # For this Input the swap+sort algo fails here Three Pointer Works 
arr2 = [-3, 1, 8]

# print(merge_Sorted_Arr(num1, num2))
# print(Merge_Sorted_Arr_Better(num1, num2))
# print(Merge_Sorted_Arr_Optimal (num1, num2))


# print(merge_Sorted_Arr(arr1, arr2))
# print(Merge_Sorted_Arr_Better(arr1, arr2))
# print(Merge_Sorted_Arr_Optimal (arr1, arr2))

print(Merge_sorted_arr_Optimal2(arr1, arr2))