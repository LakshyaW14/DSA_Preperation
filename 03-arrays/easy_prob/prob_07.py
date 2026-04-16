# Union of Two Sorted Array 

# Optimal Approach ( Two Pointers )
#  Since arrays are already sorted, we merge like merge-sort and skip duplicates.

def Union(arr1, arr2):

    # List to store the Union Elements 
    union =[]
    
    # Initialize the pointers 
    i,j=0,0

    # Iterating while both pointers are within the array bounds.
    while i < len(arr1) and j < len(arr2):
        # add if empty or Duplicate
        if i > 0 and arr1[i] == arr1[i-1]:
            i+=1
            continue 
        if j > 0 and arr2[j] == arr2[j -1]:
            j+=1
            continue
        # # Or 
        # if arr1[i] < arr2[j]:
        #     if not union or union[-1] != arr1[i]:
        #         union.append(arr1[i])
        #     i+=1
        
        # if element in arr1 is smaller 
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i+=1
        
        # if element in arr2 is smaller 
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j+=1
        
        # if both element are equal, add one -> update
        else:
            union.append(arr1[i])
            i+=1
            j+=1
        
        

    # Add Remaining Elements from arr1
    while i < len(arr1):
        if i == 0 or arr1[i] != arr1[i-1]:
            union.append(arr1[i])
        i+=1

    # add remaining elements from arr2
    while j < len(arr2):
        if j == 0 or arr2[j] != arr2[j-1]:
            union.append(arr2[j])
        j+=1

    return union


# Time Complexity: O(m+n), \
# Because at max i runs for n times and j runs for m times. When there are no common elements in arr1 and arr2 and all elements in arr1, arr2 are distinct. 

# Space Complexity : O(m+n) \
# {If Space of Union ArrayList is considered} O(1) {If Space of union ArrayList is not considered}


# ----------------------------------------------------------

# appraoch 1 -> using Set 

def FindUnion(arr1, arr2):
    # Create a set with elements of both array
    st = set(arr1) | set(arr2)

    # return sorted list 
    # py set() function worked as unordered_set, we need to sort it out 

    return sorted(st)

# TC O((m+n)log(m+n)) inserting an element into set takes log(n) time, if inserting m+n element\
# it takes log(m+n) time. adding all elements in worst case so (m+n)log(m+n)

# Using HashSet also takes the same time, On average insertion in unordered_set takes O(1) time but sorting the union vector takes O((m+n)log(m+n))  time.\
#  Because at max union vector can have m+n elements.

# SC O(m+n) {If Space of Union ArrayList is considered} ,O(1) {If Space of union ArrayList is not considered}

#--------------------------------------------------------------------------


# Approach 2 -> using map 

def FindUnion_2(arr1, arr2):
    # create a dictionary to store the frequency
    freq = {}

    for num in arr1:
        freq[num] = freq.get(num,0) +1
    for num in arr2:
        freq[num] = freq.get(num,0) +1
    union = sorted(freq.keys())

    return union

# Time Compleixty : O( (m+n)log(m+n) ) . Inserting a key in map takes logN times, where N is no of elements in map.\
#  At max map can store m+n elements, Using HashMap also takes the same time, 

#Space Complexity : O(m+n) {If Space of Union ArrayList is considered} ,O(1) {If Space of union ArrayList is not considered}

#----------------------------------------------------------------------------------

arr1 = [1,2,3,4,5] 
arr2 = [2,3,4,4,5]
print(FindUnion_2(arr1,arr2))