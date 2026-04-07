

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

arr=[5,3,2,4,1]
Quick_Sort(arr, 0,len(arr)-1)
print(arr)

#----------------------------------------------------------

# 
