

# Intersection of two sorted array 
# Brute Force Approach 

def Intersection( arr1, arr2 ):
    n1 = len(arr1)
    n2 = len(arr2) 

    vis = [0] * n2
    ans = []

    for i in range(n1):
        for j in range (n2):
            if arr1[i] == arr2[j] and vis[j] == 0:
                ans.append(arr1[i])
                vis[j] = 1
                break
            elif arr1[i] < arr2[j]:
                break 
    return ans


# Time Complexity O( n1 x n2 )
# Space complexity O( n2 )

#---------------------------------------------------------------

# Optimal Approach 
""" Two Pointers Approach """

def Intersection_Optimal (arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    # intialize pointers 
    i,j = 0,0 

    # To store the Intersection element
    res = []

    # Traversing within array bounds 
    while i < n1 and j < n2:

        # if arr1 element is smaller, move i pointer forward 
        if arr1[i] < arr2[j]:
            i+=1

        # if arr2 element is smaller, move j pointer forward 
        elif arr1[i] > arr2[j]:
            j +=1
        
        # If both element is equal, add in res and move both pointer forward 
        else:
            res.append(arr1[i])
            i+=1
            j +=1
    return res


# Time Complexity O( n1 + n2) Where n1 and n2 is the size of two arrays 
# Space Complexity O( 1) no aditional space is used

#-------------------------------------------------------

arr1 = [1,2,2,2,3,3,4,5,6]
arr2 = [ 2,3,3,5,6,6,7]
print(Intersection_Optimal(arr1, arr2))