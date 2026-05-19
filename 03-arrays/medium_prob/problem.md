# Problem Statements on array ( medium)

## 01 - Two Sum : Check if a pair with given sum exists in Array

Problem Statement: Given an array of integers arr[] and an integer target.

1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

---

# 02 - Sort an array of 0s , 1s and 2sProblem 

Statement: Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.

Examples
Input: nums = [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two


## 03 -> Find the Majority Element that occurs more than N/2 times

Problem Statement: Given an integer array nums of size n, return the majority element of the array.

The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

Example 1:
Input:
 nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]  
Output:
 7  
Explanation:
 The number 7 appears 5 times in the 9-sized array, making it the most frequent element.

---

# 04 - > Kadane's Algorithm : Maximum Subarray Sum in an Array

Oneline Intuition -> Simply move -> Add on element to sum, if sum is smaller, neglect the subarray

Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.

A subarray is a contiguous non-empty sequence of elements within an array.

Examples
Example 1:
Input:
 nums = [2, 3, 5, -2, 7, -4]  
Output:
 15  
Explanation:
 The subarray from index 0 to index 4 has the largest sum = 15, which is the maximum sum of any contiguous subarray.
# second variation-> print the subarray with maximum sum 
---

# 05 -> Stock Buy And Sell

Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note: That buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

---

# 06 Rearrange Array Elements by Sign


Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

Examples
Example 1:
Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5
Explanation: 

Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

---

# 07 -> next_permutation : find next lexicographically greater permutation


Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

Examples
Input: Arr[] = {1,3,2}
Output: {2,1,3}
Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,13} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2}

# 08 ->  Leaders in array

Examples
Example 1:
Input:
 arr = [4, 7, 1, 0]  
Output:
 7 1 0  
Explanation:
 The rightmost element (0) is always a leader.  
7 and 1 are greater than the elements to their right, making them leaders as well.

# 09 ->Longest Consecutive Sequence in an Array



Problem Statement: Given an array nums of n integers.

Return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.

Examples
Example 1:
Input:
 nums = [100, 4, 200, 1, 3, 2]  
Output:
 4  
Explanation:
 The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4. This sequence can be formed regardless of the initial order of the elements in the array.

 ---

 # 10- Set Matrix Zero


Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix..

Examples
Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.

---

# 11 - Spiral Traversal of Matrix


Problem Statement: Given a Matrix, print the given matrix in spiral order.

Examples
Input: Matrix[][] = { { 1, 2, 3, 4 },{ 5, 6, 7, 8 },{ 9, 10, 11, 12 },{ 13, 14, 15, 16 } }
Outhput: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.
Explanation: The output of matrix in spiral form.

---

# 12 -> Count Subarray sum Equals K


Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k. A subarray is a contiguous non-empty sequence of elements within an array.

Examples
Input : N = 4, array[] = {3, 1, 2, 4}, k = 6
Output: 2
Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

---

# 13 -> Rotate Image by 90 degree


Problem Statement: Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise. The rotation must be done in place, meaning the input 2D matrix must be modified directly..

Examples
Input :matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            
Output :
matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


Explanation :
First, we transpose the matrix: rows become columns. Then, we reverse each row to simulate 90° clockwise rotation. So element at (0,0) goes to (0,2), (0,1) goes to (1,2), and so on, achieving the rotated layout.

