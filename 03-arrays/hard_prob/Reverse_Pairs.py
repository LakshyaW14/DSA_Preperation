# Reverse pairs 
# Intuition -> i < j and a[i] > 2 * a[j]

# Brute Force Approach 
def Reverse_Pairs_Brute(arr):

    count = 0
    # First loop 
    for i in range (len(arr)):
        # Second Loop 
        for j in range ( i+1, len(arr)):
            # Reverse Pairs condition 
            if arr[i] > 2 * arr[j]:
                count += 1

    return count

# TC O(n^2) nested Loop 
# SC O(1)

#------------------------------


# Optimal Sol 
""" merge sort """

def Count_Pairs(arr, low, mid, high): 
    # Count variable 
    count = 0 
    right = mid + 1

    # First Loop for iterating over left half of arr 
    for i in range ( low, mid + 1): 
        while ( right <= high) and ( arr[i] > 2 * arr[right]):
            right += 1
            
        count += right - ( mid +1 )

    return count 


# 
def Merge(arr, low, mid, high):
    i = low 
    j = mid + 1
    temp = []
    while (i<= mid) and ( j <= high):
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1

        else:
            temp.append(arr[j])
            j += 1

    # Copy left 
    while ( i<= mid ):
        temp.append(arr[i])
        i += 1

    # Copy right 
    while ( j <= high):
        temp.append(arr[j])
        j += 1 

    # Copy back to original array 
    for i in range ( low , high+1):
        arr[i] = temp[i - low]

    
    

def Merge_Sort(arr, low , high):

    count = 0

    if low >= high :
        return count
    
    mid = ( low + high)//2
    
    # Divide 
    # Left Half
    count += Merge_Sort(arr, low , mid)

    # Right half 
    count += Merge_Sort(arr, mid +1 , high)
    
    # Modification 
    count += Count_Pairs(arr, low, mid , high)

    # Merge 
    Merge(arr, low, mid, high )

    return count 


def Reverse_pair_Optimal (arr):
    n = len(arr)
    return Merge_Sort(arr, 0 , n -1 )

if __name__ == "__main__":
    nums = [1,3,2,3,1]
    cnt = Reverse_pair_Optimal(nums)

    print ( " the Number of Reverse pair is : ", cnt)


# TC O(n logn) 
# Merge Sort performs logn levels of recursion 
# at Each level, Counting and Merging together takes O(n)

# SC O(n) temp array used during merging 
# the original 

# Important interview pov 
# the original arr get modified 
# before algo -> [ 1, 3, 2, 3, 1]
# after algo -> [ 1, 1, 2, 3, 3]

# use arr.copy() if don't want to modify the arr 
