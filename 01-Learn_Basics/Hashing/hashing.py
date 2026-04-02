

#Array hashing, when values are in limited range
# faster than dict ( no hashing overhead)

mylist=list(map(int,input("Enter numbers :").split(",")))

queries= list(map(int,input("Enter queries :").split(",")))

myhash=[0]*101

for num in mylist:
    myhash[num]+=1
for q in queries:
    print(myhash[q],end=" ") # TC 
    

# Basic hashing using dictionary ( frequency count ) 
arr = list(map(int,input("Enter numbers :").split(",")))
frequency = {}
for num in arr :
    frequency[num] = frequency.get(num,0) +1  #Tc o(n)
print(frequency)   

# Hashing with queries 

arr=[1,2,3,4,5,6,3,2,]
queries =[1,3,2]

fre={}
for num in arr:
    fre[num] = fre.get(num,0)+1
for q in queries:
    que= fre.get(q,0)
    print(q, "-" ,que)    # tc (n+q)



#Hashing for "check existence only" (Set )
arr=[1,2,3,4,5,6,3,2,]
s = set(arr)

print(20 in s) # False Tc (1)


#first non repeating element 
arr = [4, 5, 1, 2, 0, 4]
fre = {}
for num in arr :
    fre[num]= fre.get(num,0)+1
for num in arr :
    if fre[num] == 1:
        print("first non_repeating :", num )
        break


#character Hashing 
word="LakshyaA"
queries=["a","b"]
fre={}
for ch in word:
    fre[ch]=fre.get(ch,0)+1
print(fre)

for q in queries:
    index=fre.get(q,0)
    print(q, " : ", index)

# only for lowercase (not all character)
#for uppercase letter 
word=word.lower()
# frequency array
hash_arr =[0]*26    
for ch in word:
    index=ord(ch)-ord("a")
    hash_arr[index] +=1
print(hash_arr)

#answer array
for q in queries:
    index=ord(q)-ord("a")

    print(f"{q} : {hash_arr[index]} ")

#Tc O(n+q) faster than dict
