# Minimum Number of days to make m Bouquets 

# Brute Force 
import math
# helper Function to Find the total num of Bouqets in some day 
def Bouquets(arr, day, k):
    Flower_count, no_of_Bouquets = 0 , 0
    for i in range (len(arr)):
        if arr[i] <= day:
            Flower_count += 1
        
        # the arr[i] > day 
        else:
            no_of_Bouquets +=  Flower_count / k # [ 7 7 7 7 13 ] at day = 7 flower_c = 4/k -> 4 /3 -> 1
            Flower_count = 0

        no_of_Bouquets += Flower_count / k  # Check for rest of the flower 3/3 -> 1 
    return no_of_Bouquets

    # range is [ min(Arr) to max (arr)] 7,8,9,10,11,12,13 
def M_Bouquets(days, m, k):
    n1 = min(days)
    n2 = max(days)

    # Loop from min value of bloom day to max val of arr
    for day in range (n1, n2):
        # if Total bouquets is greater or equal to 
        if Bouquets(days, day, k ) >= m :
            return day 
        
        else:
            return -1
        


# TC O( n x (max -min + 1))
# SC O(1)

# -----------------------------------------------

# Optimal Solution 

def M_Bouquets_Optimal(days, m , k):
    low = min(days) # at not possible 
    high = max (days) # at Possible 

    # Range ( min(a) to max (a))
    while ( low <= high ):
        mid = ( low + high )// 2

        if Bouquets(days, mid, k) >= m:
            high = mid -1
        else:
            low = mid + 1
        return low 


# TC O( n x log ( min - max +1))
# SC O(1)

#---------------------------------------

Bloom_Days = [7,7,7,7,13,11,12,7]
print(M_Bouquets(Bloom_Days, m= 2, k= 3))
print(M_Bouquets_Optimal(Bloom_Days, m= 2, k= 3))