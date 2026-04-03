



# 🔹 1. Bubble Sort (Concept + Code + TC)

## 🧠 Intuition

Bubble Sort works by repeatedly comparing **adjacent elements** and swapping them if they are in the wrong order.

Why “Bubble”?

Because elements slowly rise to their correct position step by step, like bubbles in water.

👉 After each pass, the **largest unsorted element moves to the end**.

---

## ✅ Code

```python
def Bubble_Sort(arr):
    n = len(arr)

    # traverse all array elements
    for i in range(n):
        # swapped flag for early exit
        swapped = False

        # last i elements are already in place
        for j in range(0, n - i - 1):

            # swap if current element is greater than next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # if no swaps happened, array is already sorted
        if not swapped:
            break
```

---

## 🔍 How It Works

* Compare adjacent elements
* Swap if they are in wrong order
* Repeat for all elements
* After each pass, largest element settles at correct position

---

## ⏱️ Time Complexity (TC)

| Case    | TC    | Reason                       |
| ------- | ----- | ---------------------------- |
| Worst   | O(n²) | Nested loops                 |
| Average | O(n²) | Same comparisons             |
| Best    | O(n)  | Already sorted (early break) |

---

## 📦 Space Complexity

* **O(1)** → In-place sorting (no extra memory used)

---

## ⚡ Optimization Used

* `swapped` flag
* If no swaps happen → stop early

👉 This reduces TC from **O(n²) → O(n)** in best case

---

## 🎯 Key Properties

* Stable sort ✅
* In-place ✅
* Simple but inefficient ❌

---

## 🚀 Interview Insight

👉 Important observation:

* After 1st pass → largest element fixed
* After 2nd pass → 2nd largest fixed

👉 So inner loop reduces every time: `n-i-1`

---

## ❗ When NOT to Use

* Large datasets ❌
* Real-world systems ❌

👉 Better alternatives:

* Merge Sort → O(n log n)
* Quick Sort → O(n log n)

---

## 🎯 One-Line Summary

> In each pass, the largest unsorted element "bubbles" to its correct position.

---


#  Selection Sort (concept + code + tc)

## ✅ Code

```python
def Selection_Sort(arr):
    n = len(arr)

    for i in range(n - 1):

        # assume current index has minimum
        min_idx = i

        # find actual minimum in unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # place minimum at correct position
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

---

# 🧠 Concept (Intuition)

Selection Sort works by:

1. Dividing the array into two parts:

   * Sorted part (left)
   * Unsorted part (right)

2. For each position `i`:

   * Find the **minimum element** in the unsorted portion
   * Swap it with position `i`

👉 After each pass, the smallest element is fixed in its correct position.

---

# 🔍 How It Progresses

Example:

```
[5, 3, 4, 2, 1]
```

* Pass 1 → min = 1 → swap with index 0 → `[1, 3, 4, 2, 5]`
* Pass 2 → min = 2 → swap with index 1 → `[1, 2, 4, 3, 5]`
* Pass 3 → min = 3 → swap with index 2 → `[1, 2, 3, 4, 5]`

---

# ⏱️ Time Complexity (TC)

| Case    | Time Complexity |
| ------- | --------------- |
| Best    | O(n²)           |
| Average | O(n²)           |
| Worst   | O(n²)           |

### 📌 Why?

* Outer loop runs `n` times
* Inner loop scans remaining elements
* Total comparisons ≈ `n(n-1)/2`

👉 Always quadratic, no early exit optimization

---

# 📦 Space Complexity

* **O(1)** (in-place sorting)

---

# ⚡ Key Properties

* In-place ✅
* Not stable ❌
* Not adaptive ❌
* Minimum swaps (≤ n-1) ✅

---

# 🎯 Important Insight

* Comparisons → **O(n²)**
* Swaps → **O(n)**

👉 Useful when **swapping is costly but comparisons are cheap**

---

# 🚀 One-Line Summary

> Repeatedly select the minimum element from the unsorted part and place it at the correct position.
