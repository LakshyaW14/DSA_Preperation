# 👉 Topological Sort -> 

---

### 1. Simple definition (one sentence)

A technique to **order nodes of a Directed Acyclic Graph (DAG) such that every node appears before its dependent nodes**.

---

### 2. Real-world analogy

Think of **course prerequisites**—you must complete course A before course B, so the order must respect dependencies.

---

### 3. When to use it (pattern/situation)

Use this when you see:

* **Dependencies / ordering problems**
* **Directed graph (DAG)**
* Keywords like:

  * “prerequisite”
  * “order of tasks”
  * “dependency resolution”
  * “schedule”

👉 Important:

* Works only for **DAG (no cycles)**
* If cycle exists → no valid ordering

---

### 4. Basic code template (Kahn’s Algorithm - BFS)

#### Python

```python id="9i5mql"
from collections import deque, defaultdict

def topo_sort(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n
    
    # build graph
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    
    queue = deque()
    
    # push nodes with 0 indegree
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    return order if len(order) == n else []
```

#### Java

```java id="pswq6d"
Queue<Integer> queue = new LinkedList<>();
int[] indegree = new int[n];

// build graph...

for (int i = 0; i < n; i++) {
    if (indegree[i] == 0) queue.offer(i);
}

List<Integer> order = new ArrayList<>();

while (!queue.isEmpty()) {
    int node = queue.poll();
    order.add(node);

    for (int nei : graph[node]) {
        indegree[nei]--;
        if (indegree[nei] == 0) {
            queue.offer(nei);
        }
    }
}
```

👉 **Time Complexity:** O(V + E)
👉 **Space Complexity:** O(V + E)

---

### 5. Easy example + walkthrough

**Input:**
`n = 4`
`edges = [[0,1],[1,2],[2,3]]`

#### Steps

* indegree = [0,1,1,1]
* queue = [0]

Process:

* remove 0 → add 1
* remove 1 → add 2
* remove 2 → add 3

#### Output

`[0,1,2,3]`

---

### 6. Common mistakes beginners make

* ❌ Applying on **undirected graph**
* ❌ Not checking for cycle (order size < n)
* ❌ Wrong indegree calculation
* ❌ Forgetting to push 0-indegree nodes
* ❌ Confusing BFS with DFS version

---

## 🔥 Key Insight

👉 Topological Sort = **BFS (or DFS) + dependency resolution**

---

## 🔹 Must-Do Problems

* Course Schedule ⭐⭐
* Course Schedule II ⭐⭐⭐
* Alien Dictionary ⭐⭐⭐
* Minimum Height Trees

---

## ⚡ Pro Insight

If problem says:
👉 **“Find order” + “dependencies exist”**
→ It’s almost always **Topological Sort**

---

# Problem statement 

## 🔹 Easy (Foundation)

1. **Course Schedule** ⭐⭐
   → Check if all courses can be finished (cycle detection)

2. **Course Schedule II** ⭐⭐⭐
   → Return valid ordering of courses

---

## 🔹 Medium (Core Interview Level)

3. **Alien Dictionary** ⭐⭐⭐
   → Derive character order from sorted words

4. **Minimum Height Trees** ⭐⭐
   → Trim leaves layer by layer (BFS topo idea)

5. **Parallel Courses**
   → Minimum time to finish all courses

---

## 🔹 Hard / Advanced

6. **Sequence Reconstruction** ⭐⭐⭐
   → Check if unique sequence exists

7. **All Topological Sorts of a Graph**
   → Generate all valid orderings

---

## 🔥 Must-Do (High ROI)

Focus on these:

* Course Schedule
* Course Schedule II
* Alien Dictionary ⭐⭐⭐
* Minimum Height Trees

---

## 🧠 Pattern Recognition Cheat Sheet

| Problem Type              | Trick              |
| ------------------------- | ------------------ |
| Feasibility (can finish?) | detect cycle       |
| Ordering                  | Kahn’s BFS         |
| Unique order              | check queue size   |
| Character order           | graph from strings |
| Multi-level tasks         | level-based BFS    |

---

## ⚡ Pro Insight

Topological Sort problems revolve around one idea:
👉 **Remove nodes with 0 indegree repeatedly**

If at any point no such node exists → **cycle detected**

---
