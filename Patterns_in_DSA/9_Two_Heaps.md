# 🔥 Two Heaps pattern -> 

---

### 1. Simple definition (one sentence)

A technique where **two heaps (max-heap + min-heap) are used together to efficiently track median or split data into two halves**.

---

### 2. Real-world analogy

Think of **balancing weights on two sides of a scale**:

* Left side → smaller half (max-heap)
* Right side → larger half (min-heap)
  You keep both sides balanced to always know the middle value.

---

### 3. When to use it (pattern/situation)

Use this when you see:

* **Median / middle element problems**
* **Stream of numbers (dynamic input)**
* Keywords like:

  * “median”
  * “kth smallest/largest”
  * “continuous data stream”

👉 Core idea:

* Max-heap → stores smaller half
* Min-heap → stores larger half
* Keep sizes balanced (difference ≤ 1)

---

### 4. Basic code template

#### Python

```python id="3v0d7n"
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # store negatives
        self.min_heap = []

    def add_num(self, num):
        heapq.heappush(self.max_heap, -num)
        
        # balance heaps
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
```

#### Java

```java id="o8s1vd"
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
PriorityQueue<Integer> minHeap = new PriorityQueue<>();

void addNum(int num) {
    maxHeap.offer(num);
    minHeap.offer(maxHeap.poll());
    
    if (minHeap.size() > maxHeap.size()) {
        maxHeap.offer(minHeap.poll());
    }
}

double findMedian() {
    if (maxHeap.size() > minHeap.size()) {
        return maxHeap.peek();
    }
    return (maxHeap.peek() + minHeap.peek()) / 2.0;
}
```

👉 **Time Complexity:**

* Insert: O(log n)
* Find median: O(1)

👉 **Space Complexity:** O(n)

---

### 5. Easy example + walkthrough

**Stream:** `1, 2, 3`

#### Steps

* Add 1 → maxHeap = [1] → median = 1
* Add 2 → balance → median = (1+2)/2 = 1.5
* Add 3 → maxHeap = [2,1], minHeap = [3] → median = 2

---

### 6. Common mistakes beginners make

* ❌ Not balancing heaps properly
* ❌ Forgetting max-heap uses negative values (Python)
* ❌ Returning wrong median formula
* ❌ Letting size difference > 1
* ❌ Mixing up which heap stores smaller/larger half

---

## 🔥 Key Insight

👉 Always maintain:

* **All elements in maxHeap ≤ all in minHeap**
* **Size difference ≤ 1**

---

## 🔹 Must-Do Problems

* Find Median from Data Stream ⭐⭐
* Sliding Window Median ⭐⭐⭐
* Find Right Interval

---

# problem Statement 

## 🔹 Easy (Concept Building)

1. **Find Median from Data Stream** ⭐⭐
   → Add numbers continuously and return median
   👉 Core Two Heaps problem

---

## 🔹 Medium (Important)

2. **Sliding Window Median** ⭐⭐⭐
   → Median for every window of size `k`
   👉 Two heaps + removal logic

3. **Find Right Interval**
   → Use heap to track next valid interval

---

## 🔹 Hard / Advanced

4. **IPO (Maximize Capital)** ⭐⭐⭐
   → Choose projects with max profit under constraints
   👉 Min-heap + max-heap combo

5. **Find K Pairs with Smallest Sums**
   → Heap-based pair generation

---

## 🔥 Must-Do (High ROI)

Focus on these:

* Find Median from Data Stream
* Sliding Window Median ⭐⭐⭐
* IPO Problem

---

## 🧠 Pattern Recognition Cheat Sheet

| Problem Type           | Heap Strategy            |
| ---------------------- | ------------------------ |
| Median                 | Max-heap + Min-heap      |
| Sliding window         | Add + remove + rebalance |
| Top k / max profit     | Max-heap                 |
| Constraints + ordering | Min-heap                 |

---

## ⚡ Pro Insight

Two heaps are mainly used when:
👉 You need **real-time median or dynamic partitioning of data**

If median is not involved → consider normal heap instead.

---
