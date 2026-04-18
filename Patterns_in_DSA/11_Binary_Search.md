# 🔥 Modified Binary Search -> 

---

### 1. Simple definition (one sentence)

A technique where **binary search is adapted to work on non-standard sorted structures (like rotated arrays, infinite arrays, or condition-based searches)**.

---

### 2. Real-world analogy

Think of searching in a **rotated phone directory**—it’s still sorted, but not in the usual order, so you adjust your search logic.

---

### 3. When to use it (pattern/situation)

Use this when you see:

* **Sorted but modified data**
* Variations like:

  * Rotated arrays
  * Nearly sorted arrays
  * Infinite arrays
  * Peak element problems
* Keywords:

  * “sorted but rotated”
  * “find first/last occurrence”
  * “minimum/maximum in sorted array”

👉 Core idea:

* Still divide by mid, but **decide which half is valid**

---

### 4. Basic code template

#### Python

```python
def modified_binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # check sorted half
        if arr[left] <= arr[mid]:  # left is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

#### Java

```java
int left = 0, right = arr.length - 1;

while (left <= right) {
    int mid = (left + right) / 2;
    
    if (arr[mid] == target) return mid;
    
    if (arr[left] <= arr[mid]) { // left sorted
        if (arr[left] <= target && target < arr[mid]) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    } else { // right sorted
        if (arr[mid] < target && target <= arr[right]) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
}
```

👉 **Time Complexity:** O(log n)
👉 **Space Complexity:** O(1)

---

### 5. Easy example + walkthrough

**Input:**
`arr = [4,5,6,7,0,1,2], target = 0`

#### Steps

* mid = 7 → left half sorted
* target not in left → go right
* mid = 1 → right half sorted
* target in right → found

#### Output

Index = `4`

---

### 6. Common mistakes beginners make

* ❌ Not identifying which half is sorted
* ❌ Using normal binary search blindly
* ❌ Wrong boundary conditions (`<=` vs `<`)
* ❌ Infinite loop due to wrong updates
* ❌ Not handling duplicates properly

---

## 🔥 Key Insight

👉 Always ask:
**“Which half is sorted?” → then decide direction**

---

## 🔹 Must-Do Problems

* Search in Rotated Sorted Array ⭐⭐
* Find Minimum in Rotated Sorted Array ⭐⭐
* Find Peak Element ⭐⭐
* First and Last Position of Element ⭐⭐
* Search in Infinite Sorted Array ⭐⭐⭐

---

## ⚡ Pro Insight

Binary search is not just search—
👉 it’s about **eliminating half of the search space intelligently**

---
# problem Statement 

## 🔹 Easy (Foundation)

1. **Binary Search (Classic)** ⭐
   → Base template (must know perfectly)

2. **First and Last Position of Element** ⭐⭐
   → Find range using two binary searches

3. **Search Insert Position**
   → Where to insert target

---

## 🔹 Medium (Core Interview Level)

4. **Search in Rotated Sorted Array** ⭐⭐
   → Identify sorted half

5. **Find Minimum in Rotated Sorted Array** ⭐⭐
   → Pivot detection

6. **Find Peak Element** ⭐⭐
   → Compare with neighbors

7. **Search in Nearly Sorted Array**
   → Check mid, mid±1

---

## 🔹 Hard / Advanced

8. **Search in Infinite Sorted Array** ⭐⭐⭐
   → Expand range + binary search

9. **Median of Two Sorted Arrays** ⭐⭐⭐
   → Binary search on partitions

10. **Kth Smallest Element in Sorted Matrix** ⭐⭐⭐
    → Binary search on answer

---

## 🔥 Must-Do (High ROI)

Focus on these:

* First and Last Position
* Search in Rotated Sorted Array
* Find Minimum in Rotated Array
* Find Peak Element
* Median of Two Sorted Arrays ⭐⭐⭐

---

## 🧠 Pattern Recognition Cheat Sheet

| Pattern               | Trick                  |
| --------------------- | ---------------------- |
| Rotated array         | find sorted half       |
| First/last occurrence | bias left/right        |
| Peak element          | compare neighbors      |
| Infinite array        | expand window          |
| Answer-based search   | binary search on range |

---

## ⚡ Pro Insight

Modified Binary Search is about one question:
👉 **“Which half can I safely discard?”**

If you answer that correctly → problem is solved.

---
