#clean Python implementation of Merge Sort, \
# with proper intuition embedded 


def Merge (arr, left, mid, right):

    # 1- creatte temp array
    n1 = mid - left + 1
    n2 = right - mid 

    L = [0] * n1
    R = [0] * n2

    # 2- copy data into temp
    for i in range (n1):
        L[i] = arr[ left + i]
    for j in range (n2):
        R[j] = arr[mid + 1 + j]

    # 3- Merge the temp arr back into arr

    i = 0   # pointer for L
    j = 0   # pointer for R
    k =left # pointer for main array

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1

    # 4- Copy Remaining elements ( if any )
    while i < n1:
        arr[k] = L[i]
        i+=1
        k+=1

    while j < n2 :
        arr[k] = R[j]
        j+=1
        k+=1
    

def Merge_Sort(arr, left, right ):
    if left < right :
        mid =( left + right) //2

        # Divide 
        Merge_Sort(arr, left, mid)
        Merge_Sort(arr, mid +1, right)

        # Conquer (Merge)
        Merge(arr, left , mid, right)

arr = [38, 27, 43, 3, 9, 82, 10]
Merge_Sort(arr, 0, len(arr) - 1)
print(arr)

#------------------------------------------------------------------------------------------------

# Optimized code 
def merge_sort(arr):

    # Base case 
    if len(arr) <=1:
        return arr
    
    # Divide 
    mid = len(arr) //2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge 
    return merge (left, right)



def merge(left, right):
    result = []
    i = j = 0

    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result
   


arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)