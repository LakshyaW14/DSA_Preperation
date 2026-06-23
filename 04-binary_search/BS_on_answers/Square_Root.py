# Find Square Root of a num 

# Brute Force Approach

def Brute_Sqrt(num):
    ans = 0
    for i in range(num):
        if i*i <= num:
            ans = i
        else:
            break
    return ans 

# TC O(n)
# SC O(1)

#------------------------------------

print(Brute_Sqrt(num=28))