# Easy Problem Statements on Array

## 01- Remove Duplicates from Sorted Array ( In-Place ):
**Problem Statement:** Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

* Approach -> Instead of using a set to store the unique elements, we can implement a two pointer strategy to optimize the space. Since the array is sorted, we know that all the duplicate values will be adjacent to each other.

---

## 02- Check if the array is Sorted and rotated:
We need to find whether the given integer array nums could represent a sorted array that has been rotated some number of times. A sorted array is defined as one arranged in non-decreasing order, meaning each element is less than or equal to the next. A rotation involves shifting a contiguous block of elements to the back of the array, preserving the relative order of all elements.

* For example, [3, 4, 5, 1, 2] is a rotated version of the sorted array [1, 2, 3, 4, 5]. On the other hand, [3, 4, 2, 1, 5] is not a valid rotation of any sorted array because the order of elements is not preserved.