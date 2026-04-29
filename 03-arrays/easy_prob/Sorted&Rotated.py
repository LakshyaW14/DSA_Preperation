# check if the array is Sorted and Rotated

def Is_Arr_Sorted(arr):
    if 0 < len(arr) < 1:
        return True
    count=0
    if arr[len(arr)-1] > arr[0]:
        count+=1
    for i in range ( 1, len(arr)-1):
        if arr[i] > arr[i+1]:
            count+=1

        # optimization 
        #if arr[i] > arr[(i+1) %n]
    return count <= 1 

arr=[3,4,5,1,2]
print(Is_Arr_Sorted(arr))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)