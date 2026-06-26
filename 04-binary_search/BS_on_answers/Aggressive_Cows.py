# Aggressive Cows 
# Binary Search Patter -> [ (min)max] or [(max)min ]

# Brute Force 
# We have to place the cows in (min) distance that is (max )
# Cows >= 2
def CanWePlace(arr, distance,cows) :
    # Place first cow at first place 
    cow_cnt = 1
    last_pos = arr[0]

    for i in range (len(arr)):
        if arr[i] - last_pos >= distance:
            # Place a cow here 
            cow_cnt += 1
            last_pos = arr[i]
        
        # if all cows are placed 
        if cow_cnt >= cows:
            return True
    # if not possible to place all cows 
    return False
        

# Answer Range is Distance low = 1 high = max(Arr)
# Worst Case  cow1 at 1 and cow2 at farthest distance 
def Aggressive_Cows (stalls, cows):
    # Sort stalls Position 
    stalls.sort()

    # Maximum Possible Distance 
    maxdist = stalls[-1] - stalls[0]

    # Try all possible distance from 1 to maxdist
    for d in range ( 1, max(arr) +1):
        # if cows can be placed with distance d
        if CanWePlace (stalls, d, cows):
            ans = d

    return ans
    
    
# TC O( nlogn) + O(n) x O(max - min + 1)  -> nearly n^2
# sc O(1)

# ------------------------------------

    


arr= [ 0 , 3, 4, 7, 10 , 9]

print(Aggressive_Cows(arr, 4))
