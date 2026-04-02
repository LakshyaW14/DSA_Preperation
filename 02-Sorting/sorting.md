



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
        swapped = False

        # last i elements are already in place
        for j in range(0, n - i - 1):

            # swap if current element is greater than next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # if no swaps happened, array is already sorted
        if swapped == False:
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

End of Notes ✅
