# Merge Overlapping Subinterval 

# Brute Force 

def Merge_Overlapping_Subinterval(arr):
    # arr to store the result
    arr.sort()
    ans = []
    
    # intialize the start and end variable -> ( start, end )

    # iterating over the arr
    for i in range (len(arr)):  # 0 -> n
        
        # After merging intervals ( overlapping intervals visited by j pointer ),
        #  you must somehow skip all the intervals that were merged. i not nedd to visit the merged intervals 

        # Skip if this interval is already merged 
        if ans and arr[i][1] <= ans [-1][1]:
            continue

        start = arr[i][0]
        end = arr[i][1]

        # second loop 
        # Check all following Interval 
        for j in range ( i+1, len(arr)):

            # overlapping condition check 
            if arr[j][0] <= end:
                # Update the end with, max possible element 
                end = max (end, arr[j][1])
           
            else:
                break 

        ans.append([start, end])
         
    return ans
    # intialize the start and end variable -> ( start, end )

# TC  O(nlogn) + O(N^2)nearly  
# SC O(N)

# -------------------------------
# Optimal sol 

def Merge_Overlapping_Subinterval_Optimal(arr):
    
    # Sort the arr
    arr.sort()

    ans =[]

    # Current_start = arr[i][0]
    # Last_end = ans [-1][1]

    # iterating
    for i in range (len(arr)) :

        # First Interval
        if not ans :
            ans.append(arr[i])

        # Curent > last there is no overlap, so append 
        if ans and arr[i][0] > ans[-1][1] :
            ans .append(arr[i])

        # Overlap
        else:
            ans [-1][1] = max(ans[-1][1] , arr[i][1])

    return ans 

# TC O(nlogn) sorting + single traversal O(n)

# SC O(1) the extra auxiliary space ,excluding the ans list 
# else O(n) for ans list
#  
# ----------------------------------------


intervals=[[1,3],[2,4],[2,6],[8,10],[15,18]]
print(Merge_Overlapping_Subinterval(intervals))
print(Merge_Overlapping_Subinterval_Optimal(intervals))