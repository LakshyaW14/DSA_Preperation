j =5        #Pattern Length 
# Square of star 
for i in range(1,j+1): #row  
    print("*" *j)

# triangle of star (not centered)
for i in range (1, j+1):
    print("*"* i)

# triangle of numbers 
for i in range (1, j+1):
    print()
    for z in range (1,i+1):
        print(z,end=" ")

# triangle of number 
for i in range (1,j+1):
    print()
    for z in range(1,i+1):
        print(i,end="")

# Inverted triangle (not centered )
for i in range(j,0,-1):
    print("*"*i)

# inverted triangle number 
for i in range (j,0,-1):
    print()
    for z in range (1,i+1):
        print(z,end="")

# triangle (centered )

for i in range (1,j+1):
    spaces= j-i
    stars = 2*i - 1
    print(" "*spaces + "*"*stars,end="\n")

# inverted triangle ( centered)
for i in range (j,0,-1):
    spaces= j-i
    stars = 2*i - 1 
    print(" "*spaces + "*"*stars,end="\n")

# diamond pattern 

for i in range (1,j+1):
    spaces= j-i
    stars = 2*i - 1
    print(" "*spaces + "*"*stars,end="\n")
for i in range (j,0,-1):
    spaces= j-i
    stars = 2*i - 1 
    print(" "*spaces + "*"*stars,end="\n")

# double triange ( not centered )
for i in range (1,j):
    print(i*"*")
for i in range (j,0,-1):
    print(i*"*")

# 1
# 01
# 101
# 0101
# 10101

for i in range (1,j+1):
    print()
    if i % 2==0:
        num=0
    else: 
        num=1
    for z in range (1,i+1):
        print(num,end="")
        num = 1-num
    
#Number crown pattern
for i in range (1,j+1):
    print()
    for z in range(1,i+1):
        print((z),end="")

    spaces = 2*(j-i)*"-"
    print(spaces,end="")

    for z in range (i,0,-1):
        print(z,end="")
        


# continous number pattern 
num=1
for i in range(1,j+1):
    for z in range(i):
        print(num,end="")
        num+=1
    print()

#alpha  triangle pattern 
num=64
for i in range (1,j+1):
    for z in range(1,i+1):
        print(chr(num+z),end="")
        
    print()    

#alpha  triangle pattern inverted
num =64
for i in range (j,0,-1):
    for z in range(1,i+1):
        print(chr(num+z),end="")
        
    print()


# alpha pattern 
num=64
for i in range (1,j+1):
    for z in range(1,i+1):
        print(chr(num+i),end="")
        
    print() 

#alpha pattern centered 
num=64
for i in range(1,j+1):
    spaces = (j-i)*" "
    print()
    print(spaces,end="")
    for x in range(1,i):
        print(chr(num+x) ,end="")
    for z in range(i,0,-1):
        print(chr(num+z), end="")

# reversed alpha triangle 

num =65
for i in range(1,j+1):
    print()
    for z in range (j-i,j):
        print(chr(num+z),end="")




for i in range(1,j+1):
    print()
    for j in range (1,i+1):
        print(j*"*",end="")

    spaces= 2*(j-i)*"-"
    print(spaces,end=" ")

    for k in range (i,0,-1):
        print(k*"*",end="")

# Butterfly pattern
for i in range (j,0,-1):
    print()
    print(i*"*",end="")

    spaces= 2*(j-i)*" "
    print(spaces,end="")

    print(i*"*",end="")

for i in range (1,j+1):
    print()
    print((i*"*"),end="")

    spaces = 2*(j-i)*" "
    print(spaces,end="")

    print(i*"*",end="")

#Butterfly pattern 
# general formula for mirror problems 
#mirror_row = min(i,total_rows-i+1)   for mirror pattern questions 


for i in range(1,2*j+1):
    if i<= j :
        row=i
    else:
        row=(2*j - i+1)
    #Alternate way
    # row = min (i,2*j - i+1)
    
    print(row*"*",end="")

    spaces = 2*(j-row)*" "
    print(spaces,end="")

    print(row*"*",end="")

    print()


# hollow square pattern 
spaces=(j-2)*" "
for i in range(1,j+1):
    if i == 1 or i==j:
        print(j*"*")
    else:
        print("*"+spaces+"*")

#hollow square with row-col logic  ( matrix of row and col) work with all hollow pattern 
for row in range(1,j+1):
    for col in range(1,j+1):
        if row==1 or row==j or col==1 or col==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()


#concentric square pattern 
#edge distance method
size = 2*j -1

for row in range(size): 
    for col in range(size):
        top= row      #distance of cell from all edges
        left=col
        right= size-col-1
        bottom = size-row-1
        
        #decides which layer the cell belongs to 
        layer= min(top,left,right,bottom)
        print(j-layer,end=" ")
    print()

#center distance method

size=2*j-1
center = j-1
for row in range (size):
    for col in range (size):
        distance= max(abs(row-center),abs(col-center))  # distance from center for each cell 

        print(distance+1,end=" ")
    print()