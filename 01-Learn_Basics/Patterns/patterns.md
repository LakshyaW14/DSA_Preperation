
---

# 📌 Pattern Printing — Concepts & Previews

---

## 🔹 1. Square Pattern

**Concept:** Same number of rows and columns

```
*****
*****
*****
*****
*****
```

---

## 🔹 2. Right Triangle (Stars)

**Concept:** Columns increase with row

```
*
**
***
****
*****
```

---

## 🔹 3. Triangle of Numbers

**Concept:** Print numbers from `1 → row`

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

## 🔹 4. Same Number Triangle

**Concept:** Print row number repeatedly

```
1
22
333
4444
55555
```

---

## 🔹 5. Inverted Triangle

**Concept:** Reverse of increasing triangle

```
*****
****
***
**
*
```

---

## 🔹 6. Centered Triangle (Pyramid)

**Concept:** Spaces decrease, stars increase

```
    *
   ***
  *****
 *******
*********
```

---

## 🔹 7. Inverted Pyramid

**Concept:** Opposite of centered triangle

```
*********
 *******
  *****
   ***
    *
```

---

## 🔹 8. Diamond Pattern

**Concept:** Pyramid + inverted pyramid

```
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
```

---

## 🔹 9. Binary Pattern

**Concept:** Alternate 0 and 1

```
1
01
101
0101
10101
```

---

## 🔹 10. Number Crown

**Concept:** Increasing + spaces + decreasing

```
1--------1
12------21
123----321
1234--4321
1234554321
```

---

## 🔹 11. Continuous Numbers

**Concept:** Maintain global counter

```
1
23
456
78910
1112131415
```

---

## 🔹 12. Alphabet Triangle

**Concept:** Use ASCII progression

```
A
AB
ABC
ABCD
ABCDE
```

---

## 🔹 13. Same Row Alphabet

**Concept:** Same character per row

```
A
BB
CCC
DDDD
EEEEE
```

---

## 🔹 14. Centered Alphabet Pattern

**Concept:** Symmetry + alphabets

```
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
```

---

## 🔹 15. Butterfly Pattern

**Concept:** Mirror + spacing

```
*****     *****
****       ****
***         ***
**           **
*             *
*             *
**           **
***         ***
****       ****
*****     *****
```

---

## 🔹 16. Hollow Square

**Concept:** Print only borders

```
*****
*   *
*   *
*   *
*****
```

---

## 🔹 17. Concentric Square

**Concept:** Layers (distance-based)

```
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
```

---

# 🧠 Core Pattern Logic (Must Remember)

### 1. Row–Column Thinking

* Outer loop → rows
* Inner loop → columns

---

### 2. 3 Building Blocks

Every pattern is made of:

* **Stars / numbers / characters**
* **Spaces**
* **Symmetry (optional)**

---

### 3. Most Important Formulas

* **Stars in pyramid:**

  ```
  2*i - 1
  ```

* **Spaces in pyramid:**

  ```
  n - i
  ```

* **Mirror patterns:**

  ```
  row = min(i, total_rows - i + 1)
  ```

---

# 🎯 Final Intuition

> “Every pattern = controlling **rows**, **columns**, and **what to print at each position**.”

---

