# Merge Overlapping Subinterval 

# Brute Force 

def Merge_Overlapping_Subinterval(arr):
    # arr to store the result
    ans = []
    
    # intialize the start and end variable -> ( start, end )

    # iterating over the arr
    for i in range (len(arr)):
        start = arr[i][0]
        end = arr[i][1]

        # second loop 
        for j in range ( i+1, len(arr)):

            # overlapping condition check 
            if arr[j][0] <= end:
                # Update the end with, max possible element 
                end = max (end, arr[j][1])

            else:
                break 
        ans.append((start, end))
         
    return ans
    # intialize the start and end variable -> ( start, end )
    



intervals=[[1,3],[2,6],[8,10],[15,18]]
print(Merge_Overlapping_Subinterval(intervals))