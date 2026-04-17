# 🔥  05 -> Cyclic Sort

---

### 1. Simple definition (one sentence)

A technique where **each element is placed at its correct index by swapping, usually when numbers are in range [1…n]**.

---

### 2. Real-world analogy

Imagine **students standing in a line with roll numbers**—each student keeps swapping until they stand at their correct position (roll number = index).

---

### 3. When to use it (pattern/situation)

Use this when:

* Array contains numbers in range:

  * **[1 to n]** OR **[0 to n]**
* You need to find:

  * Missing number
  * Duplicate number
  * First missing positive
* Keywords:

  * “missing”
  * “duplicate”
  * “smallest missing”

👉 Core idea: **Correct index = value - 1**

---

### 4. Basic code template

#### Python

```python id="0g6q3h"
def cyclic_sort(arr):
    i = 0
    n = len(arr)
    
    while i < n:
        correct = arr[i] - 1
        
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    
    return arr
```

#### Java

```java id="1j8cwt"
int i = 0;

while (i < arr.length) {
    int correct = arr[i] - 1;
    
    if (arr[i] != arr[correct]) {
        int temp = arr[i];
        arr[i] = arr[correct];
        arr[correct] = temp;
    } else {
        i++;
    }
}
```

👉 **Time Complexity:** O(n)
👉 **Space Complexity:** O(1)

---

### 5. Easy example + walkthrough

**Input:**
`[3, 1, 5, 4, 2]`

#### Steps

* i=0 → value=3 → correct index=2 → swap
  → `[5,1,3,4,2]`

* i=0 → value=5 → correct=4 → swap
  → `[2,1,3,4,5]`

* i=0 → value=2 → correct=1 → swap
  → `[1,2,3,4,5]`

* Now correct → move forward

#### Output

`[1,2,3,4,5]`

---

### 6. Common mistakes beginners make

* ❌ Not checking `arr[i] != arr[correct]` → infinite loop
* ❌ Using it when numbers are **not in range [1…n]**
* ❌ Forgetting `correct = arr[i] - 1`
* ❌ Incrementing `i` even when swap is needed
* ❌ Not handling duplicates properly

---

## 🔥 Key Insight

👉 **Swap until every number reaches its correct index**

---

## 🔹 Must-Do Problems

* Missing Number
* Find All Missing Numbers
* Find Duplicate Number
* First Missing Positive ⭐

---

# Problem Statements -> 

## 🔹 Easy (Core Understanding)

1. **Missing Number** ⭐
   → Find missing number in range `[0…n]`

2. **Find All Missing Numbers** ⭐
   → Some numbers missing in `[1…n]`

3. **Find Duplicate Number (single duplicate)**
   → One number appears twice

---

## 🔹 Medium (Most Important)

4. **Find All Duplicates in an Array** ⭐⭐
   → Multiple duplicates possible

5. **Set Mismatch** ⭐⭐
   → One duplicate + one missing

6. **First Missing Positive** ⭐⭐⭐ (VERY IMPORTANT)
   → Smallest missing positive integer

---

## 🔹 Advanced Variations

7. **Find the Corrupt Pair**
   → One number duplicated, one missing

8. **Find the Smallest Missing Positive (optimized)**
   → Variation of above with constraints

---

## 🔥 Must-Do (High ROI)

Focus on these first:

* Missing Number
* Find All Missing Numbers
* Find All Duplicates
* First Missing Positive ⭐

---

## 🧠 Pattern Recognition Cheat Sheet

| Problem Type           | Idea                                    |
| ---------------------- | --------------------------------------- |
| Missing number         | Place at correct index, find mismatch   |
| Duplicate              | If correct index already has same value |
| Multiple missing       | Scan for index mismatch                 |
| First missing positive | Ignore negatives/out-of-range           |

---

## ⚡ Pro Insight

Cyclic sort is not about sorting—
👉 it’s about **placing elements at their correct index to reveal hidden info (missing/duplicate)**

---
