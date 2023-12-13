# GFG-Daily-Questions
This repository comprises of the daily coding questions solved on GFG platform.

Day 1:

  Q1: Find the Minimum and Maximum Elements in an Array:
  
      Given an array A of size N of integers. 
      Your task is to find the minimum and maximum elements in the array.

  Q2: Missing number in array:

    Given an array of size N-1 such that it only contains distinct integers in 
    the range of 1 to N. 
    Find the missing element.

  Q3: Search an element in an array:

    Given an integer array and another integer element. 
    The task is to find if the given element is present in array or not.

Day 2:

  Q1: Wave  Array:

    Given a sorted array arr[] of distinct integers. 
    Sort the array into a wave-like array(In Place).
    In other words, arrange the elements into a sequence such that 
    arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....

    If there are multiple solutions, find the lexicographically smallest one.
    
    Note:The given array is sorted in ascending order, and you don't need to return 
    anything to make changes in the original array itself.

  Q2: Sum of array elements:

    Given an integer array arr of size n, you need to sum the elements of arr.

  Q3: Bitonic Point:

    Given an array arr of n elements that is first strictly increasing 
    and then maybe strictly decreasing, find the maximum element in the array.
    
    Note: If the array is increasing then just print the last element will be the maximum value.

Day 3:

  Q1: How many X's:

    Given two integers L, R, and digit X. Find the number of occurrences of X 
    in all the numbers in the range (L, R) excluding L and R.

  Q2: Check if two arrays are equal or not:

    Given two arrays A and B of equal size N, the task is to find if given arrays 
    are equal or not. 
    
    Two arrays are said to be equal if both of them contain same set of elements, 
    arrangements (or permutation) of elements may be different though.

  Q3: Binary Search
  
    Given a sorted array of size N and an integer K, find the position(0-based indexing) 
    at which K is present in the array using binary search.

Day 4:

  Q1 : Palindromic Array:

    Given a Integer array A[] of n elements. 
    Your task is to complete the function PalinArray. 
    Which will return 1 if all the elements of the Array are palindrome otherwise it will           return 0.

  Q2: Print Alternate Elements of an Array:

    You are given an array A of size N. You need to print elements 
    of A in alternate order (starting from index 0).

  Q3: Print the Pattern | Set-1:

    You are given a number N. 
    You need to print the pattern for the given value of N.
    
    For N = 2 the pattern will be 
    2 2 1 1
    2 1
    
    For N = 3 the pattern will be 
    3 3 3 2 2 2 1 1 1
    3 3 2 2 1 1
    3 2 1
    
    Note: Instead of printing a new line print a "$" without quotes. 
    After printing the total output, end of the line is expected.

Day 5:

  Q1: Sum of Series:

    Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms) 

  Q2: Transform to Prime:

    Given an array of n integers. 
    Find the minimum non-negative number to be inserted in array, 
    so that sum of all elements of array becomes prime.

  Q3: Value equal to Index:

    Given an array Arr of N positive integers. 
    Your task is to find the elements whose value is equal to 
    that of its index value ( Consider 1-based indexing ).
    
    Note: There can be more than one element in the array which have the same value as its   index. 
    You need to include every such element's index. 
    Follows 1-based indexing of the array.

Day 6:

  Q1: Smith Number:

    Given a number n, the task is to find out whether this number is a Smith number or not. 
    A Smith number is a composite number whose sum of digits is equal to the sum of digits of      its prime factors.

  Q2: Find duplicattes in an Array:

    Given an array a of size N which contains elements from 0 to N-1, 
    you need to find all the elements occurring more than once in the given array. 
    Return the answer in ascending order. 
    If no such element is found, return list containing [-1].

  Q3: Leaders in an Array:

    Given an array A of positive integers. Your task is to find the leaders in the array. 
    An element of array is leader if it is greater than or equal to all the elements to its        right side. 
    The rightmost element is always a leader.

Day 7:

  Q1: Subarray with 0 sum:

    Given an array of integers. Find if there is a subarray (of size at-least one) with 0 sum. 
    You just need to return true/false depending upon whether there is a subarray present with     0-sum or not. 
    Printing will be taken care by the driver code.

  Q2: Equilibrium Point:

      Given an array A of n positive numbers. 
      The task is to find the first equilibrium point in an array. 
      Equilibrium point in an array is an index (or position) such that 
      the sum of all elements before that index is same as sum of elements after it.
    
      Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists.

  Q3: Print 1 to N without Loop:

      Print numbers from 1 to N without the help of loops.

Day 8:

  Q1: Max sum subarray of size K:

    Given an array of integers Arr of size N and a number K. 
    Return the maximum sum of a subarray of size K.
    
  Q2: Count pairs with given sum:

    Given an array of N integers, and an integer K, 
    find the number of pairs of elements in the array whose sum is equal to K.

  Q3: Rotate array:

    Given an unsorted array arr[] of size N. 
    Rotate the array to the left (counter-clockwise direction) by D steps, 
    where D is a positive integer. 

Day 9:

  Q1: Gold Mine Problem:

    Given a gold mine called M of (n x m) dimensions. 
    Each field in this mine contains a positive integer which is the amount of gold in tons. 
    Initially the miner can start from any row in the first column. 
    
    From a given cell, the miner can move
    
    1. to the cell diagonally up towards the right 
    2. to the right
    3. to the cell diagonally down towards the right
    
    Find out maximum amount of gold which he can collect until he can no longer move.

  Q2: Frequencies of limited range array elements:

    Given an array arr[] of N positive integers which can contain integers from 1 to P 
    where elements can be repeated or can be absent from the array. 
    Your task is to count the frequency of all numbers from 1 to N. 
    Make in-place changes in arr[], such that arr[i] = frequency(i). Assume 1-based indexing.
    
    Note: The elements greater than N in the array can be ignored for counting and do modify       the array in-place. 

  Q3: Find Transition Point:

    Given a sorted array containing only 0s and 1s, 
    find the transition point, i.e., the first index where 1 was observed, 
    and before that, only 0 was observed.

Day 10: 

  Q1: Consecutive 1's not allowed:

    Given a positive integer N, count all possible distinct binary strings of 
    length N such that there are no consecutive 1’s. 
    Output your answer modulo 109 + 7.

  Q2: Longest common prefix in an array:

    Given an array of N strings, 
    find the longest common prefix among all strings present in the array.

  Q3: Key Pair:

    Given an array Arr of N positive integers and another number X. 
    Determine whether or not there exist two elements in Arr whose sum is exactly X.
