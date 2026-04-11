# Quick Sort

def partition(arr, low, high):
    pivot = arr[high]   # choose last element as pivot 
    i = low -1          # pointer for smallest element 

    for j in range (low, high):
        if arr[j] < pivot :
            i+=1
            arr[i],arr[j] = arr[j], arr[i]
    
    # place pivot at correct position 
    arr[i+1], arr[high] = arr[high], arr[i +1]
    return i + 1


def Quick_Sort (arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        Quick_Sort(arr, low, pi-1)  #left
        Quick_Sort(arr, pi+1, high) #Right

arr=[5,3,2,4,12,17,34,29,32,1]

#----------------------------------------------------------

# Optimized Quick sort 

import random as rd

# Hybrid with insertion sort for smaller subarrays
def insertion_sort (arr, low, high):
    for i in range (low +1, high +1):
        key = arr[i]
        j=i-1
        while j >= low and arr[j] > key:      #shifts elements greater than key 
            arr[j+1] = arr[j]
            j-=1
        # insert key at correct position 
        arr[j+1] = key

# Partion with random pivot, TC avg stays O(nlogn)
def partition_rd_pivot(arr, low, high ):
    pivot_index = rd.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i =low - 1

    for j in range(low, high):
        if arr[j] < pivot :
            i+=1
            arr[i], arr[j]= arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
# prevents sorted / reverse sorted worst case 

def QS_optimized ( arr, low, high ):
    while low< high:
        # insertion sort for small arrays 

        if high - low < 10 :
            insertion_sort(arr, low, high )
            break
        pi = partition_rd_pivot(arr, low, high)


        # recurse on smaller partition ( tail recursion optimization )
        # instead of calling both side recursively 

        if pi - low < high - pi:
            QS_optimized(arr, low, pi -1)
            low = pi +1
        else:
            QS_optimized(arr, pi+1, high)
            high = pi-1

# 3 way optimization for handling duplicates 


QS_optimized(arr, 0,len(arr)-1)
print(arr)

        

