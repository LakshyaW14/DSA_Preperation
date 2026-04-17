# Easy Problem Statements on Array

## 01- Remove Duplicates from Sorted Array ( In-Place ):
**Problem Statement:** Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

* Approach -> Instead of using a set to store the unique elements, we can implement a two pointer strategy to optimize the space. Since the array is sorted, we know that all the duplicate values will be adjacent to each other.

---

## 02- Check if the array is Sorted and rotated:
We need to find whether the given integer array nums could represent a sorted array that has been rotated some number of times. A sorted array is defined as one arranged in non-decreasing order, meaning each element is less than or equal to the next. A rotation involves shifting a contiguous block of elements to the back of the array, preserving the relative order of all elements.

* For example, [3, 4, 5, 1, 2] is a rotated version of the sorted array [1, 2, 3, 4, 5]. On the other hand, [3, 4, 2, 1, 5] is not a valid rotation of any sorted array because the order of elements is not preserved.

---

## 03 - Rotate the array with k elements 
Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

Examples
Input : nums = [1, 2, 3, 4, 5, 6, 7], k = 2, right
Output : [6, 7, 1, 2, 3, 4, 5]
Explanation : rotate 1 step to the right: [7, 1, 2, 3, 4, 5, 6]
rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5] 

### Approach 
* Brute Force approach - use additional temp var to store the k elements 
* Optimal Approach - in place modification

---

## 04 - find the largest element in the array 
Problem Statement: Given an array, we have to find the largest element in the array.

### Approach
* Brute Force Approach - sort the array, return last element
* Optimal Approach - var max, iterate -> compare -> update -> return

---

## 05 - Find Second Smallest and Second Largest Element in an array

Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

Example 1:
Input:
 [1, 2, 4, 7, 7, 5]  
Output:
  
Second Smallest : 2  
Second Largest : 5  

---

## 06 - linear search

Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.

---

## 07 - Union of Two Sorted Array 
Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.

NOTE: Elements in the union should be in ascending order.
* optimal approach -> Two pointers 
* approach 1 -> Using Set
* approach 2 -> Using Map 

---

##  - Move zeroes to the end of the array 
Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

Examples
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0