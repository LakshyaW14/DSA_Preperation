# 🔥 Tree DFS (Depth-First Search) -> 

---

### 1. Simple definition (one sentence)

A traversal technique where **we explore as deep as possible along a branch before backtracking**.

---

### 2. Real-world analogy

Think of exploring a **maze**—you go down one path fully, and if it fails, you backtrack and try another path.

---

### 3. When to use it (pattern/situation)

Use DFS when you see:

* **Path-related problems**
* **Tree structure recursion**
* Problems like:

  * Max depth / height
  * Path sum
  * Validate tree properties
* Keywords:

  * “path”
  * “all paths”
  * “sum”
  * “depth”

👉 Types of DFS:

* **Preorder** → root → left → right
* **Inorder** → left → root → right
* **Postorder** → left → right → root

---

### 4. Basic code template

#### Python (Recursive)

```python id="b2kq9m"
def dfs(root):
    if not root:
        return
    
    # process node (preorder)
    print(root.val)
    
    dfs(root.left)
    dfs(root.right)
```

#### Java

```java id="n7t1xq"
void dfs(TreeNode root) {
    if (root == null) return;

    System.out.println(root.val);

    dfs(root.left);
    dfs(root.right);
}
```

👉 **Time Complexity:** O(n)
👉 **Space Complexity:** O(h) (recursion stack, h = height)

---

### 5. Easy example + walkthrough

**Tree:**

```
       1
     /   \
    2     3
   / \     
  4   5    
```

#### Preorder DFS

* Visit 1
* Go left → 2
* Go left → 4
* Backtrack → 5
* Go right → 3

#### Output

`1 → 2 → 4 → 5 → 3`

---

### 6. Common mistakes beginners make

* ❌ Forgetting base case (`if not root`)
* ❌ Mixing up preorder/inorder/postorder
* ❌ Not understanding backtracking
* ❌ Using DFS when BFS is better (shortest path cases)
* ❌ Stack overflow on deep trees (rare but possible)

---

## 🔥 Key Insight

👉 DFS = **Go deep → then backtrack**

---

## 🔹 Must-Do Problems

* Maximum Depth of Binary Tree ⭐
* Path Sum ⭐
* Validate Binary Search Tree ⭐⭐
* Lowest Common Ancestor ⭐⭐

---

# Problem statements

## 🔹 Easy (Foundation)

1. **Maximum Depth of Binary Tree** ⭐
   → Classic recursion

2. **Same Tree**
   → Compare two trees

3. **Invert Binary Tree** ⭐
   → Swap left & right recursively

---

## 🔹 Medium (Core Interview Level)

4. **Path Sum** ⭐⭐
   → Check if root-to-leaf path equals target

5. **Path Sum II** ⭐⭐
   → Return all valid paths

6. **Diameter of Binary Tree** ⭐⭐
   → Longest path between any two nodes

7. **Balanced Binary Tree** ⭐⭐
   → Check height difference

8. **Lowest Common Ancestor (LCA)** ⭐⭐⭐
   → Find common parent

---

## 🔹 Hard / Advanced

9. **Binary Tree Maximum Path Sum** ⭐⭐⭐
   → Path can start/end anywhere

10. **Serialize and Deserialize Binary Tree (DFS)**
    → Preorder + null markers

---

## 🔥 Must-Do (High ROI)

Focus on these:

* Maximum Depth
* Path Sum
* Diameter of Binary Tree
* Balanced Binary Tree
* Lowest Common Ancestor

---

## 🧠 Pattern Recognition Cheat Sheet

| Problem Type | DFS Trick                        |
| ------------ | -------------------------------- |
| Depth/height | return 1 + max(left, right)      |
| Path sum     | subtract target while going down |
| All paths    | backtracking                     |
| Diameter     | track global max                 |
| LCA          | return node if found             |

---

## ⚡ Pro Insight

DFS problems usually follow one pattern:
👉 **“What should this function return to its parent?”**

If you answer that clearly, recursion becomes easy.

---

