# Four sum 

# Brute solution 

def Four_Sum(arr, target):
    n = len(arr)

    # use Set for unique quads , avoiding duplicates
    st = set()
    # Pick first ele
    for i in range (n):
        # Pick Second element
        for j in range (i+1, n):
            # Pick third Element
            for k in range ( j+1, n):
                # Pick  Fourth Element 
                for l in range ( k+ 1, n):

                    total = arr[i] + arr[j] + arr[k] + arr[l]
                    if total == target:

                        # store sorted quads as Tuple 
                        nums = tuple(sorted([ arr[i], arr[j], arr[k], arr[l]]))
                        
                        st.add(nums)
    return [ list(quad) for quad in st ]

# TC O(n^4) 
# sorting 4log 4 -> O(1)
# Avg Hash set Insertion O(1)
# Converting set to list O(m)

# SC the set store all unique ele, if there are m unique ele  -> O(m)
# Ignoring Output Storage O(1)


# ----------------------------------

# Better Sol 

def Four_Sum_Better (arr, target):
    n = len(arr)


    st = set()      #O(m)

    # First Loop 
    for i in range (n):
        # Second loop 
        for j in range (i+1,n):
            # Third Loop 
            # Store numbers between j and k
            seen = set()  #O(N) hashSet
            for k in range (j +1, n):

                Fourth = target - (arr[i]+arr[j]+ arr[k])
                # 
                if Fourth in seen  : # Hash Lookup 
                    temp = tuple(sorted([arr[i], arr[j], arr[k], Fourth]))
                    st.add(temp)     # Hash Insertion 
                
                # Add Current Element to seen 
                seen.add(arr[k])

    return [ list(quad) for quad in st]


# TC O(n^3)

#Sc O(n +m)

# --------------------------------

# Optimal Sol 

# using Two Pointers 

def Four_Sum_Optimal(arr, target):

    n = len(arr)
    arr.sort()
    ans = []

    # First loop
    for i in range (n):
        # skip Duplicates 
        if i > 0 and (arr[i] == arr[i-1]):
            continue

            # Second loop 
        for j in range (i+1, n):
            # skip duplicates 
            if j > i+1 and ( arr[j] == arr[j-1]):
                continue

            k = j +1
            l = n-1

            # Two pointers
            while (k < l):
                total = arr[i] + arr[j] + arr[k] + arr[l]
                if total == target :
                    ans.append([arr[i], arr[j], arr[k], arr[l]])
                    k += 1
                    l -= 1
                    
                # skip Duplicates for k and l
                    while k < l and ( arr[k] == arr[k+1]):
                        k += 1
                    while k < l and ( arr[l] == arr[l-1]):
                        l -= 1
                   
                # 
                elif total < target :
                    k += 1

                else:
                    l -= 1
    return ans 

# TC O(nlogn) + O(n^3)
# SC O(1) auxillary spaxe 
#  if including output O(m)
 

# -----------------------------------------

arr=[1,0,-1,0,-2,2]
print(Four_Sum(arr,0))
print(Four_Sum_Better(arr,0))
print(Four_Sum_Optimal(arr,0))