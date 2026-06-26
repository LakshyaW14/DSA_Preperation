# Binary Search on Answers

## 01-> Finding Sqrt of a number using Binary Search

Problem Statement: You are given a positive integer n. Your task is to find and return its square root. If ‘n’ is not a perfect square, then return the floor value of sqrt(n).

Examples
Input: N = 36
Output: 6
Explanation: Square root of 36 is 6. 
Input: N = 28
Output: 5
Explanation: Square root of 28 is approximately 5.292. So, the floor value will be 5. 

---

## 02-> Nth Root of a Number using Binary Search

Problem Statement: Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M. If the 'nth root is not an integer, return -1.

Examples
Input: N = 3, M = 27
Output: 3
Explanation: The cube root of 27 is equal to 3.

---

## 03 -> Koko Eating Bananas

Problem Statement: A monkey Koko is given ‘n’ piles of bananas, whereas the 'ith' pile has ‘a[i]’ bananas. An integer ‘h’ is also given, which denotes the time (in hours) for all the bananas to be eaten.

Each hour, the monkey chooses a non-empty pile of bananas and eats ‘k’ bananas. If the pile contains less than ‘k’ bananas, then the monkey consumes all the bananas and won’t eat any more bananas in that hour.

Find the minimum number of bananas ‘k’ to eat per hour so that the monkey can eat all the bananas within ‘h’ hours.

Examples
Input: N = 4, a[] = {7, 15, 6, 3}, h = 8
Output: 5
Explanation:  If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly. So, he will take 8 hours to complete all the piles.  

---

## 04 - > Minimum days to make M bouquets

Problem Statement: You are given 'N’ roses and you are also given an array 'arr' where 'arr[i]' denotes that the 'ith' rose will bloom on the 'arr[i]th' day. You can only pick already bloomed roses that are adjacent to make a bouquet. You are also told that you require exactly 'k' adjacent bloomed roses to make a single bouquet. Find the minimum number of days required to make at least ‘m' bouquets each containing 'k' roses. Return -1 if it is not possible.

Examples
Example 1:
Input Format: N = 8, arr[] = {7, 7, 7, 7, 13, 11, 12, 7}, m = 2, k = 3
Result: 12
Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.

---

## 05 -> Find the Smallest Divisor Given a Threshold


Problem Statement: You are given an array of integers 'arr' and an integer i.e. a threshold value 'limit'. Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it, the sum of the division's result is less than or equal to the given threshold value.

Examples
Example 1:
Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
Result: 3
Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.

---

## 06 -> Capacity to Ship Packages within D Days

Problem Statement: You are the owner of a Shipment company. You use conveyor belts to ship packages from one port to another. The packages must be shipped within 'd' days. The weights of the packages are given in an array 'of weights'. The packages are loaded on the conveyor belts every day in the same order as they appear in the array. The loaded weights must not exceed the maximum weight capacity of the ship. Find out the least-weight capacity so that you can ship all the packages within 'd' days .

Examples

Input: N = 5, weights = [5, 4, 5, 2, 3, 4, 5, 6], d = 5
Output: 9
Explanation: The minimum ship capacity needed to ship all packages within 5 days is 9.

---

## 07 -> Kth Missing Positive Number

Problem Statement: You are given a strictly increasing array ‘vec’ and a positive integer 'k'. Find the 'kth' positive integer missing from 'vec'.

Examples
Example 1:
Input Format: vec[]={4,7,9,10}, k = 1
Result: 1
Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 1, the first missing element is 1.

---

## 08 -> Aggressive Cows : Detailed Solution

Problem Statement: You are given an array 'arr' of size 'n' which denotes the position of stalls. You are also given an integer 'k' which denotes the number of aggressive cows.
You are given the task of assigning stalls to 'k' cows such that the minimum distance between any two of them is the maximum possible. Find the maximum possible minimum distance.

Examples
Example 1:
Input Format:
 N = 6, k = 4, arr[] = {0,3,4,7,10,9}
Result:
 3
Explanation:
 The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions {0, 3, 7, 10}. Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.

 ---

 ## 09 -> Allocate Minimum Number of Pages


9

Problem Statement: Given an array ‘arr of integer numbers, ‘ar[i]’ represents the number of pages in the ‘i-th’ book. There are a ‘m’ number of students, and the task is to allocate all the books to the students.
Allocate books in such a way that:

Each student gets at least one book.
Each book should be allocated to only one student.
Book allocation should be in a contiguous manner.
You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum. If the allocation of books is not possible. return -1

Examples
Example 1:

Input Format: n = 4, m = 2, arr[] = {12, 34, 67, 90}
Result: 113
Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.
