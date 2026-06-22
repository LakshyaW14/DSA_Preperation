# Find Peak element 

# Brute Force -> Linear Search 

# Hypothetically the -1 and n idx of arr is set to - infinity

def Peak_Ele(arr):
    n =len(arr)
    for i in range(n):
        if ( i == 0 or arr[i] > arr[i+1]) and ( i == n-1 or arr[i] > arr[i-1]):
            return i 
        
# Tc O(n)
# SC O(1)

#-----------------------------------------------

