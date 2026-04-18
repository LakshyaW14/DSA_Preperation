# 🔥 Subset / Backtracking -> 

---

### 1. Simple definition (one sentence)

A technique where **we explore all possible combinations by making choices and undoing them (backtracking)**.

---

### 2. Real-world analogy

Think of **trying all outfit combinations**—you pick one item, try options, and if it doesn’t work, you go back and try another.

---

### 3. When to use it (pattern/situation)

Use this when you see:

* **All combinations / subsets / permutations**
* **Decision trees**
* Keywords like:

  * “all possible”
  * “combinations”
  * “subsets”
  * “generate”

👉 Core idea:

* Choose → Explore → Undo (backtrack)

---

### 4. Basic code template

#### Python

```python
def backtrack(start, path):
    result.append(path[:])
    
    for i in range(start, len(nums)):
        path.append(nums[i])      # choose
        backtrack(i + 1, path)   # explore
        path.pop()               # undo

result = []
nums = [1,2,3]
backtrack(0, [])
```

#### Java

```java
void backtrack(int start, List<Integer> path) {
    result.add(new ArrayList<>(path));
    
    for (int i = start; i < nums.length; i++) {
        path.add(nums[i]);             // choose
        backtrack(i + 1, path);       // explore
        path.remove(path.size() - 1); // undo
    }
}
```

👉 **Time Complexity:** O(2ⁿ) (for subsets)
👉 **Space Complexity:** O(n) (recursion stack)

---

### 5. Easy example + walkthrough

**Problem:** Generate all subsets of `[1,2]`

#### Process

* Start → `[]`
* Pick 1 → `[1]`

  * Pick 2 → `[1,2]`
  * Backtrack → `[1]`
* Backtrack → `[]`
* Pick 2 → `[2]`

#### Output

`[], [1], [1,2], [2]`

---

### 6. Common mistakes beginners make

* ❌ Forgetting to **copy path (`path[:]`)**
* ❌ Not doing `pop()` → wrong results
* ❌ Wrong base condition
* ❌ Confusing subset vs permutation logic
* ❌ Modifying same list reference

---

## 🔥 Key Insight

👉 Backtracking = **DFS on decision tree**

---

## 🔹 Must-Do Problems

* Subsets ⭐
* Subsets II (with duplicates) ⭐⭐
* Permutations ⭐⭐
* Combination Sum ⭐⭐⭐
* N-Queens ⭐⭐⭐

---

## ⚡ Pro Insight

If problem says **“return all possible…”**,
👉 90% chance it’s **backtracking**

---
# problem statement 

## 🔹 Easy (Foundation)

1. **Subsets** ⭐
   → Generate all subsets (power set)

2. **Subsets II** ⭐⭐
   → Handle duplicates (skip repeated elements)

---

## 🔹 Medium (Core Interview Level)

3. **Permutations** ⭐⭐
   → All possible arrangements

4. **Permutations II** ⭐⭐⭐
   → Handle duplicates

5. **Combination Sum** ⭐⭐⭐
   → Pick elements to reach target (reuse allowed)

6. **Combination Sum II** ⭐⭐⭐
   → No reuse + duplicates present

7. **Letter Combinations of Phone Number** ⭐⭐
   → Mapping + recursion

---

## 🔹 Hard / Advanced

8. **Palindrome Partitioning** ⭐⭐⭐
   → Split string into palindrome parts

9. **N-Queens** ⭐⭐⭐
   → Place queens safely (classic backtracking)

10. **Word Search** ⭐⭐⭐
    → DFS + backtracking in grid

---

## 🔥 Must-Do (High ROI)

Focus on these:

* Subsets
* Permutations
* Combination Sum ⭐⭐⭐
* Subsets II (duplicates)
* N-Queens ⭐⭐⭐

---

## 🧠 Pattern Recognition Cheat Sheet

| Problem Type    | Trick             |
| --------------- | ----------------- |
| Subsets         | include/exclude   |
| Permutations    | use visited array |
| Combination sum | target reduce     |
| Duplicates      | sort + skip       |
| Grid problems   | DFS + backtrack   |

---

## ⚡ Pro Insight

All backtracking problems boil down to:
👉 **Decision tree + undo (backtrack)**

If you can visualize the tree, coding becomes mechanical.

---

