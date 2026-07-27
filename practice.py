def move_consecutve(arr):
    count = 0
    maxi = 0
    for num in arr :
        if num == 1:
            count +=1
            maxi = max (maxi, count)
        else:
            count=0

    return maxi 

arr = [1, 1, 0, 1, 1, 1]
# print(move_consecutve(arr))


def Two_sum (arr,target):
    n = len(arr)

    for i in range (n):
        for j in range (i, n):
            total = arr[i] + arr[j] 
            if total == target :
                return i,j
            
def Two_sum_optimal (arr,target):
    mp = {}

    for i in range (len(arr)):
        compliment = target - arr[i]
        if compliment in mp :
            return [ mp[ compliment ], i]
        mp[arr[i]] = i 

    return "No" 

def Two_Sum_(arr,target):

    nums= [ ( nums, idx) for idx, num in enumerate(arr)]
    nums.sort(key=lambda x : x[0])


    left , right = 0, len(arr)
    while left < right :
        sums = nums[left] [0] + nums[right] [0]

        if sum == target:
            return nums[left] [1] , nums[right] [1]
        elif sum < target:
            left +=1
        else:
            right -=1


def three_sum (arr):
    st = set()
    for i in range (len(arr)):
        for j in range (i, len(arr)):
            for k in range(j, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0 :
                    triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                    st.add(triplet)
        return [ list (triplet) for triplet in st ]


def Three (arr):
    st = set()
    for i in range (len(arr)):
        hashset = set()
        for j in range (i , len(arr)):
            third = -( arr[i] + arr[j])

            if third in hashset:
                trip = tuple(sorted([arr[i], arr[j], third]))
                st.add(trip)

            hashset.add(arr[j])


def three_pointers (arr):
    arr.sort()

    res=[]

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left, right = i+1, len(arr)-1

        while left < right :
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                res. append([arr[i], arr[left], arr[right]])

                left +=1
                right -=1
                while left < right and arr[left] == arr[left -1]:
                    left +=1
                while left < right and arr[right] == arr[right +1]:
                    right -=1
            elif total < 0:
                left +=1
            else:
                right -=1
    return res 

def Rotate_array (arr,k, direction):
    n = len(arr)
    if n == 0 :
        return 0
    k %= n
    if direction == "left":
        # copy the k element in temp 
        temp = arr[:k]

        # copy the remaining elemrnt 
        for i in range ( k, n):
            arr[i-k] = arr[i]

        # copy the k element in original arr 

        for i, num in enumerate(temp):
            arr[n-k+i] = num
    return arr


def get_element (arr):
    # for smallest and second_small 

    n =len(arr)

    smallest, second_small = float('inf'), float('inf')

    for num in arr :
        if num < smallest:
            second_small = smallest
            smallest = num 
        elif num < second_small and num != smallest:
            second_small= num 

    print(smallest, second_small)
arr=[2,4,24,89,6,5]


low =3
high =3

if low <= high:
    print("yes")
else:
    print('no')