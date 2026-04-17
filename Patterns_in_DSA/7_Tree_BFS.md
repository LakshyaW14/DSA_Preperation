# 🔥 07 -> Tree BFS 

---

### 1. Simple definition (one sentence)

A traversal technique where **nodes of a tree are visited level by level using a queue (FIFO)**.

---

### 2. Real-world analogy

Think of a **queue at a ticket counter**—people are served in the order they arrive (first come, first served), just like nodes at each level.

---

### 3. When to use it (pattern/situation)

Use BFS when you see:

* **Level-wise traversal**
* **Shortest path in unweighted tree**
* Problems like:

  * Level order traversal
  * Minimum depth
  * Zigzag traversal
* Keywords:

  * “level”
  * “closest / shortest”
  * “layer by layer”

---

### 4. Basic code template

#### Python

```python id="u8k2ps"
from collections import deque

def bfs(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

#### Java

```java id="7q1mzc"
Queue<TreeNode> queue = new LinkedList<>();
queue.offer(root);

while (!queue.isEmpty()) {
    TreeNode node = queue.poll();
    
    System.out.println(node.val);
    
    if (node.left != null) queue.offer(node.left);
    if (node.right != null) queue.offer(node.right);
}
```

👉 **Time Complexity:** O(n)
👉 **Space Complexity:** O(n) (queue)

---

### 5. Easy example + walkthrough

**Tree:**

```
       1
     /   \
    2     3
   / \   /
  4   5 6
```

#### Steps

* Start → queue = [1]
* Visit 1 → add 2,3
* Visit 2 → add 4,5
* Visit 3 → add 6
* Continue…

#### Output

`1 → 2 → 3 → 4 → 5 → 6`

---

### 6. Common mistakes beginners make

* ❌ Using stack instead of queue (becomes DFS)
* ❌ Forgetting to check `root == None`
* ❌ Not pushing children correctly
* ❌ Confusing BFS with DFS
* ❌ Not handling level-based logic properly

---

## 🔥 Key Insight

👉 BFS = **Queue + Level Order Traversal**

---

## 🔹 Must-Do Problems

* Binary Tree Level Order Traversal ⭐
* Minimum Depth of Binary Tree ⭐
* Binary Tree Zigzag Level Order ⭐⭐
* Average of Levels in Binary Tree

---
# problem Statements 

## 🔹 Easy (Foundation)

1. **Binary Tree Level Order Traversal** ⭐
   → Return nodes level by level

2. **Average of Levels in Binary Tree**
   → Compute average per level

3. **Minimum Depth of Binary Tree** ⭐
   → First leaf reached = answer (BFS advantage)

---

## 🔹 Medium (Core Interview Level)

4. **Binary Tree Zigzag Level Order Traversal** ⭐⭐
   → Alternate left-right order

5. **Binary Tree Right Side View** ⭐⭐
   → Last node of each level

6. **Binary Tree Level Order Traversal II**
   → Bottom-up level order

7. **Populating Next Right Pointers** ⭐⭐
   → Connect nodes at same level

---

## 🔹 Hard / Advanced

8. **Serialize and Deserialize Binary Tree** ⭐⭐⭐
   → BFS + structure encoding

9. **Vertical Order Traversal**
   → BFS + column tracking

10. **Maximum Width of Binary Tree**
    → BFS + indexing trick

---

## 🔥 Must-Do (High ROI)

Focus on these:

* Level Order Traversal
* Minimum Depth
* Zigzag Traversal
* Right Side View
* Serialize & Deserialize ⭐

---

## 🧠 Pattern Recognition Cheat Sheet

| Pattern            | Trick                            |
| ------------------ | -------------------------------- |
| Level traversal    | Queue + loop size                |
| Level-based answer | Use `for _ in range(len(queue))` |
| First/last node    | Track start/end of level         |
| Zigzag             | Reverse or use deque             |
| Shortest path      | BFS guarantees minimum           |

---

## ⚡ Pro Insight

Almost every BFS tree problem reduces to:
👉 **Process nodes level-by-level using queue size**

---
