

---

# 03- Merge Sort

## Concept

Merge Sort is a **Divide and Conquer algorithm** that breaks a problem into smaller subproblems, solves them independently, and then combines the results.

It divides the array into halves until each subarray has only one element, then merges them back in sorted order.

---

## Intuition

> “Break the array until it cannot be broken further, then rebuild it in sorted order.”

- A single element is always sorted.
- So instead of sorting directly, we:
  1. Divide the array
  2. Sort smaller parts
  3. Merge them

👉 Key Insight:
- **Splitting does NOT sort**
- **Sorting happens during merging**

---

## Algorithm Steps

1. If array size ≤ 1 → return (already sorted)
2. Find middle index
3. Recursively sort left half
4. Recursively sort right half
5. Merge both sorted halves

---

## Code (Python)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
````

---

## Dry Run

Input:

```
[38, 27, 43, 3]
```

### Divide:

```
[38, 27, 43, 3]
→ [38, 27] [43, 3]
→ [38] [27] [43] [3]
```

### Merge:

```
[38] + [27] → [27, 38]
[43] + [3]  → [3, 43]
```

### Final Merge:

```
[27, 38] + [3, 43]
→ [3, 27, 38, 43]
```

---

## Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n log n) |
| Average Case | O(n log n) |
| Worst Case   | O(n log n) |

### Reason:

* Splitting → log n levels
* Merging → n work at each level

👉 Total = **O(n log n)**

---

## Space Complexity

```
O(n) + O(log n)
```

* O(n) → temporary arrays during merge
* O(log n) → recursion stack

---

## Key Points

✔ Stable sorting algorithm
✔ Uses Divide & Conquer
✔ Works well for large datasets
✔ Predictable performance (no worst-case degradation)
❌ Not in-place (uses extra memory)

---

## Interview Questions

### Basic

* What is Merge Sort?
* Why is it called Divide and Conquer?
* Why is its time complexity always O(n log n)?

---

### Intermediate

* Why is Merge Sort stable?
* Why does it require extra space?
* Compare Merge Sort vs Quick Sort

---

### Advanced

* Can Merge Sort be implemented in-place?
* How does Merge Sort work on Linked Lists?
* Write iterative (bottom-up) Merge Sort

---

## Final Summary

> Merge Sort divides the array into smaller parts and merges them back in sorted order using recursion.


---
#  05 - Quick Sort — Concept + Intuition

**Quick Sort** is a **divide-and-conquer** sorting algorithm.

Instead of splitting the array into equal halves (like Merge Sort), it:

1. Picks a **pivot element**
2. Partitions the array into:

   * Elements **less than pivot**
   * Elements **greater than pivot**
3. Recursively applies the same process on both sides

---

### 🧠 Core Idea

> “Put the pivot in its correct sorted position, then sort left and right parts.”

---

### ⚙️ Working Steps

Given array:

```
[8, 3, 1, 7, 0, 10, 2]
```

Pick pivot (usually last element → `2`)

After partition:

```
[1, 0, 2, 7, 3, 10, 8]
        ↑
     pivot fixed
```

Now:

* Left: `[1, 0]`
* Right: `[7, 3, 10, 8]`

Repeat recursively.

---

### 🔁 Algorithm (Python Code)

```python
def partition(arr, low, high):
    pivot = arr[high]  # choose last element as pivot
    i = low - 1        # pointer for smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot at correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)   # left
        quick_sort(arr, pi + 1, high)  # right
```

---

### 🧪 Dry Run (Short)

Array:

```
[4, 2, 6, 1, 3]
```

Pivot = 3
After partition:

```
[2, 1, 3, 6, 4]
        ↑
```

Then recursively:

* Left → `[2,1] → [1,2]`
* Right → `[6,4] → [4,6]`

Final:

```
[1,2,3,4,6]
```

---

### ⏱️ Time Complexity (Important)

| Case       | Time Complexity |
| ---------- | --------------- |
| Best Case  | **O(n log n)**  |
| Average    | **O(n log n)**  |
| Worst Case | **O(n²)**       |

👉 Worst case happens when:

* Array is already sorted
* Pivot is always smallest/largest

---

### 💾 Space Complexity

* **O(log n)** → due to recursion stack (best/average)
* **O(n)** → worst case recursion depth

---

### ⚡ Why Quick Sort is Fast in Practice?

* In-place sorting (no extra array like Merge Sort)
* Better cache performance
* Used in real systems (with optimizations like random pivot)

---

### ⚖️ Quick Sort vs Merge Sort (Quick Insight)

| Feature       | Quick Sort | Merge Sort  |
| ------------- | ---------- | ----------- |
| Space         | In-place   | Extra space |
| Stability     | ❌ No       | ✅ Yes       |
| Worst Case    | O(n²)      | O(n log n)  |
| Practical Use | 🔥 Faster  | Reliable    |

---

### 💡 Key Interview Points

* Pivot selection matters (random / median improves performance)
* Not stable
* Tail recursion optimization possible
* Used in libraries (hybrid versions)

---


