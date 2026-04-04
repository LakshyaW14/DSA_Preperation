def Insertion_Sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i] # the element to be placed correctly 
        j = i - 1

        # shift elements greater than key
        # move elements of arr [0...i-1], that are greater than key, \
        # to one position ahead of their current position 
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # insert key at correct position
        arr[j + 1] = key

arr=[5,3,4,2,1]

Insertion_Sort(arr)
for val in arr:
    print(val, end=" ")


