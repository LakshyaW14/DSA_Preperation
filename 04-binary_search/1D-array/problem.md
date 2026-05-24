# Binary Search Problem Statements 

## 01 - Lower Bound 

Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

What is lower bound?
The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.
Example 1:
Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
Result: 1
Explanation: Index 1 is the smallest index such that arr[1] >= x.

---

## 02 - Upper Bound 

Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.

What is Upper Bound?
The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than the given key i.e. x.

The upper bound is the smallest index, ind, where arr[ind] > x.

Examples
Example 1:
Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
Result: 3
Explanation: Index 3 is the smallest index such that arr[3] > x.

---

## 03 - Binary Search x 

Problem statement: You are given a sorted array of integers and a target, your task is to search for the target in the given array. Assume the given array does not contain any duplicate numbers.

---

## 04 - Search Insert Position

Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

Examples
Example 1:
Input Format: arr[] = {1,2,4,7}, x = 6
Result: 3
Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

---

## 05 - Floor and Ceil in Sorted Array

Problem Statement: ou're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1]. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x

Examples

Example 1:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
Result: 4 7
Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

---

## 06 -> Last occurrence in a sorted array

Problem Statement: Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key. If the target is not found then return -1. Note: Consider 0 based indexing

Examples
Example 1:
Input:
 N = 7, target = 13, array[] = {3, 4, 13, 13, 13, 20, 40}  
Output:
 4  
Explanation:
 The target value 13 appears for the first time at index number 2 in the array.  

 ---

 # 07 - >  Count Occurrences in Sorted Array

Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.

Examples
Example 1:
Input:
 N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
Output
: 4
Explanation:
 3 is occurring 4 times in 
the given array so it is our answer.

---

# 08 -> Search Element in a Rotated Sorted Array |


Problem Statement: Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.

Examples
Input:nums = [4, 5, 6, 7, 0, 1, 2], k = 0
Output :4
Explanation : Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

--- 

#  09 -> Search Element in Rotated Sorted Array II


Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.

Examples
Example 1:
Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Result: True
Explanation: The element 3 is present in the array. So, the answer is True.

---

#  10 -> Minimum in Rotated Sorted Array

Problem Statement:
Given an integer array arr of size N, sorted in ascending order (with distinct values), the array is rotated at any index which is unknown. Find the minimum element in the array.

Pre-requisites: Search in Rotated Sorted Array I,  Search in Rotated Sorted Array II & Binary Search algorithm

Examples
Input: arr = [4,5,6,7,0,1,2,3]
Output: 0
Explanation: The minimum element in the array is 0.

---

