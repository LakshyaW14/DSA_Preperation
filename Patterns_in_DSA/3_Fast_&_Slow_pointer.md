# 🔥 Fast & Slow Pointer (Floyd’s Cycle Detection

---

### 1. Simple definition (one sentence)

A technique where **two pointers move at different speeds to detect cycles or find middle positions efficiently in O(n)**.

---

### 2. Real-world analogy

Imagine two runners on a circular track:
one runs **slow (1 step)**, the other **fast (2 steps)**—if there’s a loop, the fast runner will eventually meet the slow one.

---

### 3. When to use it (pattern/situation)

Use this when you see:

* **Linked list cycle detection**
* **Find middle of linked list**
* **Detect loop in array (cycle problems)**
* Keywords like:

  * “cycle”
  * “loop exists?”
  * “find middle node”
  * “find start of cycle”

---

### 4. Basic code template

#### Python

```python id="zv2c2g"
def has_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps
        
        if slow == fast:
            return True
    
    return False
```

#### Java

```java id="bndw0r"
ListNode slow = head;
ListNode fast = head;

while (fast != null && fast.next != null) {
    slow = slow.next;
    fast = fast.next.next;
    
    if (slow == fast) {
        return true;
    }
}
return false;
```

👉 **Time Complexity:** O(n)
👉 **Space Complexity:** O(1)

---

### 5. Easy example + walkthrough

**Problem:**
Detect cycle in linked list

#### Idea

* If no cycle → fast reaches `null`
* If cycle exists → fast meets slow

#### Walkthrough

List: `1 → 2 → 3 → 4 → 5 → 3 (cycle)`

* Step 1: slow=2, fast=3
* Step 2: slow=3, fast=5
* Step 3: slow=4, fast=4 ✅ (meet → cycle exists)

---

### 6. Common mistakes beginners make

* ❌ Forgetting `fast and fast.next` check → runtime error
* ❌ Moving both pointers at same speed (loses purpose)
* ❌ Confusing with normal two pointers (this is speed-based, not position-based)
* ❌ Not understanding **why they meet in a cycle**
* ❌ Using extra space when not needed

---

## 🔥 Key Insight

Fast & Slow pointer works because:
👉 In a cycle, **relative speed = 1 step**, so they must meet

---

# clean, interview-focused list of Fast & Slow Pointer (Floyd’s Algorithm) problems

---

## 🔹 Easy (Core Understanding)

1. **Detect Cycle in Linked List** ⭐
   👉 Return `True/False` if cycle exists

2. **Find Middle of Linked List** ⭐
   👉 Slow stops at middle when fast reaches end

3. **Happy Number**
   👉 Treat number transformation as a cycle

---

## 🔹 Medium (Most Important)

4. **Linked List Cycle II** ⭐⭐
   👉 Find the **starting node of the cycle**

5. **Palindrome Linked List**
   👉 Find middle → reverse second half → compare

6. **Reorder List**
   👉 Split using middle → merge alternately

---

## 🔹 Hard / Conceptual

7. **Find Duplicate Number (Array)** ⭐⭐
   👉 Treat array as a cycle (very important trick)

8. **Circular Array Loop**
   👉 Detect loop with direction constraints

---

## 🔥 Must-Do (High ROI)

Focus on these:

* Detect Cycle in Linked List
* Find Middle of Linked List
* Linked List Cycle II
* Find Duplicate Number

---

## 🧠 Pattern Recognition Cheat Sheet

| Problem Type       | Why Fast-Slow Works        |
| ------------------ | -------------------------- |
| Cycle detection    | Fast catches slow          |
| Middle element     | Fast moves twice as fast   |
| Cycle start        | Mathematical meeting point |
| Duplicate in array | Index mapping creates loop |

---

## ⚡ Pro Insight (Very Important)

Fast & slow pointer is not just for linked lists:
👉 Any problem that can be modeled as a **cycle/loop** can use this trick.

---
