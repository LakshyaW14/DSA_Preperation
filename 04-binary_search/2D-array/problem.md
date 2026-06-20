# Binary Search in 2D Array 

## 01 -> Search in 2D Mat
Search in a sorted 2D matrix

Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. The elements of each row are sorted in non-decreasing order. Moreover, the first element of a row is greater than the last element of the previous row (if it exists). You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.

Examples
Input :mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], target = 8
Output :True.
Explanation :The target = 8 exists in the 'mat' at index (1, 3).

## 02 -> Search in 2D Mat 2

Search in a row and column-wise sorted matrix

Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. The elements of each row and each column are sorted in non-decreasing order. But, the first element of a row is not necessarily greater than the last element of the previous row (if it exists). You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.

Examples
Example 1:
Matrix=
1   4   7   11
2   5   8   12
3   6   9   16
10 13  14  17
Target: 9
Output: Found at (2,2) (0-indexed)


## 03 -> Find Row with maximum 1s

Find the row with maximum number of 1's

Problem Statement: You have been given a non-empty grid ‘mat’ with 'n' rows and 'm' columns consisting of only 0s and 1s. All the rows are sorted in ascending order. Your task is to find the index of the row with the maximum number of ones. Note: If two rows have the same number of ones, consider the one with a smaller index. If there's no row with at least 1 zero, return -1

Examples
Example 1:
Input Format: n = 3, m = 3, 
mat[] = 
1 1 1
0 0 1
0 0 0
Result: 0
Explanation: The row with the maximum number of ones is 0 (0 - indexed).

 