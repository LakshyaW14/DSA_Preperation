# 📌 Hashing in DSA (Complete Guide)

This document covers:

* Concepts of hashing
* Types of hashing techniques
* Time Complexity (TC)
* Common interview problems

---

# 🔹 1. What is Hashing?

Hashing is a technique used to store and retrieve data efficiently using a **key → value mapping**.

👉 Goal: Achieve **O(1)** lookup time.

---

# 🔹 2. Array Hashing (Frequency Array)

## ✅ Concept

* Used when the range of values is **limited and known**
* Uses direct indexing instead of hashing function

## ✅ Code

```python
myhash = [0] * 101

for num in mylist:
    myhash[num] += 1

for q in queries:
    print(myhash[q])
```

## ✅ Time Complexity

* Building array: **O(n)**
* Query lookup: **O(q)**
* **Total TC = O(n + q)**

## ✅ Space Complexity

* **O(k)** (k = range, here 101)

## ⚡ Advantage

* Faster than dictionary (no hashing overhead)

## ❌ Limitation

* Only works when range is small (e.g., 0–100)

---

# 🔹 3. Dictionary Hashing (Frequency Map)

## ✅ Concept

* Works for **any range of values**
* Uses hashing internally

## ✅ Code

```python
frequency = {}
for num in arr:
    frequency[num] = frequency.get(num, 0) + 1
```

## ✅ Time Complexity

* Build: **O(n)**
* Lookup: **O(1)** (average case)
* **Total TC = O(n)**

## ⚠️ Note

* Worst case: **O(n)** (due to collisions, rare)

## ✅ Space Complexity

* **O(n)**

---

# 🔹 4. Hashing with Queries

## ✅ Code

```python
fre = {}
for num in arr:
    fre[num] = fre.get(num, 0) + 1

for q in queries:
    print(fre.get(q, 0))
```

## ✅ Time Complexity

* Build: **O(n)**
* Queries: **O(q)**
* **Total TC = O(n + q)**

---

# 🔹 5. Set (Existence Checking)

## ✅ Concept

* Used only to check presence

## ✅ Code

```python
s = set(arr)
print(20 in s)
```

## ✅ Time Complexity

* Build: **O(n)**
* Lookup: **O(1)**

## ⚡ Use Case

* Fast membership testing

---

# 🔹 6. First Non-Repeating Element

## ✅ Problem

Find the first element that appears only once.

## ✅ Code

```python
fre = {}
for num in arr:
    fre[num] = fre.get(num, 0) + 1

for num in arr:
    if fre[num] == 1:
        print(num)
        break
```

## ✅ Time Complexity

* Frequency count: **O(n)**
* Scan again: **O(n)**
* **Total TC = O(n)**

---

# 🔹 7. Character Hashing (Dictionary)

## ✅ Code

```python
fre = {}
for ch in word:
    fre[ch] = fre.get(ch, 0) + 1

for q in queries:
    print(fre.get(q, 0))
```

## ✅ Time Complexity

* Build: **O(n)**
* Queries: **O(q)**
* **Total TC = O(n + q)**

---

# 🔹 8. Character Hashing (Array - Optimized)

## ✅ Concept

* Only for lowercase letters (a–z)

## ✅ Code

```python
word = word.lower()
hash_arr = [0] * 26

for ch in word:
    index = ord(ch) - ord('a')
    hash_arr[index] += 1

for q in queries:
    index = ord(q) - ord('a')
    print(hash_arr[index])
```

## ✅ Time Complexity

* Build: **O(n)**
* Queries: **O(q)**
* **Total TC = O(n + q)**

## ⚡ Why Faster?

* No hashing function
* Direct indexing

---

# ❗ Common Mistake (IMPORTANT)

❌ Wrong:

```
TC = O(n * q)
```

✅ Correct:

```
TC = O(n + q)
```

👉 Because:

* We are NOT looping queries inside array build
* Operations are separate

---

# 🧠 Interview Insight

| Approach      | TC     | Space | Use Case       |
| ------------- | ------ | ----- | -------------- |
| Array Hashing | O(n+q) | O(k)  | Small range    |
| Dictionary    | O(n+q) | O(n)  | General use    |
| Set           | O(n)   | O(n)  | Existence only |

---

# 🎯 Practice Problems

### 1. Count Frequency

Input: arr = [1,2,2,3]
Output: {1:1, 2:2, 3:1}

---

### 2. Query Frequency

Input:
arr = [1,2,2,3]
queries = [2,3,4]

Output:
2 → 2
3 → 1
4 → 0

---

### 3. First Non-Repeating Element

Input: [4,5,1,2,0,4]
Output: 5

---

### 4. Character Count

Input: "aabbc"
Output: a=2, b=2, c=1

---

# 🚀 Final Takeaway

* Use **array hashing** when range is small → fastest
* Use **dictionary** when range is large → flexible
* Use **set** when only checking existence

👉 In interviews:

* Always mention **TC = O(n + q)**
* Explain **why it's not O(n*q)**

---

End of Notes ✅
