# 🔥 Sliding Window (Two Pointer Advanced)



### 1. Simple definition (one sentence)

A technique where a **window (subarray/substring) expands and shrinks dynamically to process contiguous elements efficiently in O(n)**.

---

### 2. Real-world analogy

Think of a **camera frame sliding over a scene**—you expand the frame to capture more, and shrink it to remove unnecessary parts while maintaining a condition.

---

### 3. When to use it (pattern/situation)

Use sliding window when you see:

* **Subarray / substring problems**
* **Contiguous elements only**
* Keywords like:

  * “longest / smallest substring”
  * “at most / exactly k”
  * “sum equals target”
  * “without repeating characters”

👉 Two types:

* **Fixed window** → size `k` (e.g., max sum of size k)
* **Variable window** → grows & shrinks based on condition

---

### 4. Basic code template

#### Python (Variable Window)

```python
def sliding_window(arr):
    left = 0
    result = 0
    
    for right in range(len(arr)):
        # expand window
        add(arr[right])
        
        # shrink window if invalid
        while not valid_condition:
            remove(arr[left])
            left += 1
        
        # update answer
        result = max(result, window_value)
    
    return result
```

#### Java

```java
int left = 0;

for (int right = 0; right < arr.length; right++) {
    // expand window
    
    while (condition_not_valid) {
        // shrink window
        left++;
    }
    
    // update result
}
```

👉 **Time Complexity:** O(n)
👉 **Space Complexity:** O(k) or O(1) (depends on hashmap/set)

---

### 5. Easy example + walkthrough

**Problem:**
Longest substring without repeating characters

**Input:** `"abcabcbb"`
**Output:** `3` ("abc")

#### Code (Python)

```python
def longest_unique(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

#### Walkthrough

* Window expands: `"a" → "ab" → "abc"` ✅
* Next `"a"` repeats → shrink from left
* Continue…
* Max length found = **3**

---

### 6. Common mistakes beginners make

* ❌ Not shrinking window properly → wrong answers
* ❌ Using sliding window on **non-contiguous problems**
* ❌ Forgetting `while` loop (using `if` instead)
* ❌ Not updating answer at correct place
* ❌ Confusing fixed vs variable window

---

## 🔥 Key Insight (Very Important)

Sliding window =
👉 **Expand (right++)** to explore
👉 **Shrink (left++)** to maintain condition

---

# 🔥focused set of Sliding Window questions (clean, interview-relevant :

---

## 🔹 Easy (Build Basics)

1. **Maximum Sum Subarray of Size K**
   👉 Fixed window
   → Find max sum of any subarray of size `k`

2. **First Negative Number in Every Window of Size K**
   👉 Fixed window + queue

3. **Count Occurrences of Anagrams**
   👉 Fixed window + hashmap

---

## 🔹 Medium (Core Interview Level)

4. **Longest Substring Without Repeating Characters** ⭐
   👉 Variable window + set

5. **Longest Substring with At Most K Distinct Characters**
   👉 Variable window + hashmap

6. **Minimum Size Subarray Sum**
   👉 Smallest subarray with sum ≥ target

7. **Permutation in String**
   👉 Check if permutation exists in string

---

## 🔹 Hard (High Value Problems)

8. **Minimum Window Substring** ⭐⭐
   👉 Most important sliding window problem

9. **Longest Repeating Character Replacement**
   👉 Replace k chars to make longest same char substring

10. **Subarrays with Exactly K Distinct Integers**
    👉 Trick: at most(k) – at most(k-1)

---

## 🔥 Must-Do (High ROI shortlist)

If you're serious about interviews, do these first:

* Maximum Sum Subarray of Size K
* Longest Substring Without Repeating Characters
* Minimum Size Subarray Sum
* Minimum Window Substring
* Longest Repeating Character Replacement

---

## 🧠 Pattern Recognition Cheat Sheet

| Pattern       | Approach             |
| ------------- | -------------------- |
| Fixed size k  | Expand + remove left |
| No duplicates | Use set              |
| K distinct    | Use hashmap          |
| Min length    | Shrink aggressively  |
| Max length    | Expand more          |

---

## ⚡ Pro Insight

Sliding window problems are solved by answering one question repeatedly:
👉 **“When should I shrink the window?”**

If you master that, you master the pattern.

---
