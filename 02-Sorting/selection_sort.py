
def Selection_Sort(arr):
    n=len(arr)

    for i in range (n-1):

        #assume the current position holds the min element
        min_idx = i

        # iterate through unsorted portion to find the actual min element
        for j in range (i + 1 ,n):
            if arr[j] < arr[min_idx]:

                #update min_num if a smaller element is found 
                min_idx = j
        #move min element to its correct position 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def print_arr(arr):
    for val in arr:
        print(val, end=" ")

if __name__ == "__main__":
    arr=[64,37,84,23,20,10]
    Selection_Sort(arr)
    print("sorted  array:", end=" ")
    print_arr(arr)
 
    
