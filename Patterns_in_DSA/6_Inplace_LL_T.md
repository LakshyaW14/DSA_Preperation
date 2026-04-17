# 🔥 06 - > In-place Linked List Reversal 

---

### 1. Simple definition (one sentence)

A technique where **we reverse a linked list by changing pointers (links) without using extra space**.

---

### 2. Real-world analogy

Think of a **train where each bogie points to the next**—you reverse the train by **changing the direction of each coupling**.

---

### 3. When to use it (pattern/situation)

Use this when:

* You see **linked list reversal**
* Problems like:

  * Reverse entire list
  * Reverse part of list (k-group, sublist)
* Keywords:

  * “reverse linked list”
  * “in-place”
  * “constant space”

---

### 4. Basic code template

#### Python

```python id="v9q3xa"
def reverse_list(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next   # store next
        curr.next = prev        # reverse link
        prev = curr             # move prev
        curr = next_node        # move curr
    
    return prev
```

#### Java

```java id="y7d2kp"
ListNode prev = null;
ListNode curr = head;

while (curr != null) {
    ListNode nextNode = curr.next;
    curr.next = prev;
    prev = curr;
    curr = nextNode;
}

return prev;
```

👉 **Time Complexity:** O(n)
👉 **Space Complexity:** O(1)

---

### 5. Easy example + walkthrough

**Input:**
`1 → 2 → 3 → 4 → 5`

#### Steps

* Start: `prev = None`, `curr = 1`

1. Reverse 1 → `1 → None`
2. Reverse 2 → `2 → 1`
3. Reverse 3 → `3 → 2 → 1`
4. Reverse 4 → `4 → 3 → 2 → 1`
5. Reverse 5 → `5 → 4 → 3 → 2 → 1`

#### Output

`5 → 4 → 3 → 2 → 1`

---

### 6. Common mistakes beginners make

* ❌ Losing reference to next node (forget `next_node`)
* ❌ Changing pointers in wrong order
* ❌ Not updating `prev` and `curr` correctly
* ❌ Returning wrong pointer (`curr` instead of `prev`)
* ❌ Confusing with array reversal

---

## 🔥 Key Insight

👉 Always follow this order:
**save next → reverse link → move pointers**

---

## 🔹 Must-Do Problems

* Reverse Linked List ⭐
* Reverse Linked List II (sublist) ⭐⭐
* Reverse Nodes in K-Group ⭐⭐⭐
* Palindrome Linked List

---

# Problem Statement

## 🔹 Easy (Foundation)

1. **Reverse Linked List** ⭐
   → Reverse entire list

2. **Reverse Linked List (Recursive)**
   → Same problem, different approach

---

## 🔹 Medium (Core Interview Level)

3. **Reverse Linked List II** ⭐⭐
   → Reverse a sublist between positions `left` and `right`

4. **Reverse Nodes in K-Group** ⭐⭐⭐
   → Reverse every group of size `k`

5. **Palindrome Linked List** ⭐⭐
   → Reverse second half + compare

6. **Reorder List** ⭐⭐
   → Split + reverse second half + merge

---

## 🔹 Advanced / Pattern Combination

7. **Rotate List**
   → Modify links after partial reversal logic

8. **Swap Nodes in Pairs**
   → Mini reversal of size 2

---

## 🔥 Must-Do (High ROI)

Focus on these:

* Reverse Linked List
* Reverse Linked List II
* Reverse Nodes in K-Group
* Palindrome Linked List

---

## 🧠 Pattern Recognition Cheat Sheet

| Problem Type     | Trick                       |
| ---------------- | --------------------------- |
| Full reversal    | Standard 3-pointer          |
| Sublist reversal | Break + reverse + reconnect |
| K-group          | Loop + reverse chunks       |
| Palindrome       | Fast-slow + reverse half    |
| Reorder          | Split + reverse + merge     |

---

## ⚡ Pro Insight

Most problems are just variations of one core operation:
👉 **Reverse a part of the list and reconnect it properly**

If you master:

* Pointer handling
* Connection logic

👉 You can solve almost all linked list problems.

---
