# KoKo Eating Banana 

# Brute Force 
import math

# Helper Function -> to calculate total hours for given speed
def Req_Time(arr,hrs):

    Total_time = 0

    for pile in arr:
        Total_time += math.ceil(pile/hrs)
    return Total_time
    
# Function to find the minimum eating speed 
def KoKo_Banana_Brute (pile, hrs):
    # Max Pile Size
    MaxVal = max(pile)

    # Loop from 1 to max(pile)
    for i in range (1, MaxVal +1):

        hours = Req_Time( pile, i)

        # if hours fitt within hrs 
        if hours <= hrs:
            return i
    return MaxVal
        

# TC O( n x max(arr)) since for each possible speed we go through all the piles.
# SC O(1)

#----------------------------------------------------------



pile = [ 3, 6, 7, 11]
pile2 = [25, 12, 8, 14, 19] 
time = 8
print(KoKo_Banana_Brute(pile, time))