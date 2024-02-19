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


Day 24:

  Q1: Anti Diagonal traversal of a matrix:
    
    Give a N*N square matrix, return an array of its 
    anti-diagonals in top-leftmost to bottom-rightmost order. 
    In an element of a anti-diagonal (i, j), surrounding elements will be 
    (i+1, j-1) and (i-1, j+1). 
    
    Look at the examples for more clarity.

  Q2: Arithmetic Number:

    Given three integers  'A' denoting the first term 
    of an arithmetic sequence , 'C' denoting the common difference 
    of an arithmetic sequence and an integer 'B'. 
    
    you need to tell whether 'B' exists in the 
    arithmetic sequence or not. Return 1 if B is present in the sequence. 
    Otherwise, returns 0.

  Q3: Perfect Number:

    Given a number N, check if a number is perfect or not. 
    A number is said to be perfect if sum of all its factors 
    excluding the number itself is equal to the number. 
    
    Return 1 if the number is Perfect otherwise return 0.


Day 25:

  Q1: Wildcard string matching:

    Given two strings wild and pattern. 
    Determine if the given two strings can be matched given that, 
    wild string may contain * and ? but string pattern will not. 
    
    * and ? can be converted to another character 
    according to the following rules:
    
    * --> This character in string wild can be 
    replaced by any sequence of characters, 
    it can also be replaced by an empty string.
    
    ? --> This character in string wild can 
    be replaced by any one character.


  Q2: Reverse Coding:

    You will be given an integer n, 
    your task is to return the sum of 
    all natural number less than or equal to n.
    
    As the answer could be very large, return answer modulo 10^9+7.

  Q3: Series GP:

    Given the A and R i,e first term and common ratio of a GP series. 
    Find the Nth term of the series.
    
    Note: As the answer can be rather 
    large print its modulo 1000000007 (10^9 + 7).


Day 26:

  Q1: Check if a string is repetition of its substring of k-length:

    Given a string s, check if it is possible to convert it 
    into a string that is the repetition of a substring of length k. 
    Conversion has to be done by following the steps mentioned below only once:
    
    Select two indices i and j (zero-based indexing, i could be equal to j), 
    such that i and j are divisible by k.
    
    Select substrings of length k starting from indices i and j.
    
    Replace substring starting at index i with 
    substring starting at index j within the string.

  Q2: Nth Fibonacci Number:

    Given a positive integer n, 
    find the nth fibonacci number. 
    
    Since the answer can be very large, 
    return the answer modulo 1000000007.

  Q3: Square root of a number:
  
    Given an integer x, find the square root of x. 
    If x is not a perfect square, then return floor(√x).


Day 27:

  Q1: Winner of an election:

    Given an array of n names arr of candidates in an election, 
    where each name is a string of lowercase characters. 
    
    A candidate name in the array represents a vote casted 
    to the candidate. Print the name of the candidate that 
    received the maximum count of votes. 
    
    If there is a draw between two candidates, 
    then print lexicographically smaller name.


  Q2: Frogs and Jumps:

    N frogs are positioned at one end of the pond. 
    All frogs want to reach the other end of the pond 
    as soon as possible. 
    
    The pond has some leaves arranged in a straight line. 
    Each frog has the strength to jump exactly K leaves.
    
    For example, a  frog having strength 2 
    will visit the leaves 2, 4, 6, ...  etc. 
    while crossing the pond.
    
    Given the strength of each frog and the number of leaves, 
    your task is to find the number of leaves that not be visited 
    by any of the frogs when all frogs have reached the other end of the pond. 


  Q3: Maximum Diamonds:

    There are N bags with diamonds in them. 
    The i'th of these bags contains A[i] diamonds. 
    If you drop a bag with A[i] diamonds, it changes to 
    A[i]/2 diamonds and you gain A[i] diamonds. 
    
    Dropping a bag takes 1 minute. 
    
    Find the maximum number of diamonds that 
    you can take if you are given K minutes.


Day 28:

  Q1: New Year Resolution:

    As the clock struck midnight on New Year's Eve, 
    Geek bid farewell to the wasted moments of 2023, 
    realizing the untapped potential of GFG's Problem of the Day.
    
    His 2024 resolution: Solve POTD every day.
    
    Eager to earn coins for GFG Merchandise, Geek faces new rules:
    
    Earning Coin: Geek can accumulate coins[i] by 
    solving the POTD on the ith day, where 1 <= coins[i] <= 2024 
    and the sum of coins <= 2024.
    
    Merchandise Eligibility: To purchase merchandise, 
    the coins earned must be divisible by 20 or 24, or precisely equal to 2024.
    
    Geek's resolutions often fades over time. 
    Realistically, he can only commit to active participation 
    for N (where N ≤ 366) days. Given the value of N and 
    number of coins associated with each POTD, 
    can Geek strategically solve some (or all) POTDs 
    to become eligible for redeeming merchandise?

  Q2: Largest Number Possible:

    Given two numbers 'N' and 'S' , 
    find the largest number that can be formed with 'N' digits 
    and whose sum of digits should be equals to 'S'. 
    
    Return -1 if it is not possible.

  Q3: Minimum Integer:

    You are given an array A of size N. 
    Let us denote S as the sum of all integers present in the array. 
    
    Among all integers present in the array, 
    find the minimum integer X such that S ≤ N*X.


Day 29:

  Q1: Array pair sum divisiility problem:

    Given an array of integers nums and a number k, 
    write a function that returns true if given array 
    can be divided into pairs such that 
    sum of every pair is divisible by k.

  Q2: Least Prime Factors:
    
    Given a number N, find the least prime factors 
    for all numbers from 1 to N.  
    
    The least prime factor of an integer X 
    is the smallest prime number that divides it.
    
    Note :
    
    1 needs to be printed for 1.
    
    You need to return an array/vector/list of 
    size N+1 and need to use 1-based indexing to store the answer for each number.

  Q3: Array Operations:

    You are given an array arr of n integers. 
    You must return the minimum number of operations 
    required to make this array 0. 
    
    For this you can do an operation :
    
    Choose a sub-array of non-zero elements & 
    replace all with 0(0 must be present in arr, 
    if not you can not replace it).


Day 30:

  Q1: Largest sum subarray of size atleast K:
    
    Given an array a of length n and a number k, 
    find the largest sum of the subarray containing at least k numbers. 
    It is guaranteed that the size of array is at-least k.

  Q2: Number of Open Doors:

    Consider a long alley with a N number of doors on one side. 
    
    All the doors are closed initially. 
    
    You move to and fro in the alley changing the states of the doors as follows: 
    
    you open a door that is already closed and you close a door that is already opened. 
    
    You start at one end go on altering the state of the doors till 
    you reach the other end and then you come back and start altering the states of the doors      again.
    
    In the first go, you alter the states of doors numbered 1, 2, 3, , n.
    
    In the second go, you alter the states of doors numbered 2, 4, 6
    
    In the third go, you alter the states of doors numbered 3, 6, 9
    
    You continue this till the Nth go in which 
    you alter the state of the door numbered N.
    
    You have to find the number of open doors 
    at the end of the procedure.

  Q3: Find Nth root of M:

    You are given 2 numbers (n , m); 
    the task is to find n√m (nth root of m).


Day 31:

  Q1: Smallest window containing 0, 1 and 2:

    Given a string S consisting of the characters 0, 1 and 2. 
    Your task is to find the length of the smallest substring of 
    string S that contains all the three characters 0, 1 and 2. 
    If no such substring exists, then return -1.

  Q2: Parenthesis Checker:

    Given an expression string x.
     
    Examine whether the pairs and the 
    orders of {,},(,),[,] are correct in exp.
    
    For example, the function should 
    return 'true' for exp = [()]{}{[()()]()} 
    and 'false' for exp = [(]).
    
    Note: The drive code prints "balanced" 
    if function return true, otherwise it prints "not balanced".

  Q3: Second Largest:

    Given an array Arr of size N, 
    print second largest distinct element from an array.


Day 32:

  Q1: Find element occuring once when all other are present thrice:

    Given an array of integers arr[] of length N, 
    every element appears thrice except for one which occurs once.
    Find that element which occurs once.

  Q2: Peak element:

    An element is called a peak element if its value 
    is not smaller than the value of its adjacent elements (if they exists). 
    
    Given an array arr[] of size N, 
    Return the index of any one of its peak elements. 
    
    Note: The generated output will always be 1 if the index 
    that you return is correct. Otherwise output will be 0. 
    
    Also, arr[] will be in ascending order before the peak element, 
    and in descending order after that.

  Q3: Common elements:

    Given three arrays sorted in increasing order. 
    Find the elements that are common in all three arrays.
    
    Note: can you take care of the duplicates without 
    using any additional Data Structure?


Day 33:

  Q1: Count possible ways to construct buildings:

    There is a road passing through a city with N plots on both sides of the road. 
    Plots are arranged in a straight line on either side of the road. 
    Determine the total number of ways to construct buildings in these plots, 
    ensuring that no two buildings are adjacent to each other. Specifically, 
    buildings on opposite sides of the road cannot be adjacent.
    
    Using * to represent a plot and || for the road, 
    the arrangement for N = 3 can be visualized as follows: * * * || * * *.
    
    Note: As the answer can be very large, print it mod 10^9+7.

  Q2: Find triplets with zero sum:

    Given an array arr[] of n integers. 
    Check whether it contains a triplet that sums up to zero. 
    
    Note: Return 1, if there is at least 
    one triplet following the condition else return 0.

  Q3: Coin CHange

    Given an integer array coins[ ] of size N 
    representing different denominations of currency and an integer sum, 
    find the number of ways you can make sum by using different combinations from coins[ ].  
    
    Note: Assume that you have an infinite supply of each type of coin. 
    And you can use any coin as many times as you want.


Day 34:

  Q1: Techfest and the Queue:
    
    A Techfest is underway, and each participant 
    is given a ticket with a unique number. Organizers 
    decide to award prize points to everyone 
    who has a ticket ID between a and b (inclusive). 
    
    The points given to a participant with 
    ticket number x will be the sum of powers of the prime factors of x.
    
    For instance, if points are to be awarded 
    to a participant with ticket number 12, 
    the amount of points given out will be 
    equal to the sum of powers in the prime factorization 
    of 12 (2^2 × 3^1), which will be 2 + 1 = 3.
    
    Given a and b, determine the sum of all the points 
    that will be awarded to the participants with ticket 
    numbers between a and b (inclusive).

  Q2: Majority Element:

    Given an array A of N elements. 
    Find the majority element in the array. 
    A majority element in an array A of size N 
    is an element that appears strictly more 
    than N/2 times in the array.

  Q3: Minimum Platforms:

    Given arrival and departure times of all trains 
    that reach a railway station. 
    
    Find the minimum number of platforms required 
    for the railway station so that no train is kept waiting.
    
    Consider that all the trains arrive on the 
    same day and leave on the same day. Arrival and 
    departure time can never be the same for a train 
    but we can have arrival time of one train equal 
    to departure time of the other. 
    
    At any given instance of time, same platform 
    can not be used for both departure of a train 
    and arrival of another train. In such cases, 
    we need different platforms.


Day 35:

  Q1: Split Array Largest Sum:

    Given an array arr[] of N elements and a number K., 
    split the given array into K subarrays such that the 
    maximum subarray sum achievable out of K subarrays 
    formed is minimum possible. 
    Find that possible subarray sum.

  Q2: Power of Numbers:

    Given a number and its reverse. 
    Find that number raised to the power of its own reverse.
    
    Note: As answers can be very large, 
    print the result modulo 10^9 + 7.

  Q3: The Celebrity Problem:

    A celebrity is a person who is known to all but 
    does not know anyone at a party. 
    
    If you go to a party of N people, 
    find if there is a celebrity in the party or not.
    
    A square NxN matrix M[][] is used to represent people 
    at the party such that if an element of row i and column j  
    is set to 1 it means ith person knows jth person. 
    
    Here M[i][i] will always be 0.
    
    Note: Follow 0 based indexing.
    
    Follow Up: Can you optimize it to O(N)


Day 36:

  Q1: Merge 2 sorted linked list in reverse order:

    Given two linked lists of size N and M, 
    which are sorted in non-decreasing order. 
    
    The task is to merge them in such a way that 
    the resulting list is in non-increasing order.

  Q2: Trapping Rain Water:

    Given an array arr[] of N non-negative integers 
    representing the height of blocks. If width of each block is 1, 
    compute how much water can be trapped between 
    the blocks during the rainy season. 

  Q3: Stickler Thief:

    Stickler the thief wants to loot money from a 
    society having n houses in a single line. 
    
    He is a weird person and follows a certain rule 
    when looting the houses. According to the rule, 
    he will never loot two consecutive houses. 
    
    At the same time, he wants to maximize the amount he loots. 
    The thief knows which house has what amount of money but is 
    unable to come up with an optimal looting strategy. 
    
    He asks for your help to find the maximum money he can get 
    if he strictly follows the rule. 
    
    ith house has a[i] amount of money present in it.


Day 37:

  Q1: Search Pattern (KMP-Algorithm):

    Given two strings, one is a text string, txt and 
    other is a pattern string, pat. 
    
    The task is to print the indexes of all the occurences 
    of pattern string in the text string. Use one-based indexing 
    while returing the indices. 
    
    Note: Return an empty list incase of no occurences of pattern. 
    Driver will print -1 in this case.

  Q2: Subarray with given sum:

    Given an unsorted array A of size N that 
    contains only non negative integers, 
    find a continuous sub-array that adds to a given number S 
    and return the left and right index(1-based indexing) of that subarray.
    
    In case of multiple subarrays, return the subarray indexes 
    which come first on moving from left to right.
    
    Note:- You have to return an ArrayList consisting of two elements left and right. 
    In case no such subarray exists return an array consisting of element -1.

  Q3: Count the triplets:

    Given an array of distinct integers. 
    The task is to count all the triplets such 
    that sum of two elements equals the third element.

Day 38:

  Q1: Longest subarray with sum divisible by K:
    
    Given an array arr containing N integers and a positive integer K, 
    find the length of the longest sub array with sum of the 
    elements divisible by the given value K.

  Q2: Tom and Jerry:

    Tom and Jerry being bored in this pandemic, 
    decides to play a game. Given an integer N. 
    
    On each player's turn, that player makes a move by 
    subtracting a divisor of current N (which is less than N) 
    from current N, thus forming a new N for the next turn. 
    
    The player who does not have any divisor left to subtract loses the game.
    
    The game begins with Tom playing the first move. 
    
    Both Tom and Jerry play optimally. 
    
    The task is to determine who wins the game. 
    
    Return 1 if Tom wins, else return 0.

  Q3: Binary Modulo:

    You are given a binary string s and an integer m. 
    You need to return an integer r. Where r = k%m, 
    k is the binary equivalent of string s.

Day 39:

  Q1: Remove K digits:

    Given a non-negative integer S represented as a string, 
    remove K digits from the number so that the new number is the smallest possible.
    
    Note : The given num does not contain any leading zero.

  Q2: Make Palindrome:

    You are given an array of strings arr of size n. 
    
    You have to find out if it is possible to make a 
    palindromic string by concatenating all the strings in any order. 
    
    Provided that all the strings given in the array are of equal length.

  Q3: String Mirror:

    You are given a string str of length n. 
    You want to choose a non-zero integer k (k<=n), 
    such that you can perform the following operation:
    
    Take the prefix of the string of length k 
    and append the reverse of it to itself.
    
    Your task is to find the lexicographically 
    smallest string you can get.

Day 40:

  Q1: Reverse first k elements of a queue:

    Given an integer K and a queue of integers, 
    we need to reverse the order of the first K elements of the queue, 
    leaving the other elements in the same relative order.
    
    Only following standard operations are allowed on queue.
    
    enqueue(x) : Add an item x to rear of queue
    dequeue() : Remove an item from front of queue
    size() : Returns number of elements in queue.
    front() : Finds front item.
    
    Note: The above operations represent the general processings. 
    In-built functions of the respective languages can be used to solve the problem.

  Q2: Is binary number multiple of 3:

    Given a number in its binary form 
    find if the given binary number is a multiple of 3. 
    
    It is recommended to finish the task using 
    one traversal of input binary number.

  Q3: Trailing zeroes in a factorial:

    For an integer N find the number of trailing zeroes in N!.  


Day 41:

  Q1: Insertion sort for singly linked list:

    Given a singly linked list, sort the list 
    (in ascending order) using insertion sort algorithm.

  Q2: Break a number:

    Given a really large number N, 
    break it into 3 whole numbers such that 
    they sum up to the original number and 
    find the number of ways to do so. 
    
    Since this number can be very large, 
    return it modulo 109+7. 

  Q3: BBT Counter:

    Given a height h, count the maximum number of balanced 
    binary trees possible with height h. Print the result modulo 10^9 + 7.
    
    Note : A balanced binary tree is one in which for every node, 
    the difference between heights of left and right subtree is not more than 1.

Day 42:

  Q1: Find duplicate rows in a binary matrix:

    Given a boolean matrix of size RxC where 
    each cell contains either 0 or 1, 
    find the row numbers (0-based) of row 
    which already exists or are repeated.

  Q2: Overlapping Rectangles:

    You are given an integer N. 
    Consider an array arr having N elements 
    where arr[i] = 2*i+1. (The array is 0-indexed)
    
    You are allowed to perform the 
    given operation on the array any number of times:
    
    1) Select two indices i and j and 
    increase arr[i] by 1 and decrease arr[j] by 1.
    
    Your task is to find the minimum number 
    of such operations required to make all 
    the elements of the array equal.

  Q3: Make array elements equal:

    Given two rectangles, 
    find if the given two rectangles overlap or not. 
    A rectangle is denoted by providing the x and y coordinates 
    of two points: the left top corner and the 
    right bottom corner of the rectangle. 
    
    Two rectangles sharing a side are considered overlapping. 
    (L1 and R1 are the extreme points of the first rectangle 
    and L2 and R2 are the extreme points of the second rectangle).
    
    Note: It may be assumed that the rectangles are parallel to the coordinate axis.

Day 43:

  Q1: Grinding Geek:

    GeeksforGeeks has introduced a special offer 
    where you can enroll in any course, and if you manage 
    to complete 90% of the course within 90 days, 
    you will receive a refund of 90%.
    
    Geek was fascinated by this offer. 
    This offer was valid for only n days, 
    and each day a new course was available for purchase. 
    
    Geek decided that if he bought a course on some day, 
    he will complete that course on the same day itself 
    and redeem floor[90% of cost of the course] amount back. 
    
    Find the maximum number of courses that Geek can 
    complete in those n days if he had total amount initially.
    
    Note: On any day, Geek can only buy the new course 
    that was made available for purchase that day.

  Q2: Pair Cube Count:

    Given N, count all ‘a’(>=1) and ‘b’(>=0) 
    that satisfy the condition a^3 + b^3 = N.

  Q3: Squares in N*N Chessboard:

    Find the total number of Squares in a N*N chessboard.

Day 44: 

  Q1: Sequence of Sequence:

    Given two integers m and n, try making a 
    special sequence of numbers seq of length n such that
    
    seqi+1 >= 2*seqi 
    seqi > 0
    seqi <= m
    
    Your task is to determine total number 
    of such special sequences possible.

  Q2: Jumping Caterpillars:

    Given N leaves numbered from 1 to N . 
    A caterpillar at leaf 1, jumps from 
    leaf to leaf in multiples of Aj (Aj, 2Aj, 3Aj).
    
    j is specific to the caterpillar. 
    Whenever a caterpillar reaches a leaf, 
    it eats it a little bit.. 
    
    You have to find out how many leaves, 
    from 1 to N, are left uneaten after all K 
    caterpillars have reached the end. 
    
    Each caterpillar has its own jump factor
    denoted by Aj, and each caterpillar 
    starts at leaf number 1.

  Q3: Last Modified Ball:

    Samwell laid out N bowls in a straight line 
    and put a few marbles randomly in each bowl, 
    ith bowl has A[i] marbles. 
    
    A bowl can never have more than 9 marbles at a time. 
    A bowl can have zero marbles. Now Samwells friend adds 
    one more marble to the last bowl, after this addition all 
    the bowls must still be aligned with the rules mentioned above. 
    
    Adding a marble follows the same rules as of addition with carryover. 
    You are given the initial list of the number of marbles in each bowl 
    find the position of the bowl which was last modified. 
    
    It is guaranteed that there is at least 
    one bowl which has at least one space left.
    
    Note: Consider one-based indexing.


Day 45:

  Q1: All unique permutations of an array:

    Given an array arr[] of length n. 
    Find all possible unique permutations of 
    the array in sorted order. 
    
    A sequence A is greater than sequence B 
    if there is an index i for which Aj = Bj 
    for all j<i and Ai > Bi.

  Q2: Remainder on dividing by 11:

    Given a big positive number x represented as string, 
    find value of x % 11 or x mod 11. 
    Output is expected as an integer.

  Q3: Nearest multiple of 10:

    Given a string  N representing a positive number. 
    The task is to round N to the nearest multiple of 10.
    
    Note: If you are having two multiple equally apart 
    from N then we will choose the smallest element among them.


Day 46:

  Q1: Water the plants:

    A gallery with plants is divided into n parts, 
    numbered 0, 1, 2, 3, ..., n-1. There are provisions 
    for attaching water sprinklers in every division. 
    
    A sprinkler with range x at division i can 
    water all divisions from i-x to i+x.
    
    Given an array gallery[] consisting of n integers,
    where gallery[i] is the range of the sprinkler at 
    partition i (a power of -1 indicates no sprinkler attached), 
    return the minimum number of sprinklers that need to be 
    turned on to water the entire gallery. 
    
    If there is no possible way to water the 
    full length using the given sprinklers, print -1.

  Q2: Shortest path from 1 to n:

    Consider a directed graph whose vertices 
    are numbered from 1 to n. 
    
    There is an edge from a vertex i to a vertex j 
    if and only if either j = i + 1 or j = 3 * i. 
    
    The task is to find the minimum number of 
    edges in a path from vertex 1 to vertex n.

  Q3: Modular Multiplicative inverse:

    Given two integers ‘a’ and ‘m’. 
    The task is to find the smallest modular multiplicative 
    inverse of ‘a’ under modulo ‘m’. 
    
    if it does not exist then return -1.


Day 47:

  Q1: Top K numbers in a stream:

    Given N numbers in an array, 
    your task is to keep at most the top K 
    numbers with respect to their frequency.
    
    In other words, you have to iterate over the array, 
    and after each index, determine the top K most 
    frequent numbers until that iteration and store them 
    in an array in decreasing order of frequency. 
    
    An array will be formed for each iteration and 
    stored in an array of arrays. If the total number 
    of distinct elements is less than K, 
    then keep all the distinct numbers in the array. 
    
    If two numbers have equal frequency, 
    place the smaller number first in the array.

  Q2: Maximum Identical bowls:

    There are N bowls containing cookies. In one operation, 
    you can take one cookie from any of the non-empty bowls 
    and put it into another bowl. If the bowl becomes empty you discard it. 
    
    You can perform the above operation any number of times. 
    You want to know the maximum number of bowls 
    you can have with an identical number of cookies.
    
    Note: All the non-discarded bowls should contain the identical number of cookies.

  Q3: Minimum Numbers:

    You are given an array arr of n elements. 
    In one operation you can pick two indices i and j, 
    such that arr[i] >= arr[j] and replace the value 
    of arr[i] with (arr[i] - arr[j]). 
    
    You have to minimize the values of the 
    array after performing any number of such operations.


Day 48:

  Q1: Distribute candies in a binary tree:

    Given a binary tree with N nodes, 
    in which each node value represents number 
    of candies present at that node. 
    
    In one move, one may choose two adjacent nodes 
    and move only one candy from one node to another 
    (the move may be from parent to child, or from child to parent.) 
    
    The task is to find the number of moves 
    required such that every node has exactly one candy.
    
    Note that the testcases are framed such that it is always 
    possible to achieve a configuration in which every node 
    has exactly one candy, after some moves.

  Q2: Cutting Rectangles:

    Given a rectangle of dimensions L x B 
    find the minimum number (N) of identical squares 
    of maximum side that can be cut out from that rectangle 
    so that no residue remains in the rectangle. 
    
    Also find the dimension K of that square.

  Q3:  Ball Coloring:

    Given n balls . All of them are initially  uncolored . 
    You have to color the balls with two colors 
    RED and BLUE such that there can be atmost 
    2 positions where a RED ball is touching BLUE ball 
    or vice versa. 
    
    You have to color all the balls.
    
    Find the number of ways in which balls can be colored.


Day 49:

  Q1: Vertex Cover:

    Vertex cover of an undirected graph is a list of vertices 
    such that every vertex not in the vertex cover shares their 
    every edge with the vertices in the vertex cover. 
    
    In other words, for every edge in the graph, 
    atleast one of the endpoints of the graph should 
    belong to the vertex cover. 
    
    You will be given an undirected graph G, 
    and your task is to determine the smallest 
    possible size of a vertex cover.

  Q2: Summed Matrix:

    A matrix is constructed of size n*n. 
    such that Mi,j= i+j. 
    Count the number of cells having value q.
    
    Note: Assume, the array is in 1-based indexing.

  Q3: Is Square:

    Given four different points in space. 
    Find whether these points can form a square or not.


Day 50:

  Q1: Paths from root with a specified sum:

    Given a Binary tree and a sum S, 
    print all the paths, starting from root, 
    that sums upto the given sum. 

    Path not necessarily end on a leaf node.

  Q2: Rectangles in NxN chessboard:

    Find total number of Rectangles 
    (excluding squares) in a N*N chessboard.

  Q3: Find the minimum time:

    Geek wants to scan N documents using two scanners. 
    If S1 and S2 are the time taken by the scanner 1 and 
    scanner 2 to scan a single document, 
    find the minimum time required to scan all the N documents. 
    
    You can use one or more scanners at a time.


Day 51:

  Q1: Course Schedule:

    There are a total of n tasks you have to pick, 
    labelled from 0 to n-1. 
    Some tasks may have prerequisite tasks, 
    for example to pick task 0 you have to 
    first finish tasks 1, which is expressed as a pair: [0, 1]
    
    Given the total number of n tasks and 
    a list of prerequisite pairs of size m. 
    Find a ordering of tasks you should pick to finish all tasks.
    
    Note: There may be multiple correct orders, 
    you just need to return any one of them. 
    If it is impossible to finish all tasks, 
    return an empty array. 
    
    Driver code will print "No Ordering Possible", 
    on returning an empty array. 
    
    Returning any correct order will give the output as 1, 
    whereas any invalid order will give the output 0. 

  Q2: Final Destination:

    Consider a 2d plane and a Robot which is located at (0,0) 
    who can move only one unit step at a time in any direction i.e. 
    if its initial position is (x,y), he can go to positions (x + 1, y), 
    (x - 1, y), (x, y + 1) or (x, y - 1). 
    
    Now Given three integers a,b 
    (denoting the final position where the robot has to reach), and x. 
    Find out if the Robot can reach the final position in exactly x steps.

  Q3: Triangular Number:

    Given a number N.Check whether it is a triangular number or not.
    
    Note: A number is termed as a triangular number 
    if we can represent it in the form of a triangular grid 
    of points such that the points form an equilateral triangle 
    and each row contains as many points as the row number, i.e., 
    the first row has one point, the second row has two points, 
    the third row has three points and so on.
    
    The starting triangular numbers are 1, 3 (1+2), 
    6 (1+2+3), 10 (1+2+3+4).


Day 52: 

  Q1: Check if a given graph is tree or not:

    You are given an undirected graph of N nodes 
    (numbered from 0 to N-1) and M edges. 
    Return 1 if the graph is a tree, else return 0.
    
    Note: The input graph can have self-loops and multiple edges.

  Q2: All divisors of a number:

    Given an integer N, print all the divisors of N in the ascending order.

  Q3: Number Game:

    Given a number n the task is to find the minimum number 
    which is divisible by all numbers from 1 to n. 
    Print the answer modulo (10^9+7).


Day 53:

  Q1: Shortest Prime Path:

    You are given two four digit prime numbers num1 and num2. 
    Find the distance of the shortest path from Num1 to Num2 
    that can be attained by altering only single digit at a time 
    such that every number that we get after changing a digit 
    is a four digit prime number with no leading zeros.

  Q2: Day of the week:

    Write a program that calculates the day of the week 
    for any particular date in the past or future.

  Q3: Love for the twins:

    Given an Array of Integers Arr of length N, 
    you have to count number of elements of the array 
    that can be counted as pair of equal elements.
  

Day 54:

  Q1: Fractional Knapsack:

    Given weights and values of N items, 
    we need to put these items in a knapsack of capacity W 
    to get the maximum total value in the knapsack.
    
    Note: Unlike 0/1 knapsack, you are allowed to break the item here. 

  Q2: Multiply two polynomials:

    Given two polynomials represented by two arrays 
    that contains the coefficients of poynomials, 
    returns the polynomial in form of array formed 
    after multiplication of given polynomials.

  Q3: Deficient Number:

    Given a number x, your task is to find if 
    this number is Deficient number or not. 
    A number x is said to be Deficient Number 
    if sum of all the divisors of the number denoted by 
    divisorsSum(x) is less than twice the value of the number x. 
    And the difference between these two values is called the deficiency.
    
    Mathematically, if below condition holds the number is said to be Deficient:
    divisorsSum(x) < 2*x
    deficiency = (2*x) - divisorsSum(x)

Day 55:

  Q1: Brackets in Matrix Chain Multipliation:

    Given an array p[] of length n used to denote the dimensions 
    of a series of matrices such that the dimension of i'th matrix 
    is p[i] * p[i+1]. There are a total of n-1 matrices. 
    
    Find the most efficient way to multiply these matrices together. 
    
    As in MCM, you were returning the most effective count but 
    this time return the string which is formed of A - Z (only Uppercase) 
    denoting matrices & Brackets( "(" ")" ) denoting multiplication symbols. 
    
    For example, if n =11, the matrixes can be denoted as 
    A - K as n<=26 & brackets as multiplication symbols.
    
    NOTE:
    
    Each multiplication is denoted by putting open & closed brackets 
    to the matrices multiplied & also Please note that the order of 
    matrix multiplication matters, as matrix multiplication is non-commutative A*B != B*A
    
    As there can be multiple possible answers, 
    the console would print "True" for the correct string 
    and "False" for the incorrect string. 
    You need to only return a string that performs 
    a minimum number of multiplications.

  Q2: Multiply by 11:

    Given a number in the form of a string of length N . 
    You have to multiply the given number by 11.

  Q3: Find the Maximum Number:

    Given a number N, write a program to find a maximum number 
    that can be formed using all of the digits of this number.
    
    Note: The given number can be very large, 
    so the input is taken as a String.

Day 56:

  Q1: Geekina Hate 1s:

    It is a universal fact that Geekina hates 1s however 
    it is also known that Geekina loves the integers having 
    atmost k 1s (set-bits) in their binary representation. 
    
    Geekina demanded nth such non-negative number from Geek, 
    and being a good friend of Geek, 
    now it's your responsibility to tell him that number.
    
    Note: The test cases are generated such that the answer 
    always exists and will fit in the 64-bit data type.

  Q2: Faithful Numbers:

    A number is called faithful if you can write it 
    as the sum of distinct powers of 7. 
    
    e.g.,  2457 = 7 + 7^2 + 7^4 . 
    If we order all the faithful numbers, 
    we get the sequence 1 = 7^0, 7 = 7^1, 
    8 = 7^0 + 7^1, 49 = 7^2, 50 = 7^0 + 7^2 . . . and so on.
    
    Given some value of N, 
    you have to find the N'th faithful number.

  Q3: Amicable Pair:

    Amicable numbers are two different numbers so related that 
    the sum of the proper divisors of each is equal to the other number. 
    (A proper divisor of a number is a positive factor 
    of that number other than the number itself. 
    
    Given two Numbers A and B, find whether 
    they are Amicable Numbers or not. 
    
    Print 1 if they are Amicable else 0.

Day 57:

  Q1: Count Odd Factors:

    Given an integer N, count the numbers having 
    an odd number of factors from 1 to N (inclusive).

  Q2: Lucky Number:

    A n digit number has n*(n+1)/2 sub-numbers.  
    For example, all possible sub-numbers of 975 are 9 7 5 97 75 975. 
    A number is called Lucky if all sub-numbers have different digit product.  
    Digit product of a number is product of its digits.  
    
    For example, the number 23 is Lucky.  
    Sub-numbers of it are 2, 3 and 23 and digit products are 
    2, 3 and 6 respectively (All digit products are different). 
    975 is also lucky. Print 1 if given Number is Lucky else Print 0.

  Q3: Count digit groupings of a number:

    Given a string str consisting of digits, you can divide it 
    into sub-groups by separating the string into substrings. 
    For example, "112" can be divided as 
    {"1", "1", "2"}, {"11", "2"}, {"1", "12"}, and {"112"}.
    
    A valid grouping can be done if you are able to divide 
    sub-groups where the sum of digits in a sub-group is less than 
    or equal to the sum of the digits of the sub-group immediately right to it. 
    Your task is to determine the total number of valid groupings 
    that could be done for a given string.

Day 58:

  Q1: LCS of three strings:

    Given 3 strings A, B and C, 
    the task is to find the length of the longest sub-sequence 
    that is common in all the three given strings.

  Q2: Find first set bit:

    Given an integer N. The task is to return the position of first set bit 
    found from the right side in the binary representation of the number.
    
    Note: If there is no set bit in the integer N, then return 0 from the function.

  Q3: Bubble Sort:

    Given an Integer N and a list arr. 
    Sort the array using bubble sort algorithm.


Day 59:

  Q1: Insert and Search in a Trie:

    Complete the Insert and Search functions for a Trie Data Structure. 
    
    Insert: Accepts the Trie's root and a string, 
    modifies the root in-place, and returns nothing.
    
    Search: Takes the Trie's root and a string, 
    returns true if the string is in the Trie, otherwise false.
    
    Note: To test the correctness of your code, 
    the code-judge will be inserting a list of N 
    strings called into the Trie, and then will search 
    for the string key in the Trie. 
    The code-judge will generate 1 if the key is present in the Trie, else 0.

  Q2: Reverse a String:

    You are given a string s. 
    You need to reverse the string.

  Q3: Prime Number:

    For a given number N check if it is prime or not. 
    A prime number is a number which is only divisible by 1 and itself.


Day 60:

  Q1: Panagram Checking:

    Given a string s check if it is "Panagram" or not.
    
    A "Panagram" is a sentence containing 
    every letter in the English Alphabet.

  Q2: Non Repeating Character:

    Given a string S consisting of lowercase Latin Letters. 
    Return the first non-repeating character in S. 
    If there is no non-repeating character, return '$'.

  Q3: Run Length Encoding:

    Given a string, Your task is to  complete the function 
    encode that returns the run length encoded string for the given string.
    
    eg if the input string is “wwwwaaadexxxxxx”, 
    then the function should return “w4a3d1e1x6″.
    
    You are required to complete the function encode 
    that takes only one argument the string which is 
    to be encoded and returns the encoded string.


Day 61:

  Q1: Implement Atoi:

    Given a string, s, the objective is to convert it into integer 
    format without utilizing any built-in functions. 
    If the conversion is not feasible, the function should return -1.
    
    Note: Conversion is feasible only if all characters in the string 
    are numeric or if its first character is '-' and rest are numeric.

  Q2: Remaining String:

    Given a string S without spaces, a character ch, 
    and an integer count, the task is to find the string 
    after the specified character has occurred count number of times.

  Q3: Closest Strings:

    Given a list of words followed by two words, 
    the task to find the minimum distance between 
    the given two words in the list of words

Day 62: 

  Q1: Decimal Equivalent of Binary Linked List:

    Given a singly linked list of length n. 
    The link list represents a binary number, 
    ie- it contains only 0s and 1s. Find its decimal equivalent.
    
    The significance of the bits decreases 
    with the increasing index in the linked list.
    
    An empty linked list is considered 
    to represent the decimal value 0. 
    
    Since the answer can be very large, 
    answer modulo 109+7 should be printed.

  Q2: Wifi Range:

    There are N rooms in a straight line in 
    Geekland State University's hostel, 
    you are given a binary string S of length N where S[i] = '1' 
    represents that there is a wifi in ith room or 
    S[i] = '0' represents no wifi. Each wifi has range X i.e. 
    if there is a wifi in ith room then its range will go upto 
    X more rooms on its left as well as right. 
    
    You have to find whether students in all rooms can use wifi.

  Q3: Type it:

    Geek is extremely punctual but today even he is not 
    feeling like doing his homework assignment. 
    He must start doing it immediately 
    in order to meet the deadline. 
    
    For the assignment, 
    Geek needs to type a string s.
    
    To reduce his workload, 
    he has decided to perform one of the following 
    two operations till he gets the string.
    
    Append a character at the end of the string.
    
    Append the string formed thus far to the end of the string. 
    (This can not be done more than once.)
    
    Help Geek find the minimum operations 
    required to type the given string.

Day 63:

  Q1: Subtraction in linked list:

    You are given two linked lists that represent two large positive numbers. 
    From the two numbers represented by the linked lists, 
    subtract the smaller number from the larger one. 
    
    Look at the examples to get a better understanding of the task.

  Q2: K-Pangrams

    Given a string str and an integer K, 
    find whether the string can be changed into a pangram 
    after at most k operations. 
    
    A pangram is a sentence containing every letter 
    in the english alphabet. 
    A single operation can be used to swap an 
    existing alphabetic character with any other alphabetic character.

  Q3: Count Substrings:

    Given a binary string S. 
    The task is to count the number of substrings 
    that starts and end with 1.
    
    Note: The starting and the ending 1s should be different.


Day 64: 

  Q1: Sorted insert for circular linked list:

    Given a sorted circular linked list of length n, 
    the task is to insert a new node in this circular list 
    so that it remains a sorted circular linked list.

  Q2: Min number of flips:

    Given a binary string, that is it contains only 0s and 1s. 
    We need to make this string a sequence of alternate characters 
    by flipping some of the bits, our goal is to minimize the
    number of bits to be flipped.

  Q3: Balanced String:

    Given an integer N.Create a string using only 
    lowercase characters from a to z that follows the given rules.
    
    When N is even:
    
    Use N/2 characters from the beginning of a-z 
    and N/2 characters from the ending of a-z.
    
    When N is greater than 26,
    continue repeating the instructions 
    until length of string becomes N.
    
    When N is odd:
    
    Case 1: If the sum of digits of N is even, 
    Select (N+1)/2 characters from the beginning 
    of a-z and (N-1)/2 characters from the ending of a-z.
    
    Case 2: If the sum of digits of N is odd, 
    Select (N-1)/2 characters from the beginning of a-z 
    and (N+1)/2 characters from the ending of a-z.
    
    When N is greater than 26,
    continue repeating the instructions 
    until length of string becomes N.

Day 65:

  Q1: Rearrange a String:

    Given a string containing uppercase alphabets and 
    integer digits (from 0 to 9), the task is to print 
    the alphabets in the lexicographical order 
    followed by the sum of digits.

  Q2: Count the nodes at distance K from leaf:

    Given a binary tree with n nodes and a non-negative integer k, 
    the task is to count the number of special nodes.
    
    A node is considered special if there exists 
    at least one leaf in its subtree such that the 
    distance between the node and leaf is exactly k.
    
    Note: Any such node should be counted only once. 
    For example, if a node is at a distance k from 2 or more leaf nodes, 
    then it would add only 1 to our count.

  Q3: Meta Strings:

    Given two strings consisting of lowercase english alphabets, 
    the task is to check whether these strings are meta strings or not. 
    Meta strings are the strings which can be made equal 
    by exactly one swap in any of the strings. 
    Equal string are not considered here as Meta strings.


Day 66:

  Q1: Min distance between two given nodes of a binary tree:

    Given a binary tree with n nodes and two node values, 
    a and b, your task is to find the minimum distance between them. 
    The given two nodes are guaranteed to be in the binary tree and 
    all node values are unique.

  Q2: Palindrome Sentence:

    Given a single sentence s, 
    check if it is a palindrome or not. 
    Ignore white spaces and any other character you may encounter. 

  Q3: Count Alphabets:

    Given a string, The task is to count the 
    number of alphabets present in the string.

Day 67:

  Q1: Check if all leaves are at same level:

    Given a binary tree with n nodes, 
    determine whether all the leaf nodes 
    are at the same level or not. 
    
    Return true if all leaf nodes are 
    at the same level, and false otherwise.

  Q2: Amend the Sentence:

    Given a string which is basically a sentence without spaces between words. 
    However the first letter of every word is in uppercase. 
    You need to print this sentence after following amendments:
    
    (i) Put a single space between these words
    
    (ii) Convert the uppercase letters to lowercase.
    
    Note: The first character of the string can be both uppercase/lowercase.

  Q3: Divisible by 8:

    Given a number S, you need to check whether 
    any permutation of the number S divisible by 8 or not. 

Day 68:

  Q1: Check for children sum property in a Binary tree:

    Given a binary tree having n nodes. 
    Check whether all of its nodes have the value 
    equal to the sum of their child nodes. 
    
    Return 1 if all the nodes in the tree 
    satisfy the given properties, else it return 0.
    
    For every node, data value must be equal to the 
    sum of data values in left and right children. 
    Consider data value as 0 for NULL child.  
    Also, leaves are considered to follow the property.

  Q2: Check if the number is balanced:

    Given an integer N which has odd number of digits, 
    find whether the given number is a balanced or not.
    
    An odd digit number is called a balanced number 
    if the sum of all digits to the left of the middle digit 
    and the sum of all digits to the right of the middle digit is equal.

  Q3: Check if a number is divisible by 8:

    Given a string representation of a number S, 
    check if it is divisible by 8.

Day 69:

  Q1: Number of Paths in a matrix with k coins:

    Given a n x n matrix such that each of its cells contains some coins. 
    Count the number of ways to collect exactly k coins while moving 
    from top left corner of the matrix to the bottom right. 
    
    From a cell (i, j), you can only move to (i+1, j) or (i, j+1).

  Q2: Second most repeated string in a sequence:

    Given a sequence of strings, 
    the task is to find out the second most repeated 
    (or frequent) string in the given sequence.
    
    Note: No two strings are the second most repeated, 
    there will be always a single string.

  Q3: Remove all duplicates from a given string:

    Given a string str which may contains lowercase and uppercase chracters. 
    The task is to remove all duplicate characters from the string 
    and find the resultant string. 
    
    The order of remaining characters in the output 
    should be same as in the original string.

Day 70:

  Q1: Racemans Sequence:

    Given an integer n, return the 
    first n elements of Recaman’s sequence.
    
    It is a function with domain and 
    co-domain as whole numbers.
     
    It is recursively defined as below:
    
    Specifically, let a(n) denote the (n+1)th term. 
    (0 being the 1st term).
    The rule says:
    a(0) = 0
    a(n) = a(n-1) - n, if a(n-1) - n > 0 and 
    is not included in the sequence previously
           =  a(n-1) + n otherwise.

  Q2: Convert to Roman No:

    Given an integer n, your task is to complete the function 
    convertToRoman which prints the corresponding roman number of n. 
    Various symbols and their values are given below
    
    Note:- There are a few exceptions for some numbers 
    like 4 in roman is IV,9 in roman is IX, similarly, 
    40 is XL while 90 is XC. Similarly, 
    400 is CD while 900 is CM
    
    I 1
    V 5
    X 10
    L 50
    C 100
    D 500
    M 1000

  Q3: Print Bracket Number:

    Given a string S, the task is to find the bracket numbers. 

Day 71:

  Q1: Recursive Sequence:

    Given a string S that consists of only 
    alphanumeric characters and dashes. 
    The string is separated into N + 1 
    groups by N dashes. 
    
    Also given an integer K. 
    
    We want to reformat the string S, 
    such that each group contains exactly K characters, 
    except for the first group, which could be shorter than K 
    but still must contain at least one character. 
    
    Furthermore, there must be a dash inserted between two groups, 
    and you should convert all lowercase letters to uppercase.
    
    Return the reformatted string.

  Q2: Reversing the equation:

    A function F is defined as follows F(n)= (1) +(2*3) + (4*5*6) ... 
    upto n terms (look at the examples for better clarity). 
    
    Given an integer n, determine the F(n).
    
    Note: As the answer can be very large, 
    return the answer modulo 10^9+7.

  Q3: License Key Formatting:

    Given a string S that consists of only 
    alphanumeric characters and dashes. 
    The string is separated into N + 1 
    groups by N dashes. 
    
    Also given an integer K. 
    
    We want to reformat the string S, 
    such that each group contains exactly K characters, 
    except for the first group, which could be shorter than K 
    but still must contain at least one character. 
    
    Furthermore, there must be a dash inserted between two groups, 
    and you should convert all lowercase letters to uppercase.
    
    Return the reformatted string.

Day 72:

  Q1: Clone an Undirected Graph:

    Given a connected undirected graph with n nodes and m edges, 
    with each node having a distinct label from 0 to n-1, 
    create a clone of the graph. 
    
    Each node in the graph contains an integer val 
    and an array (neighbors) of nodes, 
    containing nodes that are adjacent to the current node.
    
    Note: If the user returns a correct copy of the given graph, 
    then the system will print 1; in the case when an incorrect 
    copy is generated or when the user returns the original node, 
    the system will print 0.
    
    For Example :    
    
    class Node {
        val: integer
        neighbors: List[Node]
    }

  Q2: Minimum indexed Character:

    Given a string str and another string patt. 
    Find the minimum index of the character in 
    str that is also present in patt.

  Q3: Find first repeated Character:

    Given a string S. The task is to find the 
    first repeated character in it. 
    
    We need to find the character that occurs 
    more than once and whose index of 
    second occurrence is smallest. 
    S contains only lowercase letters.


Day 73:

  Q1: Find all critical connections in the graph:

    A critical connection refers to an edge that, 
    upon removal, will make it impossible for certain nodes 
    to reach each other through any path. You are given an 
    undirected connected graph with v vertices and 
    e edges and each vertex distinct and ranges from 0 to v-1, 
    and you have to find all critical connections in the graph. 
    It is ensured that there is at least one such edge present.
    
    Note: The answers may be presented in various potential orders. 
    Each edge should be displayed in sorted order. For instance, 
    if there's an edge between node 1 and node 2, 
    it should be stored as (1,2) rather than (2,1). 
    
    Additionally, it is expected that you 
    store the edges in sorted order.

  Q2: N meetings in one room:

    There is one meeting room in a firm. 
    There are N meetings in the form of (start[i], end[i]) where start[i] 
    is start time of meeting i and end[i] is finish time of meeting i.
    
    What is the maximum number of meetings that can be accommodated 
    in the meeting room when only one meeting can be held in 
    the meeting room at a particular time?
    
    Note: Start time of one chosen meeting can't be 
    equal to the end time of the other chosen meeting.

  Q3: Floor in a Sorted Array:

    Given a sorted array arr[] of size N without duplicates, 
    and given a value x. Floor of x is defined as the 
    largest element K in arr[] such that K is smaller than 
    or equal to x. Find the index of K(0-based indexing).


Day 74:

  Q1: Count all Possible Path:

    You are presented with an undirected connected graph 
    consisting of n vertices and connections between them 
    represented by an adjacency matrix. Your objective is 
    to determine whether it is possible to start traversing 
    from a node, x, and return to it after traversing 
    all the vertices at least once, using each edge exactly once.

  Q2: Check for BST:

    Given the root of a binary tree. 
    Check whether it is a BST or not.
    Note: We are considering that BSTs 
    can not contain duplicate Nodes.
    
    A BST is defined as follows:
    
    The left subtree of a node contains only nodes 
    with keys less than the node's key.
    
    The right subtree of a node contains only nodes 
    with keys greater than the node's key.
    
    Both the left and right subtrees must 
    also be binary search trees.

  Q3: Detect Loop in linked list:
  
    Given a linked list of N nodes. 
    The task is to check if the linked list has a loop. 
    Linked list can contain self loop.
