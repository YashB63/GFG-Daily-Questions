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

Day 11:

  Q1: Painting the Fence:

    Given a fence with n posts and k colors, 
    find out the number of ways of painting the fence so that not more than two 
    consecutive posts have the same colors. 

    Since the answer can be large return it modulo 10^9 + 7.


  Q2: Minimum distance between two numbers:

    You are given an array a, of n elements. 
    Find the minimum index based distance between two distinct elements of the array, 
    x and y. Return -1, if either x or y does not exist in the array.

  Q3: First repeating element:

    Given an array arr[] of size n, find the first repeating element. 
    The element should occur more than once and the index of its first occurrence should be        the smallest.
    
    Note:- The position you return should be according to 1-based indexing. 


Day 12:

  Q1: Reach the Nth point:

    There are N points on the road, 
    you can step ahead by 1 or 2 . If you start from a point 0, 
    and can only move from point i to point i+1 after taking a step of length one, 
    find the number of ways you can reach at point N. 

  Q2: Check if array is sorted:

    Given an array arr[] of size N, check if it is sorted in non-decreasing order or not.

  Q3: Intersection of two arrays:

Day 13:

  Q1: String's Count:

    Given a length n, count the number of strings of length n 
    that can be made using a, b and c with at-most one b and two c allowed.

  Q2: Move all zeroes to end of array:

    Given an array arr[] of n positive integers. 
    Push all the zeros of the given array to the right end of the array while 
    maintaining the order of non-zero elements. Do the mentioned change in the array in-place.

  Q3: Rotation:

    Given an ascending sorted rotated array Arr of 
    distinct integers of size N. The array is right rotated K times. 
    Find the value of K.
    
Day 14:

  Q1: Max sum without adjacents:

    Given an array Arr of size N containing positive integers. 
    Find the maximum sum of a any possible subsequence such that 
    no two numbers in the subsequence should be adjacent in Arr.

  Q2: Minimize the sum of product:

    You are given two arrays, A and B, of equal size N. 
    The task is to find the minimum value of 
    A[0] * B[0] + A[1] * B[1] + .... + A[N-1] * B[N-1], 
    where shuffling of elements of arrays A and B is allowed.

  Q3: Maximum size of consecutives:

    Given a sorted array arr of n distinct elements and an integer k. 
    The array elements denote positions of points on 1-D number line, 
    find the maximum size of subset of points that can have consecutive values 
    of points which can be formed by placing another k points on the number line.

Day 15:

  Q1: Game of XOR:

    Given an array A of size N. 
    The value of an array is denoted by the bit-wise 
    XOR of all elements it contains. Find the bit-wise XOR 
    of the values of all subarrays of A.

  Q2: Product array puzzle:

    Given an array nums[] of size n, 
    construct a Product Array P (of same size n) such that 
    P[i] is equal to the product of all the elements of nums except nums[i].

  Q3: Remove duplicates from sorted array:

    Given a sorted array A[] of size N, 
    delete all the duplicated elements from A[]. 
    Modify the array such that if there are X distinct elements in it 
    then the first X positions of the array should be filled with them in 
    increasing order and return the number of distinct elements in the array.
    
    Note:
    1. Don't use set or HashMap to solve the problem.
    2. You must return the number of distinct elements(X) in the array, 
    the driver code will print all the elements of the modified array from 
    index 0 to X-1 as output of your code.


Day 16:

  Q1: Rightmost different bit:

    Given two numbers M and N. 
    The task is to find the position of the rightmost different bit 
    in the binary representation of numbers. 
    If both M and N are the same then return -1 in this case.

  Q2: Union of two sorted arrays:

    Union of two arrays can be defined as the common 
    and distinct elements in the two arrays.
    Given two sorted arrays of size n and m respectively, 
    find their union.

  Q3: Alternative positive and negative numbers:

    Given an unsorted array Arr of N positive and negative numbers. 
    Your task is to create an array of alternate positive and 
    negative numbers without changing the relative order of positive and negative numbers.
    
    Note: Array should start with a positive number and 0 (zero) should be considered a       
    positive element.
 
  
Day 17:

  Q1: Modified game of nim:

    You are given an array A of n elements. 
    There are two players player 1 and player 2.
    
    A player can choose any of element from an array and remove it. 
    If the bitwise XOR of all remaining elements equals 0 
    after removal of the selected element, then that player loses. 
    Find out the winner if player 1 starts the game and they both play their best.

  Q2: Implement two stacks in an array:

    Your task is to implement  2 stacks in one array efficiently. 
    You need to implement 4 methods.
    
    push1 : pushes element into first stack.
    
    push2 : pushes element into second stack.
    
    pop1 : pops element from first stack and returns the popped element. 
    If first stack is empty, it should return -1.
    
    pop2 : pops element from second stack and returns the popped element. 
    If second stack is empty, it should return -1.

  Q3: Find all pairs with a given sum: 

    Given two unsorted arrays A of size N and B of 
    size M of distinct elements, 
    the task is to find all pairs from both arrays 
    whose sum is equal to X.
    
    Note: All pairs should be printed in increasing order of u. 
    For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then
    (u1,v1) should be printed first else second.


Day 18:

  Q1: Candy:

    There are N children standing in a line. 
    Each child is assigned a rating value 
    given in the integer array ratings.
    
    You are giving candies to these children 
    subjected to the following requirements:
    
    Each child must have atleast one candy.
    
    Children with a higher rating than its neighbors 
    get more candies than their neighbors.
    
    Return the minimum number of candies 
    you need to have to distribute.

  Q2: Pascal Triangle:

    Given a positive integer N, return the Nth row of pascal's triangle.
    
    Pascal's triangle is a triangular array of the binomial coefficients 
    formed by summing up the elements of previous row.
    
    The elements can be large so return it modulo 109 + 7.


  Q3: Save Ironman:
    
    Jarvis is weak in computing palindromes for Alphanumeric characters.
    
    While Ironman is busy fighting Thanos, he needs to activate 
    sonic punch but Jarvis is stuck in computing palindromes.
    
    You are given a string S containing alphanumeric characters. 
    Find out whether the string is a palindrome or not.
    
    If you are unable to solve it then 
    it may result in the death of Iron Man.


Day 19:

  Q1: Maximum meetings in one room:

    There is one meeting room in a firm. 
    There are N meetings in the form of (S[i], F[i]) where S[i] 
    is the start time of meeting i and F[i] is the finish time of meeting i. 
    
    The task is to find the maximum number of meetings 
    that can be accommodated in the meeting room. 
    
    You can accommodate a meeting if the start time of the meeting is 
    strictly greater than the finish time of the previous meeting.
     
    Print all meeting numbers.
    
    Note: If two meetings can be chosen for the same slot 
    then choose meeting with smaller index in the given array.

  Q2: Palindrome String:

    Given a string S, check if it is palindrome or not.

  Q3: Kadane's Algorithm:

    Given an array Arr[] of N integers. 
    Find the contiguous sub-array(containing at least one number) 
    which has the maximum sum and return its sum.

  
Day 20:

  Q1: Count more than n/k occurences:

    Given an array arr of size N and an element k. 
    The task is to find the count of elements in the array 
    that appear more than n/k times.

  Q2: Median of two sorted arrays of different sizes:

    Given two sorted arrays array1 and array2 of size 
    m and n respectively. Find the median of the two sorted arrays.

  Q3: Three way partitioning:

    Given an array of size n and a range [a, b]. 
    The task is to partition the array around the range 
    such that array is divided into three parts.
    
    1) All elements smaller than a come first.
    2) All elements in range a to b come next.
    3) All elements greater than b appear in the end.
    The individual elements of three sets can appear in any order. 
    
    You are required to return the modified array.
    
    Note: The generated output is 1 if you modify the given array successfully.


Day 21:

  Q1: Buy Maximum Stocks if i stocks can be bought on i-th day:

    In a stock market, there is a product with its infinite stocks. 
    The stock prices are given for N days, where price[i] denotes 
    the price of the stock on the ith day.
    There is a rule that a customer can buy at most i stock on the ith day.
    
    If the customer has an amount of k amount of money initially. 
    The task is to find out the maximum number of stocks a customer can buy. 

  Q2: Anagram:

    Given two strings a and b consisting of lowercase characters. 
    The task is to check whether two given strings are an anagram of each other or not. 
    An anagram of a string is another string that contains the same characters, 
    only the order of characters can be different. 
    
    For example, act and tac are an anagram of each other.
    
    Note:-
    
    If the strings are anagrams you have to return True or else return False

    |s| represents the length of string s.


  Q3: Mirror Tree:

    Given a Binary Tree, convert it into its mirror.


Day 22:

  Q1: Determinant of a Matrix:

    Given a square matrix of size n*n. 
    The task is to find the determinant of this matrix.

  Q2: Remove Duplicates

    Given a string without spaces, the task is to remove duplicates from it.
    
    Note: The original order of characters must be kept the same. 

  Q3: Rotate Bits:

    Given an integer N and an integer D, 
    rotate the binary representation of the integer N 
    by D digits to the left as well as right and 
    return the results in their decimal representation after each of the rotation.
    
    Note: Integer N is stored using 16 bits. i.e. 
    12 will be stored as 0000000000001100.


Day 23:

  Q1: Largest rectangular sub-matrix whose sum is 0:

    Given a matrix mat[][] of size N x M. 
    The task is to find the largest rectangular 
    sub-matrix by area whose sum is 0.
    
    If there are multiple solutions return the rectangle 
    which starts from minimum column index. 
    If you still have multiple solutions return the 
    one starting from minimum row index. 
    If you still have multiple solutions return the 
    one having greatest row number. 
    
    If no such matrix is present return a zero (0) size matrix.

  Q2: Twice Counter:

    Given a list of N words. Count the number of words 
    that appear exactly twice in the list.

  Q3: Panagram Checking:

    Given a string check if it is Panagram or not. 
    A panagram is a sentence containing every letter 
    in the English Alphabet (either lowercase or uppercase or both). 
    For example, we say the letter A is present in the string 
    if either 'a' is present or 'A' is present.
