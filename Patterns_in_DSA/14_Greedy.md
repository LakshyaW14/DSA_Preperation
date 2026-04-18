# Greedy Algorithm -> 

---

### 1. Simple definition (one sentence)

A technique where **we make the best local (immediate) choice at each step hoping it leads to a globally optimal solution**.

---

### 2. Real-world analogy

Think of **picking coins to make change**—you always pick the largest coin first to minimize the number of coins.

---

### 3. When to use it (pattern/situation)

Use greedy when you see:

* **Optimization problems (min/max)**
* **Sorting + decision making**
* Keywords like:

  * “maximum profit”
  * “minimum cost”
  * “minimum number of steps”
  * “activity selection”

👉 Common patterns:

* Interval scheduling
* Sorting by some criteria
* Choosing locally optimal option

⚠️ Important:
Greedy works only when **local optimal → global optimal** (not always true)

---

### 4. Basic code template

#### Python

```python id="4y6q2l"
def greedy(arr):
    arr.sort()  # often needed
    
    result = 0
    
    for item in arr:
        if condition:
            result += value
    
    return result
```

#### Java

```java id="k3m8tz"
Arrays.sort(arr);

int result = 0;

for (int item : arr) {
    if (condition) {
        result += value;
    }
}
```

👉 **Time Complexity:** Usually O(n log n) (due to sorting)
👉 **Space Complexity:** O(1)

---

### 5. Easy example + walkthrough

**Problem:** Activity Selection
Max number of non-overlapping activities

**Input:**
`[(1,3), (2,4), (3,5), (6,7)]`

#### Steps

1. Sort by end time → `[(1,3), (2,4), (3,5), (6,7)]`
2. Pick (1,3)
3. Skip (2,4) (overlap)
4. Pick (3,5)
5. Pick (6,7)

#### Output

`3 activities`

---

### 6. Common mistakes beginners make

* ❌ Using greedy when DP is required
* ❌ Not sorting properly (wrong criteria)
* ❌ Assuming greedy always works
* ❌ Not proving correctness
* ❌ Ignoring edge cases

---

## 🔥 Key Insight

👉 Greedy =
**Make best choice now, don’t reconsider later**

---

## 🔹 Must-Do Problems

* Activity Selection ⭐
* Fractional Knapsack ⭐⭐
* Jump Game ⭐⭐
* Gas Station ⭐⭐⭐
* Non-overlapping Intervals ⭐⭐

---

## ⚡ Pro Insight

If problem asks for **global optimal**:
👉 First try greedy → if fails → switch to DP

---

# Problem Statement 



## 🔹 Easy (Foundation)

1. **Assign Cookies** ⭐
   → Match greed factor with cookie size

2. **Best Time to Buy and Sell Stock (I)** ⭐
   → Max profit with one transaction

3. **Valid Parenthesis String (Greedy approach)**
   → Track min/max balance

---

## 🔹 Medium (Core Interview Level)

4. **Jump Game** ⭐⭐
   → Can you reach the end?

5. **Jump Game II** ⭐⭐⭐
   → Minimum jumps

6. **Gas Station** ⭐⭐⭐
   → Circular route feasibility

7. **Non-overlapping Intervals** ⭐⭐
   → Remove minimum overlaps

8. **Partition Labels** ⭐⭐
   → Divide string into segments

---

## 🔹 Hard / Advanced

9. **Candy** ⭐⭐⭐
   → Distribute candies with constraints

10. **Task Scheduler** ⭐⭐⭐
    → Minimum time with cooldown

11. **Minimum Number of Arrows to Burst Balloons** ⭐⭐
    → Interval greedy

---

## 🔥 Must-Do (High ROI)

Focus on these:

* Jump Game
* Jump Game II
* Gas Station ⭐⭐⭐
* Non-overlapping Intervals
* Task Scheduler ⭐⭐⭐

---

## 🧠 Pattern Recognition Cheat Sheet

| Pattern             | Greedy Choice           |
| ------------------- | ----------------------- |
| Intervals           | sort by end             |
| Reachability        | track max reach         |
| Min steps           | expand range            |
| Circular problems   | reset when negative     |
| Resource allocation | assign smallest/largest |

---

## ⚡ Pro Insight

Greedy works when:
👉 **Taking the best choice now never hurts future choices**

If that condition breaks → switch to DP.

---
