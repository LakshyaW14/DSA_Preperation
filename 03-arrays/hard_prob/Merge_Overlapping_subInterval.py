# Merge Overlapping Subinterval 

# Brute Force 

def Merge_Overlapping_Subinterval(arr):
    # arr to store the result
    arr.sort()
    ans = []
    
    # intialize the start and end variable -> ( start, end )

    # iterating over the arr
    for i in range (len(arr)):  # 0 -> n

        start = arr[i][0]
        end = arr[i][1]
        # second loop 
        for j in range ( i+1, len(arr)):

            # overlapping condition check 
            if arr[j][0] <= end:
                # Update the end with, max possible element 
                end = max (end, arr[j][1])
            if [ start, end ] in ans :
                continue
            else:
                break 
        ans.append((start, end))
         
    return ans
    # intialize the start and end variable -> ( start, end )

# TC O(n^2)
# SC O(1)

# -------------------------------
# Optimal sol 

def Merge_Overlapping_Subinterval(arr):
    ...



# TC O(n)
# SC O(1)



intervals=[[1,3],[2,4],[2,6],[8,10],[15,18]]
print(Merge_Overlapping_Subinterval(intervals))