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
    return True if count <= 1 else False

arr=[2,1,3,4]
print(Is_Arr_Sorted(arr))