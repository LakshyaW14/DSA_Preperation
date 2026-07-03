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

# SC the set store all unique ele, if there are m unique ele  -> O(m)

arr=[1,0,-1,0,-2,2]
print(Four_Sum(arr,0))