# 🔥 Merge Intervals

---

### 1. Simple definition (one sentence)

A technique where **overlapping intervals are combined into a single interval after sorting**.

---

### 2. Real-world analogy

Think of **meeting time slots**—if two meetings overlap, you merge them into one continuous block.

---

### 3. When to use it (pattern/situation)

Use this when you see:

* **Intervals (start, end) format**
* **Overlapping ranges**
* Keywords like:

  * “merge intervals”
  * “overlapping”
  * “schedule”
  * “ranges”

👉 Key step: **Sort by start time first**

---

### 4. Basic code template

#### Python

```python id="1r8o0v"
def merge_intervals(intervals):
    intervals.sort()  # sort by start
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged
```

#### Java

```java id="z1y8cb"
Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

List<int[]> merged = new ArrayList<>();

for (int[] interval : intervals) {
    if (merged.isEmpty() || merged.get(merged.size()-1)[1] < interval[0]) {
        merged.add(interval);
    } else {
        merged.get(merged.size()-1)[1] = Math.max(
            merged.get(merged.size()-1)[1],
            interval[1]
        );
    }
}
```

👉 **Time Complexity:** O(n log n) (sorting)
👉 **Space Complexity:** O(n)

---

### 5. Easy example + walkthrough

**Input:**
`[[1,3],[2,6],[8,10],[15,18]]`

#### Steps

1. Sort → already sorted
2. Start merging:

* [1,3] + [2,6] → overlap → merge → [1,6]
* [8,10] → no overlap → add
* [15,18] → no overlap → add

#### Output

`[[1,6],[8,10],[15,18]]`

---

### 6. Common mistakes beginners make

* ❌ Forgetting to **sort first**
* ❌ Using wrong overlap condition
  👉 Correct: `prev_end >= current_start`
* ❌ Modifying original intervals incorrectly
* ❌ Not handling empty input
* ❌ Confusing with two-pointer (this is greedy + sorting)

---

## 🔥 Key Insight

👉 **Sort + Compare with last merged interval** = whole problem

---
Here’s a **clean, interview-focused list of Interval (Merge Intervals pattern) problems**:

---

## 🔹 Easy (Foundation)

1. **Merge Intervals** ⭐
   → Combine overlapping intervals

2. **Meeting Rooms**
   → Check if a person can attend all meetings
   👉 Detect overlap

---

## 🔹 Medium (Core Interview Level)

3. **Insert Interval** ⭐⭐
   → Insert new interval and merge if needed

4. **Non-overlapping Intervals** ⭐⭐
   → Remove minimum intervals to avoid overlap
   👉 Greedy (end time sorting)

5. **Meeting Rooms II** ⭐⭐
   → Minimum number of rooms required
   👉 Heap / line sweep

6. **Interval List Intersections**
   → Find intersections between two lists

---

## 🔹 Hard / Advanced

7. **Employee Free Time** ⭐⭐
   → Find common free intervals

8. **Maximum Number of Events That Can Be Attended**
   → Greedy + sorting + heap

---

## 🔥 Must-Do (High ROI)

Focus on these:

* Merge Intervals
* Insert Interval
* Non-overlapping Intervals
* Meeting Rooms II

---

## 🧠 Pattern Recognition Cheat Sheet

| Pattern             | Approach                   |
| ------------------- | -------------------------- |
| Merge overlaps      | Sort + compare with last   |
| Check conflict      | Compare adjacent intervals |
| Min removals        | Greedy (sort by end)       |
| Resource allocation | Heap / priority queue      |
| Intersections       | Two pointers               |

---

## ⚡ Pro Insight

Most interval problems reduce to one core idea:
👉 **Sort intervals (by start or end) → then apply greedy logic**

---

If you want, I can:

* Solve **Insert Interval step-by-step (very important)**
* OR give you a **complete DSA pattern roadmap (like what to study next after this)**
