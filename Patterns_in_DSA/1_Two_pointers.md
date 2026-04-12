# 🔥 01- Two Pointers 


### 1. Simple definition (one sentence)

A technique where **two indices traverse a data structure (usually an array/string) to reduce time complexity**, often from O(n²) → O(n).

---

### 2. Real-world analogy

Imagine two people starting at **opposite ends of a sorted line of numbers**, moving toward each other to find a pair whose sum matches a target.

---

### 3. When to use it (pattern/situation)

Use two pointers when you see:

* **Sorted array / string**
* **Pair problems** → sum, difference, etc.
* **Subarray / substring problems**
* **Reversing or rearranging**
* Keywords like:

  * “find pair”
  * “remove duplicates”
  * “longest substring”
  * “container with most water”

---

### 4. Basic code template

#### Python

```python
def two_pointer(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if condition:
            return result
        elif move_left_pointer:
            left += 1
        else:
            right -= 1
```

#### Java

```java
int left = 0, right = arr.length - 1;

while (left < right) {
    if (condition) {
        // return result
    } else if (moveLeft) {
        left++;
    } else {
        right--;
    }
}
```

👉 **Time Complexity:** O(n)
👉 **Space Complexity:** O(1)

---

### 5. Easy example + walkthrough

**Problem:**
Find if a sorted array has two numbers that sum to target.

**Input:**
`arr = [1, 2, 4, 6, 8], target = 10`

#### Code (Python)

```python
def has_pair(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        s = arr[left] + arr[right]
        
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1
            
    return False
```

#### Walkthrough

* left = 1, right = 8 → sum = 9 → too small → move left
* left = 2, right = 8 → sum = 10 → ✅ found

---

### 6. Common mistakes beginners make

* ❌ Using it on **unsorted arrays** (without sorting first)
* ❌ Moving the wrong pointer (logic mismatch)
* ❌ Forgetting `left < right` condition → infinite loop
* ❌ Not understanding **why pointers move** (core logic)
* ❌ Sorting when indices matter (loses original positions)

---

🔥 **clean, interview-focused list of Two Pointer problems**, grouped from easy → advanced so you can build intuition step-by-step.
---


## 🔹 Easy (Foundation)

1. **Two Sum II (Sorted Array)**
   → Find pair with given sum
   👉 Core idea: left + right comparison

2. **Remove Duplicates from Sorted Array**
   → Keep only unique elements
   👉 One pointer writes, one scans

3. **Valid Palindrome**
   → Check if string reads same both ways
   👉 Compare characters from both ends

4. **Reverse a String**
   → In-place swap using two pointers

---

## 🔹 Medium (Most Important for Interviews)

5. **3Sum**
   → Find triplets = target (usually 0)
   👉 Sort + fix one element + two pointers
   👉 TC: O(n²)

6. **Container With Most Water**
   → Max area between lines
   👉 Move pointer with smaller height

7. **Remove Element (In-place)**
   → Shift valid elements forward

8. **Squares of Sorted Array**
   → Return sorted squares
   👉 Compare absolute values from ends

9. **Subarray with Given Sum (Sliding Window variant)**
   → Continuous sum = target
   👉 Expanding & shrinking window

---

## 🔹 Hard / Advanced Patterns

10. **Trapping Rain Water**
    → Store water between heights
    👉 Two pointers + max tracking

11. **Minimum Window Substring**
    → Smallest substring containing all chars
    👉 Sliding window (very important)

12. **Longest Substring Without Repeating Characters**
    → No duplicates allowed
    👉 Hash + sliding window

13. **4Sum / K-Sum**
    → Extension of 3Sum
    👉 Recursion + two pointers

---

## 🔥 Must-Do Set (High ROI)

If you want efficiency, prioritize:

* Two Sum II
* 3Sum
* Container With Most Water
* Valid Palindrome
* Trapping Rain Water
* Longest Substring Without Repeating Characters

---

## 🧠 Pattern Summary (Very Important)

| Problem Type  | Pointer Movement Logic |
| ------------- | ---------------------- |
| Sum too small | left++                 |
| Sum too large | right--                |
| Need max/min  | move limiting factor   |
| Duplicates    | skip or overwrite      |
| Substring     | use sliding window     |

---

## ⚡ Pro Tip (Interview Insight)

Two pointer problems are not about code — they’re about **decision logic of pointer movement**.
If you can justify *why left or right moves*, you’ve solved the problem.



