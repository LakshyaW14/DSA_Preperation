
def Bubble_Sort(arr):
    n =len(arr)

    #for traversing all array elements 
    for i in range (n):
        # optimized swapped flag, for early exit if arr is sorted 
        swapped= False
        # last element are already in place 
        for j in range (0,n-i-1):

            # traverse the array from 0 to n-i-1
            # swap if the element found is greater 
            #than the next element 
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1], arr[j]
                swapped =True
        if not swapped:
            break


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    Bubble_Sort(arr)


print("sorted array by ( Bubble sort)")

for i in range (len(arr)) :
    print(arr[i], end=" ")