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


Day 75:

  Q1: Flatten BST to sorted list:

    You are given a Binary Search Tree (BST) with n nodes, 
    each node has a distinct value assigned to it. 
    
    The goal is to flatten the tree such that, 
    the left child of each element points to nothing (NULL), 
    and the right child points to the next element in the 
    sorted list of elements of the BST (look at the examples for clarity). 
    
    You must accomplish this without using any extra storage, 
    except for recursive calls, which are allowed.
    
    Note: If your BST does have a left child, 
    then the system will print a -1 and will skip it, 
    resulting in an incorrect solution.

  Q2: Easy String:

    You are given the string S. 
    Compress the string when lower and upper cases are the same. 
    In compressed string characters should be in lowercase.

  Q3: Special array Reversal:

    Given a string S, containing special characters a
    nd all the alphabets, reverse the string without
    affecting the positions of the special characters.


Day 76:

  Q1: Does array represent Heap:

    Given an array arr of size n, 
    the task is to check if the given array can 
    be a level order representation of a Max Heap.

  Q2: Left view of Binary Tree:

    Given a Binary Tree, return Left view of it. 
    Left view of a Binary Tree is set of nodes visible 
    when tree is visited from Left side. 
    The task is to complete the function leftView(), 
    which accepts root of the tree as argument. 
    If no left view is possible, return an empty tree.
    
    Left view of following tree is 1 2 4 8.
    
              1
           /     \
         2        3
       /     \    /    \
      4     5   6    7
       \
         8   

  Q3: Reverse a linked list:

    Given a linked list of N nodes. 
    The task is to reverse this list.

Day 77:

  Q1: Arya's Long String:

    Arya has a string, s, of uppercase English letters. 
    She writes down the string s on a paper k times. 
    She wants to calculate the occurence of a specific letter  
    in the first n characters of the final string.

  Q2: Closing bracket index:

    Given a string with brackets ('[' and ']') and 
    the index of an opening bracket. 
    
    Find the index of the corresponding closing bracket.

  Q3: Sum of leaf nodes in BST:

    Given a Binary Search Tree with n nodes, 
    find the sum of all leaf nodes. 
    BST has the following property (duplicate nodes are possible):
    
    The left subtree of a node contains 
    only nodes with keys less than the node’s key.
    
    The right subtree of a node contains only nodes 
    with keys greater than or equal to the node’s key.
    
    Your task is to determine the total sum 
    of the values of the leaf nodes.
    
    Note: Input array arr doesn't represent the actual BST, 
    it represents the order in which the elements will be added into the BST.


Day 78:

  Q1: Game with String:

    Given a string s of lowercase alphabets and a number k, 
    the task is to print the minimum value of the string 
    after removal of k characters. 
    
    The value of a string is defined as the sum of squares 
    of the count of each distinct character present in the string. 

  Q2: The Modified String:

    Ishaan is playing with strings these days. 
    He has found a new string. 
    He wants to modify it as per the 
    following rules to make it valid:
    
    The string should not have three 
    consecutive same characters 
    (Refer example for explanation).
    
    He can add any number of characters 
    anywhere in the string. 
    
    Find the minimum number of characters which 
    Ishaan must insert in the string to make it valid.

  Q3: Pattern Searching:

    Given a text and a pattern, 
    the task is to check if the pattern 
    exists in the text or not.

Day 79:

  Q1: Word Break:

    Given a string s and a dictionary of n words dictionary, 
    find out if a s can be segmented into a space-separated 
    sequence of dictionary words. 
    
    Return 1 if it is possible to break the s into 
    a sequence of dictionary words, else return 0. 
    
    Note: From the dictionary dictionary each word 
    can be taken any number of times and in any order.

  Q2: Count the Substrings:

    Given a string S. 
    The task is to count the number of substrings which contains 
    equal number of lowercase and uppercase letters. 

  Q3: Match specific pattern:

    Given a dictionary of words and a pattern. 
    Every character in the pattern is uniquely mapped 
    to a character in the dictionary. 
    
    Find all such words in the dictionary 
    that match the given pattern. 

Day 80:

  Q1: Boolean Parenthesization:

    Given a boolean expression s of length n with following symbols.
    Symbols
        'T' ---> true
        'F' ---> false
    and following operators filled between symbols
    Operators
        &   ---> boolean AND
        |   ---> boolean OR
        ^   ---> boolean XOR
    Count the number of ways we can parenthesize the expression 
    so that the value of expression evaluates to true.
    
    Note: The answer can be large, 
    so return it with modulo 1003

  Q2: Divisible by 7:

    Given an n-digit large number in form of string, 
    check whether it is divisible by 7 or not. 
    Print 1 if divisible by 7, otherwise 0.

  Q3: Prime String:

    Provided a String of length N, your task is to find out 
    whether or not the given string is a prime string. 
    
    A prime string is a string in which the sum of the 
    ASCII value of all the characters is prime.

Day 81:

  Q1: Distinct Occurences:

    Given two strings s and t of length n and m respectively. 
    Find the count of distinct occurrences of t in 
    s as a sub-sequence modulo 10^9 + 7.

  Q2: Pangram Strings:

    Check if the given string S is a Panagram or not. 
    A pangram is a sentence containing every 
    letter in the English Alphabet.

  Q3: Common Subsequence: 

    Given two strings a and b. 
    Check whether they contain any 
    common subsequence (non empty) or not.


Day 82:

  Q1: Distinct Occurences:

    Given two strings s and t of length n and m respectively. 
    Find the count of distinct occurrences of t in 
    s as a sub-sequence modulo 10^9 + 7.

  Q2: Pangram Strings:

    Check if the given string S is a Panagram or not. 
    A pangram is a sentence containing every 
    letter in the English Alphabet.

  Q3: Common Strings:

    Given two strings a and b. 
    Check whether they contain any 
    common subsequence (non empty) or not.


Day 83:

  Q1: Maximum Sum Problem:

    A number n can be broken into three parts n/2, n/3, and n/4 
    (consider only the integer part). 
    
    Each number obtained in this process can be divided further recursively. 
    
    Find the maximum sum that can be obtained by 
    summing up the divided parts together.
    
    Note: It is possible that we don't divide the number at all.

  Q2: String Modification:

    Given a string with repeated characters, 
    the task is to complete the function rearrangeString 
    which rearrange characters in a string so that 
    no two adjacent characters are same.
    
    Note : It may be assumed that the string has only lowercase 
    English alphabets and such transformation is always always possible.

  Q3: Last Match:

    Given two strings A and B, 
    you need to find the last occurrence 
    ( 1 based indexing) of string B in string A.


Day 84:

  Q1: Reach a given score:

    Consider a game where a player can score 3 or 5 
    or 10 points in a move. 
    Given a total score n, 
    find number of distinct combinations 
    to reach the given score.

  Q2: Difficulty of sentence:

    Given a sentence as a string S. 
    
    Calculate difficulty of a given sentence.
    
    Difficulty of sentence is defined as 5*(number of hard words) + 
    3*(number of easy words). 
    
    A word in the given string is considered hard 
    if it has 4 consecutive consonants or number of consonants 
    are more than number of vowels. 
    
    Else the word is easy.
    
    Note: uppercase and lowercase characters are same.

  Q3: Odd Even Problem:

    Given a string S of lowercase english characters, 
    find out whether the summation of X and Y is even or odd, 
    where X is the count of distinct characters which occupy 
    even positions in english alphabets and 
    have positive even frequency, and Y is the count of 
    distinct characters which occupy odd positions 
    in english alphabets and have positive odd frequency.
    
    Note: Positive means greater than zero.

Day 85:

  Q1: Power Set:

    Given a string s of length n, 
    find all the possible subsequences of the string s 
    in lexicographically-sorted order.

  Q2: Count number of words:

    Given a string consisting of spaces,\t,\n and lower case  
    alphabets.Your task is to count the number of words 
    where spaces,\t and \n work as separators.

  Q3: Replace a word:

    Given three strings S, oldW and newW. 
    
    Find all occurrences of the word oldW 
    in S and replace them with word newW.

Day 86:

  Q1: Play with OR:

    You are given an array arr[] of length n, 
    you have to re-construct the same array arr[] in-place. 
    The arr[i] after reconstruction will become arr[i] OR arr[i+1], 
    where OR is bitwise or. If for some i, 
    i+1 does not exists, then do not change arr[i].

  Q2: Longest common prefix:

    Given two strings str1 and str2 of the same length. 
    Find the longest prefix of str1 which is common in str2.

  Q3: Generate binary string:

    Given a string containing of 0, 1 and ? - a wildcard character, 
    generate all distinct binary strings that can be formed by 
    replacing each wildcard character by either 0 or 1.

Day 87:

  Q1: Check if a number is divisible by 8:

    Given a string representation of a decimal number s, 
    check whether it is divisible by 8.

  Q2: Minimal moves to form a string:

    Given a string S, check if it is possible to construct the 
    given string S by performing any of the 
    below operations any number of times. 
    
    In each step, we can:
    
    Add any character at the end of the string.
    or, append the string to the string itself.
    
    The above steps can be applied any number of times. 
    
    The task is to find the minimum steps required to form the string.

  Q3: Next greater even number:

    Given a positive integer X. 
    The task is to find the smallest 
    even number E such that
    E > X and all digits in 
    X and E are the same.
    
    Note: All the digits in X should 
    be same with digits in E.

Day 88: 

  Q1: Sum of bit differences:

    Given an array integers arr[], containing n elements, 
    find the sum of bit differences between 
    all pairs of element in the array. 
    
    Bit difference of a pair (x, y) is the count of 
    different bits at the same positions in
    binary representations of x and y.
    
    For example, bit difference for 2 and 7 is 2. 
    
    Binary representation of 2 is 010 and 7 is 111 respectively 
    and the first and last bits differ between the two numbers.
    
    Note: (x, y) and (y, x) are considered two separate pairs.

  Q2: Distinct Substrings:

    Given a string s consisting of uppercase and 
    lowercase alphabetic characters. 
    
    Return the  number of distinct substrings 
    of size 2 that appear in s as contiguous substrings.
    
  Q3: Colorful Strings: 

    Find the count of all possible strings of size n.
    Each character of the string is either ‘R’, ‘B’ or ‘G’.
     
    In the final string there needs to be at least r number of ‘R’, 
    at least b number of ‘B’ and at least g 
    number of ‘G’ (such that r + g + b <= n). 

Day 89:

  Q1: Count even substrings:

    Given a string of digits 0 – 9. 
    The task is to count the number of substrings 
    which when converting into integer form an even number.

  Q2: Peak Element:

    Given an 0-indexed array of integers arr[] of size n, 
    find its peak element. 
    
    An element is considered to be peak if it's value 
    is greater than or equal to the values 
    of its adjacent elements (if they exist).
    
    Note: The output will be 1 if the index returned 
    by your function is correct; otherwise, it will be 0.

  Q3: Divisible by 5 or not:

    The problem is to check whether the decimal representation 
    of a given binary number is divisible by 5 or not.

Day 90:

  Q1: First element to occur k times:

    Given an array of n integers. 
    Find the first element that occurs atleast k number of times. 
    If no such element exists in the array, 
    then expect the answer to be -1.

  Q2: Large number division:

    Given a large number (represented as string S)  
    which has to divided by another number 
    (represented as int data type D). 
    The task is to find division of these numbers.

  Q3: Smallest number in one swap:

    Given a non-negative number N. The task is to apply 
    at most one swap operation on the number N 
    so that the result is the smallest possible number.
    
    Note: Input and Output should not contain leading zeros.

Day 91:

  Q1: Largest Number formed from an Array:

    Given an array of strings arr[] of length n 
    representing non-negative integers, 
    arrange them in a manner, such that, 
    after concatanating them in order, 
    it results in the largest possible number. 
    
    Since the result may be very large, 
    return it as a string.

  Q2: Decode It:

    An encoded string S consisting of alphabets(lowercase) 
    and integers(1<=num<=9) is given, 
    the task is to decode it and print the character 
    at the 'K'th position in the string. 
    
    The pattern in which the strings were encoded were as follows :\
    
    original string: jonjonsnowjonjonsnowjonjonsnow
    encoded string: jon2snow3
    
    Note: encoded string will always start 
    with an alphabet and end with a number.

  Q3: Palindromic Series:

    Adobe wants to play a game. 
    He is given a number N. He has to create a alphabetical string 
    in lower case from that number and 
    tell whether the string is palindrome or not. 
    a = 0 , b = 1….. and so on.  
    
    For eg : If the number is 61 the substring 
    “gb” will be printed till 7 (6+1) characters i.e. 
    “gbgbgbg” and check if palindrome or not. 
    Adobe is weak in concepts of palindrome and strings, 
    help him in winning the game.
    
    Note: No number will start with zero. 
    Consider alphabets ' a to j ' only i.e. 
    single digit numbers from 0 to 9.

Day 92:

  Q1: Swap the array elements:

    Given an array arr of n positive integers. 
    The task is to swap every ith element of 
    the array with (i+2)th element.

  Q2: RegEx matching:

    Given a pattern string and a test string, 
    If the pattern is preceded by a ^, 
    the pattern(excluding the ^) will be matched 
    with the starting position of the text string. 
    Similarly, if it is preceded by a $, 
    the pattern(excluding the ^) will be matched 
    with the ending position of the text string. 
    
    If no such markers are present, 
    it will be checked whether pattern 
    is a substring of test.

  Q3: Divisibility by 999:

    You are given a large number N in the form of a string, 
    you have to check whether it is divisible by 999 
    without dividing or finding modulo of number by 999.

Day 93:

  Q1: Maximum Index:

    Given an array a of n positive integers. 
    The task is to find the maximum of j - i 
    subjected to the constraint of a[i] < a[j] and i < j.

  Q2: Unusual String Sort:

    Given a string composed of both lowercase and uppercase letters. 
    Sort it in such a manner such that the uppercase and 
    lowercase letter comes in an alternate manner but in sorted way.

  Q3: Reverse alternate words:

    Given a string str consisting of multiple words, 
    reverse alternate words in str. 

Day 94:

  Q1: Search Pattern (Rabin-Karp Algorithm):

    Given two strings, one is a text string 
    and other is a pattern string. 
    The task is to print the indexes of all the 
    occurences of pattern string in the text string. 
    
    For printing, Starting Index of a string should be taken as 1. 
    
    The strings will only contain lowercase English alphabets ('a' to 'z').

  Q2: Split the String:

    Given a string S, you have to check if 
    we can split it into four strings such that 
    each string is non-empty and distinct from each other.

  Q3: Palindromic Sequences:

    Given a Binary String S (the string that contains only 0's and 1's). 
    
    Find the minimum number of palindromic subsequences 
    that are needed to be removed such that string S becomes empty.

Day 95:

  Q1: Longest repeating and non-overlapping substring:

    Given a string s of length n, find the longest repeating 
    non-overlapping substring in it. In other words 
    find 2 identical substrings of maximum length which do not overlap. 
    
    Return the longest non-overlapping substring. 
    
    Return "-1" if no such string exists.
    
    Note: Multiple Answers are possible but you have to 
    return the substring whose first occurrence is earlier.
    
    For Example: "abhihiab", here both "ab" and "hi" 
    are possible answers. But you will have to return "ab" 
    because it's first occurrence appears 
    before the first occurrence of "hi".

  Q2: String comparison:

    In a native language, the increasing order of priority 
    of characters is a, b, c, d, e, f, g, h, i, j, k, l, m, 
    n, ng, o, p, q, r, s, t, u, v, w, x, y, z. 
    
    You are given two strings s1 and s2 and 
    your task is to compare them on the basis 
    of the given priority order.
    
    Note: Function must return 0 if both the strings are equal, 
    1 if s1 is greater than s2, and -1 if s1 is lesser than s2.

  Q3: Word with maximum frequency:

    You are given a string that is made up of 
    words separated by spaces. 
    
    Your task is to find the word with highest frequency, 
    i.e. it appears maximum times in the sentence. 
    
    If multiple words have maximum frequency, 
    then print the word that occurs first in the sentence.

Day 96:

  Q1: Check if frequencies can be equal:

    Given a string s which contains only lower alphabetic characters, 
    check if it is possible to remove at most one character 
    from this string in such a way that frequency of each distinct 
    character becomes same in the string. 
    
    Return true if it is possible to do else return false.
    
    Note: The driver code print 1 if the 
    value returned is true, otherwise 0.

  Q2: The Even Array:

    Given a string contains 'E' and 'O', 'E' 
    represents a number is even and 'O' 
    represents a number is odd. 
    
    To make an element even, you can add 1 
    to any odd element of the array. 
    
    Also, when any element of the array is converted to even, 
    any neighboring element which is odd, 
    can also be made even without adding 1. 
    
    The task is to find the minimum number of 
    additions required to make all the elements even.

  Q3: The Non-repetitive String:

    Given a string S, the task is to check if a 
    string is a non-repetitive or not.  
    
    A non-repetitive string is defined as a string 
    that does not contain any different character 
    between two same characters

Day 97: 

  Q1: Find the N-th character:

    Given a binary string s. Perform r iterations on string s, 
    where in each iteration 0 becomes 01 and 1 becomes 10. 
    Find the nth character (considering 0 based indexing) 
    of the string after performing these r iterations 
    (see examples for better understanding).

  Q2: Does robot moves circular:

    Given a sequence of moves for a robot. 
    Check if the sequence is circular or not.
    
    A sequence of moves is circular if the first and 
    last positions of the robot are the same. 
    A move can be one of the following :
    
        G - Go one unit
        L - Turn left
        R - Turn right

  Q3: Generate Grey Code Sequences:

    Given a number N, your task is to complete the function 
    which generates all n-bit grey code sequences, 
    a grey code sequence is a sequence such that 
    successive patterns in it differ by one bit.

Day 98:

  Q1: Minimum Indexed Character:

    Given a string S and another string patt. 
    Find the character in patt that is 
    present at the minimum index in S.

  Q2: Remove all duplicates from a given string:

    Given a string str which may contain lowercase 
    and uppercase characters. The task is to remove 
    all duplicate characters from the string and 
    find the resultant string. 
    
    The order of remaining characters in the 
    output should be same as in the original string.

  Q3: Find the most frequent digit:

    Given a number N, find the most occurring digit in it. 
    
    If two or more digits occur same number of times, 
    then return the highest of them. 
    
    Input number is given as a string.

Day 99:

  Q1: Mr Binary:
  
    Given a string S containing lowercase English alphabets. 
    Initially, you are at index 1. 
    You can only jump to some other location j (j>i) 
    only if s[j] = s[i] + 1. 
    
    Find the maximum index you can reach.
    
    Note: First character of the string is always 'a'. 
    He can only go 'a'->'b','b'->'c','c'->'d' and so on. 
    'a'->'c','b'->'d','b'->'a' is not a valid move. 
    He can start from any of index of 'a'. 
    Indexing is zero based.

  Q2: Count pairs Sum in matrices:

    Given two sorted matrices mat1 and mat2 
    of size n x n of elements. 
    
    Each matrix contains numbers arranged in 
    strictly ascending order, 
    with each row sorted from left to right, 
    and the last element of a row being smaller 
    than the first element of the next row. 
    
    You're given a target value, x, your task is to find 
    and count all pairs {a, b} such that a is from mat1 
    and b is from mat2 where sum of a and b is equal to x.

  Q3: Common Subsequence OldP:

    Given two strings S1 and S2 print whether they 
    contain any common subsequence (non empty) or not.
    
    NOTE: Print 1 if they have a 
    common subsequence (non empty) else 0.

Day 100:

  Q1: Generalised Fibonacci numbers:

    Consider the generalized Fibonacci number g, 
    which is dependent on a, b and c as follows :-
    
    g(1) = 1, g(2) = 1. 
    For any other number n, 
    g(n) = a*g(n-1) + b*g(n-2) + c.
    
    For a given value of m, determine g(n)%m.

  Q2: Same characters in two strings:

    Given two strings A and B of equal length, 
    find how many times the corresponding position 
    in the two strings hold exactly the same character. 
    
    The comparison should not be case sensitive. 

  Q3: Convert the string:

    Given string str, transform it according to the following rules:
    
    Delete all the vowels from the string.
    
    Insert # in front of all the consonants.
    
    Change the case of all the letters of the string. 

Day 101:

  Q1: Print matrix in diagonal pattern:

    Given a square matrix mat[][] of n*n size, 
    the task is to determine the diagonal pattern 
    which is a linear arrangement of the elements 
    of the matrix.

  Q2: Largest number in one swap:

    Given a non-negative number N in the form of a string.
    
    Find the largest number that can be formed 
    by swapping two characters at most once.

  Q3: Three consecutive duplicates:

    Given a string S, in an operation you can remove 3 
    consecutive characters which are duplicates and 
    concatenate the rest string. 
    
    You can perform this operation any number of times. 
    Find the reduced string.
    
    Note: Return '-1' if the string is 
    empty after removing the duplicates.

Day 102:

  Q1: Check for Balanced Tree:

    Given a binary tree, find if it is height balanced or not. 
    
    A tree is height balanced if difference between heights 
    of left and right subtrees is not more than one 
    for all nodes of tree.

  Q2: Largest subsquare surrounded by X:

    Given a square matrix a of size n x n, 
    where each cell can be either 'X' or 'O', 
    you need to find the size of the largest square 
    subgrid that is completely surrounded by 'X'. 
    
    More formally you need to find the largest square 
    within the grid where all its border cells are 'X'.

  Q3: Nth node from front end of linked list:

    Given a linked list consisting of L nodes and given a number N. 
    The task is to find the Nth node from the end of the linked list.

Day 103:

  Q1: Linked List that is sorted Alternatingly:

    You are given a Linked list of size n. 
    The list is in alternating ascending and descending orders. 
    Sort the given linked list in non-decreasing order.

  Q2: Pythagorean Triplet:

    Given an array arr of n integers, 
    write a function that returns true if there is a 
    triplet (a, b, c) from the array (where a, b, and c are on different indexes) 
    that satisfies a^2 + b^2 = c^2, 
    otherwise return false.

  Q3: Maximum Index:

    Given an array arr[] of n non-negative integers. 
    The task is to find the maximum of j - i (i<=j) 
    subjected to the constraint of arr[i] <= arr[j].

Day 104:

  Q1: Delete without head pointer:

    You are given a node del_node of a Singly Linked List 
    where you have to delete a value of the given node 
    from the linked list but you are not given the head of the list.
    
    By deleting the node value, 
    we do not mean removing it from memory. We mean:
    
    The value of the given node should not exist in the linked list.
    The number of nodes in the linked list should decrease by one.
    All the values before & after the del_node node should be in the same order.
    
    
    Note:
    
    Multiple nodes can have the same values as the del_node, 
    but you must only remove the node whose 
    pointer del_node is given to you.
    
    It is guaranteed that there exists a node with a value 
    equal to the del_node value and it will 
    not be the last node of the linked list.

  Q2: Height of Binary Tree:

    Given a binary tree, find its height.

  Q3: DFS of Graph:

    You are given a connected undirected graph. 
    
    Perform a Depth First Traversal of the graph.
    
    Note: Use the recursive approach to find the 
    DFS traversal of the graph starting from the 
    0th vertex from left to right according to the graph.

Day 105:

  Q1: Count Pairs whose sum is equal to X:

    Given two linked list head1 and head2 with distinct elements, 
    determine the count of all distinct pairs from 
    both lists whose sum is equal to the given value x.
    
    Note: A valid pair would be in the form (x, y) 
    where x is from first linked list and 
    y is from second linked list.

  Q2: Permutation divisibility:

    You are given a number. 
    Your task is to check if there exists a permutation 
    of the digits of this number which is divisible by 4. 

  Q3: Convertible string:

    Given two strings check whether first string 
    could be converted to the second string but the conditions are:
    
    1.If the character is at odd place you can swap 
    this character with the characters only 
    at the odd places in the given first string.
    
    2.If the character is at even place you can swap 
    this character with the characters only at the even places      
    in the given first string.
    
    3.You cannot insert or delete any character on your own.

Day 105: 

  Q1: Count pairs whose sum is equal to X:

    Given two linked list head1 and head2 with distinct elements, 
    determine the count of all distinct pairs from 
    both lists whose sum is equal to the given value x.
    
    Note: A valid pair would be in the form (x, y) 
    where x is from first linked list and 
    y is from second linked list.

  Q2: Permutation divisibility:

    You are given a number. 
    Your task is to check if there exists a permutation 
    of the digits of this number which is divisible by 4. 

  Q3: Convertible string:

    Given two strings check whether first string 
    could be converted to the second string but the conditions are:
    
    1.If the character is at odd place you can swap 
    this character with the characters only 
    at the odd places in the given first string.
    
    2.If the character is at even place you can swap 
    this character with the characters only at the even places      
    in the given first string.
    
    3.You cannot insert or delete any character on your own.

Day 106:

  Q1: Level order traversal:

    Given a root of a binary tree with n nodes, 
    find its level order traversal.
    
    Level order traversal of a tree 
    is breadth-first traversal for the tree.

  Q2: Perfect Sum Problem:

    Given an array arr of non-negative integers and an integer sum, 
    the task is to count all subsets of the given array 
    with a sum equal to a given sum.
    
    Note: Answer can be very large, so, output answer modulo 10^9+7.

  Q3: Row with max 1's:

    Given a boolean 2D array of n x m dimensions, 
    consisting of only 1's and 0's, where each row is sorted. 
    
    Find the 0-based index of the first row 
    that has the maximum number of 1's.

Day 107: 

  Q1: Possible Paths in a Tree:

    Given a weighted tree with n nodes and (n-1) edges. 
    You are given q queries. Each query contains a number x. 
    
    For each query, find the number of paths in 
    which the maximum edge weight is less than or equal to x.
    
    Note: Path from A to B and B to A are considered to be the same.

  Q2: Chocolate Distribution Problem:

    Given an array A[ ] of positive integers of size N, 
    where each value represents the number of chocolates in a packet. 
    Each packet can have a variable number of chocolates. There are M students, 
    the task is to distribute chocolate packets among M students such that :
    
    1. Each student gets exactly one packet.
    
    2. The difference between maximum number of chocolates given 
    to a student and minimum number of chocolates given to a student is minimum.

  Q3: Minimum Cost

    There are given N ropes of different lengths, 
    we need to connect these ropes into one rope. 
    
    The cost to connect two ropes is equal to sum of their lengths.
    
    The task is to connect the ropes with minimum cost. 
    Given N size array arr[] contains the lengths of the ropes.

Day 108:

  Q1: Sum of nodes on the longest path from root to leaf node:

    Given a binary tree having n nodes. 
    Find the sum of all nodes on the longest path 
    from root to any leaf node. If two or more paths 
    compete for the longest path, then the path having 
    maximum sum of nodes will be considered.

  Q2: Remove duplicates from an unsorted linked list:

    Given an unsorted linked list of N nodes. 
    The task is to remove duplicate elements 
    from this unsorted Linked List. 
    
    When a value appears in multiple nodes, 
    the node which appeared first should be kept, 
    all others duplicates are to be removed.

  Q3: Sum Tree:

    Given a Binary Tree. Return true if, 
    for every node X in the tree other than the leaves, 
    its value is equal to the sum of its left subtree's value 
    and its right subtree's value. 
    
    Else return false.
    
    An empty tree is also a Sum Tree as the sum of an 
    empty tree can be considered to be 0. 
    
    A leaf node is also considered a Sum Tree.

Day 109:

  Q1: ZigZag Tree Traversal:

    Given a binary tree with n nodes. 
    
    Find the zig-zag level order traversal 
    of the binary tree.

  Q2: Next Greater Element:

    Given an array arr[ ] of size N having elements, 
    the task is to find the next greater element for 
    each element of the array in order of their 
    appearance in the array.
    
    Next greater element of an element in the array 
    is the nearest element on the right which is 
    greater than the current element.
    
    If there does not exist next greater of current element, 
    then next greater element for current element is -1.
    For example, next greater of the last element is always -1.

  Q3: Longest Palindrome in a String:

    Given a string S, 
    find the longest palindromic substring in S. 
    Substring of string S: S[ i . . . . j ] 
    where 0 ≤ i ≤ j < len(S). 
    
    Palindrome string: A string that reads the same backward. 
    More formally, S is a palindrome if reverse(S) = S. 
    
    In case of conflict, 
    return the substring which occurs first 
    ( with the least starting index).

Day 110:

  Q1: Diagonal sum in binary tree:

    Consider Red lines of slope -1 
    passing between nodes (in following diagram). 
    
    The diagonal sum in a binary tree is the 
    sum of all node datas lying between these lines. 
    
    Given a Binary Tree of size n, 
    print all diagonal sums.
    
    For the following input tree, output should be 9, 19, 42.
    9 is sum of 1, 3 and 5.
    19 is sum of 2, 6, 4 and 7.
    42 is sum of 9, 10, 11 and 12.
    
    DiagonalSum

  Q2: Find All Four Sum Numbers:

    Given an array A of integers and another number K. 
    Find all the unique quadruple from the 
    given array that sums up to K.
    
    Also note that all the quadruples 
    which you return should be internally sorted, 
    ie for any quadruple [q1, q2, q3, q4] 
    the following should follow: q1 <= q2 <= q3 <= q4.

  Q3: Longest Common Substring:

    Given two strings. 
    The task is to find the length 
    of the longest common substring.

Day 111:

  Q1: Fibonacci series up to Nth term:

    You are given an integer n, 
    return the fibonacci series 
    till the nth(0-based indexing) term. 
    Since the terms can become very large 
    return the terms modulo 10^9+7.

  Q2: Right View of Binary Tree:

    Given a Binary Tree, find Right view of it. 
    Right view of a Binary Tree is set of nodes 
    visible when tree is viewed from right side.
    
    Right view of following tree is 1 3 7 8.
    
              1
           /     \
         2        3
       /   \      /    \
      4     5   6    7
        \
         8

  Q3: Roman Number to Integer:

    Given a string in roman no format (s)  
    your task is to convert it to an integer. 
    
    Various symbols and their values are given below.
    
    I 1
    V 5
    X 10
    L 50
    C 100
    D 500
    M 1000

Day 112:

  Q1: Insert an Element at the Bottom of a Stack:

    You are given a stack st of n integers and an element x. 
    You have to insert x at the bottom of the given stack. 
    
    Note: Everywhere in this problem, 
    the bottommost element of the stack is 
    shown first while priniting the stack.

  Q2: Top View of Binary Tree:

    Given below is a binary tree. 
    The task is to print the top view of binary tree. 
    Top view of a binary tree is the set of nodes visible 
    when the tree is viewed from the top. 
    
    For the given below tree
    
           1
        /     \
       2       3
      /  \    /   \
    4    5  6   7
    
    Top view will be: 4 2 1 3 7
    
    Note: Return nodes from leftmost node to rightmost node. 
    Also if 2 nodes are outside the shadow of the tree 
    and are at same position then consider the left ones only(i.e. leftmost). 
    
    For ex - 1 2 3 N 4 5 N 6 N 7 N 8 N 9 N N N N N 
    
    will give 8 2 1 3 as answer. 
    Here 8 and 9 are on the same position 
    but 9 will get shadowed.

  Q3: Diameter of a Binary Tree:

    The diameter of a tree (sometimes called the width) 
    is the number of nodes on the longest path 
    between two end nodes. 
    
    The diagram below shows two trees 
    each with diameter nine, 
    the leaves that form the ends 
    of the longest path are shaded 
    
    (note that there is more than one path 
    in each tree of length nine, 
    but no path longer than nine nodes). 

Day 113:

  Q1: Print N-bit binary numbers having more 1s than 0s:

    Given a positive integer n. 
    
    Your task is to generate a string list 
    of all n-bit binary numbers where, 
    for any prefix of the number, 
    there are more or an equal number of 1's than 0's.
     
    The numbers should be sorted in 
    decreasing order of magnitude.

  Q2: Largest subarray with 0 sum:

    Given an array having both positive and negative integers.
     
    The task is to compute the length of the 
    largest subarray with sum 0.

  Q3: Longest Common Subsequence:

    Given two strings, 
    find the length of longest subsequence 
    present in both of them. 
    
    Both the strings are in 
    uppercase latin alphabets.

Day 114:

  Q1: Additive Sequence:

    Given a string n, your task is to find whether 
    it contains an additive sequence or not. 
    
    A string n contains an additive sequence 
    if its digits can make a sequence of numbers 
    in which every number is addition of previous two numbers. 
    
    You are required to complete the function 
    which returns true if the string is a 
    valid sequence else returns false. 
    
    For better understanding check the examples.
    
    Note: A valid string should contain at least 
    three digit to make one additive sequence. 

  Q2: Insert a node in a BST:

    Given a BST and a key K. 
    
    If K is not present in the BST, 
    Insert a new Node with a value equal to K into the BST.
     
    If K is already present in the BST, don't modify the BST.

  Q3: Symmetric Tree:

    Given a Binary Tree. 
    
    Check whether it is Symmetric or not, 
    i.e. whether the binary tree is a 
    Mirror image of itself or not.

Day 115:

  Q1: Find shortest safe route in a matrix:

    Given a matrix mat[][] with r rows and c columns, 
    where some cells are landmines (marked as 0) 
    and others are safe to traverse. 
    
    Your task is to find the shortest safe route 
    from any cell in the leftmost column to any cell 
    in the rightmost column of the mat. 
    
    You cannot move diagonally, 
    and you must avoid both the landmines and 
    their adjacent cells (up, down, left, right), 
    as they are also unsafe.

  Q2: Count number of hops:

    A frog jumps either 1, 2, or 3 steps to go to the top.
     
    In how many ways can it reach the top of Nth step. 
    
    As the answer will be large find the answer modulo 1000000007.

  Q3: Count Digits:

    Given a number N. Count the number of digits in N which evenly divide N.
    
    Note :- Evenly divides means whether N is divisible by a digit 
    i.e. leaves a remainder 0 when divided.

Day 116:

  Q1: City with the smallest number of neighbours at threshold distance:

    There are n cities labeled from 0 to n-1 
    with m edges connecting them. 
    
    Given the array edges where edges[i] = [fromi , toi ,weighti]  
    represents a bidirectional and weighted edge 
    between cities fromi and toi, 
    and given the integer distanceThreshold. 
    
    You need to find out a city with the smallest number 
    of cities that are reachable through some path 
    and whose distance is at most Threshold Distance. 
    
    If there are multiple such cities, 
    our answer will be the city with the greatest label.
    
    Note: The distance of a path connecting 
    cities i and j is equal to the sum of 
    the edge's weights along that path.

  Q2: Number of 1 bits:

    Given a positive integer N, 
    print count of set bits in it. 

  Q3: Find length of loop:

    Given a linked list of size N. 
    
    The task is to complete the function countNodesinLoop() 
    that checks whether a given Linked List contains 
    a loop or not and if the loop is present then return 
    the count of nodes in a loop or else return 0. 
    
    C is the position of the node to which the 
    last node is connected. 
    
    If it is 0 then no loop.

Day 117:

  Q1: Euler Circuit in an Undirected Graph:

    Eulerian Path is a path in a graph 
    that visits every edge exactly once. 
    Eulerian Circuit is an Eulerian Path that 
    starts and ends on the same vertex. 
    
    Given the number of vertices v and adjacency list 
    adj denoting the graph. 
    
    Find that there exists the Euler circuit or not. 
    
    Return 1 if there exist  alteast one eulerian path else 0.

  Q2: Insertion Sort:

    The task is to complete the insert() function 
    which is used to implement Insertion Sort.

  Q3: Search in a matrix:

    Given a matrix mat[][] of size N x M, 
    where every row and column is sorted in increasing order, 
    and a number X is given. 
    
    The task is to find whether element X 
    is present in the matrix or not.

Day 118:

  Q1: Minimum element in BST:

    Given the root of a Binary Search Tree. 
    The task is to find the minimum valued 
    element in this given BST.

  Q2: Josephus problem:

    A total of n people are standing in a circle, 
    and you are one of them playing a game. 
    
    Starting from a person, k persons will be 
    counted in order along the circle, 
    and the k^th person will be killed. 
    
    Then the next k persons will be counted along the circle, 
    and again the k^th person will be killed. 
    
    This cycle will continue until only a 
    single person is left in the circle.
    
    If there are 5 people in the circle 
    in the order A, B, C, D, and E, 
    you will choose k=3. Starting from A, 
    you will count A, B and C. C will be 
    the 3rd person and will be killed. 
    
    Then you will continue counting 
    from D, E and then A. 
    
    A will be third person and will be killed. 
    
    You will be given an array where the first element 
    is the first person from whom the counting 
    will start and the subsequent order of the people. 
    
    You want to be the last one standing. 
    
    Determine the index at which 
    you should stand to survive the game.

  Q3: Root to leaf path sum:

    Given a binary tree and an integer s, 
    check whether there is a root-to-leaf 
    path with its sum as s.

Day 119:

  Q1: Closest Neighbour in BST:

    Given the root of a binary search tree and a number n, 
    find the greatest number in the binary search tree 
    that is less than or equal to n.

  Q2: Insert in a sorted list:

    Given a linked list sorted in ascending order 
    and an integer called data, insert data in the 
    linked list such that the list remains sorted.

  Q3: Queue Reversal:

    Given a Queue Q containing N elements. 
    The task is to reverse the Queue. 
    
    Your task is to complete the function rev(), 
    that reverses the N elements of the queue.

Day 120:

  Q1: Pairs violating the BST property:

    Given a binary tree with n nodes, 
    find the number of pairs violating the BST property.
    
    BST has the following properties:-
    
    Every node is greater than its left child 
    and less than its right child.
    
    Every node is greater than the maximum value of 
    in its left subtree and less than the minimum value in its right subtree.
    
    The maximum in the left sub-tree must be 
    less than the minimum in the right subtree.

  Q2: Minimum Operations:

    Given a number N. 
    
    Find the minimum number of operations 
    required to reach N starting from 0. 
    
    You have 2 operations available:
    
    Double the number
    Add one to the number

  Q3: Non-Repeating Element:

    Find the first non-repeating element in a given array arr 
    of n integers and if there is not present any 
    non-repeating element then return 0
    
    Note: The array consists of only positive 
    and negative integers and not zero.

Day 121:

  Q1: Minimum Absolute difference in BST:

    Given a binary search tree having n (n>1) nodes, 
    the task is to find the minimum absolute 
    difference between any two nodes.

  Q2: Index of an Extra Element:

    Given two sorted arrays of distinct elements.
     
    There is only 1 difference between the arrays.
     
    First array has one element extra added in between. 
    
    Find the index of the extra element.

  Q3: Transpose of Matrix:

    Write a program to find the transpose 
    of a square matrix of size N*N. 
    
    Transpose of a matrix is obtained by 
    changing rows to columns and columns to rows.

Day 121:

  Q1: Minimum Absolute difference in BST:

    Given a binary search tree having n (n>1) nodes, 
    the task is to find the minimum absolute 
    difference between any two nodes.

  Q2: Index of an Extra Element:

    Given two sorted arrays of distinct elements.
     
    There is only 1 difference between the arrays.
     
    First array has one element extra added in between. 
    
    Find the index of the extra element.

  Q3: Transpose of Matrix:

    Write a program to find the transpose 
    of a square matrix of size N*N. 
    
    Transpose of a matrix is obtained by 
    changing rows to columns and columns to rows.

Day 122:

  Q1: Kth common ancestor in BST:

    Given a BST with n (n>=2) nodes, 
    find the kth common ancestor of nodes 
    x and y in the given tree. 
    
    Return -1 if kth ancestor does not exist.
    
    Nodes x and y will always be present 
    in the input of a BST, and x != y.

  Q2: Selection Sort:

    Given an unsorted array of size N, 
    use selection sort to sort arr[] in increasing order.

  Q3: Delete Middle of Linked List:

    Given a singly linked list, 
    delete middle of the linked list. 
    
    For example, if given linked list is 1->2->3->4->5 
    then linked list should be modified to 1->2->4->5.
    
    If there are even nodes, 
    then there would be two middle nodes, 
    we need to delete the second middle element. 
    
    For example, if given linked list is 
    1->2->3->4->5->6 then it should be 
    modified to 1->2->3->5->6.
    
    If the input linked list has single node, 
    then it should return NULL.

Day 123:

  Q1: K distance from root:

    Given a binary tree having n nodes and an integer k. 
    
    Print all nodes that are at distance k from the root 
    (root is considered at distance 0 from itself). 
    
    Nodes should be printed from left to right.

  Q2: Segregate 0s and 1s:

    Given an array of length n consisting 
    of only 0's and 1's in random order. 
    
    Modify the array in-place to segregate 0s 
    on the left side and 1s on the right side of the array.

  Q3: Sum of all substrings of a number:

    Given an integer s represented as a string, 
    the task is to get the sum of all possible 
    sub-strings of this string.
    
    As the answer will be large, 
    return answer modulo 10^9+7. 
    
    Note: The number may have leading zeros.

Day 124:

  Q1: Strictly Increasing Array:

    Given an array nums of n positive integers. 
    Find the minimum number of operations required 
    to modify the array such that array elements 
    are in strictly increasing order (nums[i] < nums[i+1]).
    
    Changing a number to greater or lesser than 
    original number is counted as one operation.
    
    Note: Array elements can become negative 
    after applying operation.

  Q2: Convert array into Zig-Zag fashion:

    Given an array arr of distinct elements of size N, 
    the task is to rearrange the elements of the array 
    in a zig-zag fashion so that the converted array 
    should be in the below form: 
    
    arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] 
    < . . . . arr[n-2] < arr[n-1] > arr[n]. 
    
    NOTE: If your transformation is correct, 
    the output will be 1 else the output will be 0. 

  Q3: Print adjacency list:

    Given an undirected graph with V nodes and E edges, 
    create and return an adjacency list of the graph. 
    
    0-based indexing is followed everywhere.

Day 125:

  Q1: Count ways to Nth Stair:

    There are n stairs, and a person standing 
    at the bottom wants to reach the top. 
    
    The person can climb either 1 stair or 
    2 stairs at a time. 
    
    Count the number of ways, 
    the person can reach the top 
    (order does not matter).

  Q2: Reverse a Doubly Linked List:

    Given a doubly linked list of n elements. 
    Your task is to reverse the doubly linked list in-place.

  Q3: Special Stack:

    Design a data-structure SpecialStack that supports 
    all the stack operations like push(), pop(), isEmpty(), 
    isFull() and an additional operation getMin() 
    which should return minimum element from the SpecialStack. 
    
    Your task is to complete all the functions, 
    using stack data-Structure.

Day 126:

  Q1: Kth largest element in BST:

    Given a Binary Search Tree. 
    Your task is to complete the function which 
    will return the Kth largest element without 
    doing any modification in Binary Search Tree.

  Q2: Stack using two queues:

    Implement a Stack using two queues q1 and q2.

  Q3: Maximize dot product:

    Given two arrays a and b of positive integers of 
    size n and m where n >= m, the task is to maximize the 
    dot product by inserting zeros in the second array 
    but you cannot disturb the order of elements.
    
    Dot product of array a and b of size n is 
    a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1].

Day 127:

  Q1: Optimal Strategy for A Game:

    You are given an array arr of size n. 
    The elements of the array represent n coin 
    of values v1, v2, ....vn. 
    
    You play against an opponent in an alternating way. 
    
    In each turn, a player selects either the 
    first or last coin from the row, 
    removes it from the row permanently, 
    and receives the value of the coin.
    
    You need to determine the maximum possible 
    amount of money you can win if you go first.
    
    Note: Both the players are playing optimally.

  Q2: Binary Tree to BST:

    Given a Binary Tree, 
    convert it to Binary Search Tree in such a way 
    that keeps the original structure of Binary Tree intact.

  Q3: Rotate by 90 degree:

    Given a square matrix of size N x N. 
    The task is to rotate it by 90 degrees 
    in anti-clockwise direction without using any extra space. 

Day 128:

  Q1: Minimum Points to Reach Destination:

    Given a m*n grid with each cell consisting of positive, 
    negative, or zero point. We can move across a cell only 
    if we have positive points. 
    
    Whenever we pass through a cell, 
    points in that cell are added to our overall points, 
    the task is to find minimum initial points to reach cell 
    (m-1, n-1) from (0, 0) by following these certain set of rules :
    
    1. From a cell (i, j) we can move to (i + 1, j) or (i, j + 1).
    
    2. We cannot move from (i, j) if your overall points at (i, j) are <= 0.
    
    3. We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.

  Q2: Median of BST:
  
    Given a Binary Search Tree of size N, 
    find the Median of its Node values.

  Q3: Print Pattern:

    Print a sequence of numbers starting with N, 
    without using loop, 
    where replace N with N - 5, 
    until N > 0. 
    
    After that replace N with N + 5 
    until N regains its initial value.

Day 129:

  Q1: Party of Couples:

    You are given an integer array arr[] of size n, 
    representing n number of people in a party, 
    each person is denoted by an integer.
    
    Couples are represented by the same number ie: 
    two people have the same integer value, 
    it means they are a couple. 
    
    Find out the only single person in the party of couples.
    
    NOTE: It is guarantee that there exist 
    only one single person in the party.

  Q2: Queue of Two Stocks:

    Implement a Queue using 2 stacks s1 and s2 .
    A Query Q is of 2 Types
    (i) 1 x (a query of this type means  pushing 'x' into the queue)
    (ii) 2   (a query of this type means to pop 
    element from queue and print the poped element)
    
    Note :- If there is no element return -1 as answer while popping.

  Q3: Inorder Successor in BST:

    Given a BST, and a reference to a Node x in the BST. 
    Find the Inorder Successor of the given node in the BST.

Day 130:

  Q1: Gray to Binary Equivalent:

    Given an integer number n, 
    which is a decimal representation of Gray Code. 
    
    Find the binary equivalent of the Gray Code & 
    return the decimal representation of the binary equivalent.
     
    Note: Please visit here to learn How Gray Code is generated.

  Q2: Count the Zeroes:

    Given an array Arr of size N consisting of only 0's and 1's. 
    The array is sorted in such a manner that all the 1's 
    are placed first and then they are followed by all the 0's. 
    
    Find the count of all the 0's.

  Q3: Predict the Columnm:

    Given a matrix(2D array) M of size N*N consisting 
    of 0s and 1s only. The task is to find the column 
    with maximum number of 0s. 
    
    If more than one column exists, 
    print the one which comes first. 
    
    If the maximum number of 0s is 0 then return -1.

Day 131:

  Q1: Sum of Products:

    Given an array arr[] of size n. 
    Calculate the sum of Bitwise ANDs 
    ie: calculate sum of arr[i] & arr[j] 
    for all the pairs in the given array arr[] where i < j.

  Q2: Maximum width of Tree:

    Given a Binary Tree, 
    find the maximum width of it. 
    
    Maximum width is defined as the 
    maximum number of nodes at any level.
    
    For example, the maximum width of the following tree 
    is 4 as there are 4 nodes at the 3rd level.
    
              1
           /     \
         2        3
       /    \    /    \
      4    5   6    7
        \
          8

  Q3: Sjop in Candy Store:

    In a candy store, there are N different types 
    of candies available and the prices of all the 
    N different types of candies are provided to you.
    
    You are now provided with an attractive offer.
    
    For every candy you buy from the store and 
    get K other candies ( all are different types ) for free.
    
    Now you have to answer two questions. 
    Firstly, you have to find what is the 
    minimum amount of money you have to spend 
    to buy all the N different candies. 
    
    Secondly, you have to find what is the 
    maximum amount of money you have to spend 
    to buy all the N different candies.
    
    In both the cases you must utilize the offer i.e. 
    you buy one candy and get K other candies for free.

Day 132:

  Q1: Reverse Bits:

    Given a number x, reverse its binary form 
    and return the answer in decimal.

  Q2: Reverse Level order Traversal:

    Given a binary tree of size N, 
    find its reverse level order traversal. 
    
    ie- the traversal must begin from the last level.

  Q3: Boundary traversal of matrix:

    You are given a matrix of dimensions n x m. 
    
    The task is to perform boundary traversal 
    on the matrix in a clockwise manner starting 
    from the first row of the matrix.

Day 133:

  Q1: Xoring and Clearing:

    You are given an array arr[] of size n. 
    
    You need to do the following:
    
    You need to calculate the bitwise XOR 
    of each element in the array with its 
    corresponding index (indices start from 0).
    
    After step1, print the array.
    
    Now, set all the elements of arr[] to zero.
    
    Now, print arr[].

  Q2: Find the Frequency:

    Given an Array Arr of N positive integers 
    and an integer X. 
    
    Return the frequency of X in the array.

  Q3: Transform to Sum Tree:

    Given a Binary Tree of size N , 
    where each node can have positive or negative values. 
    
    Convert this to a tree where each node contains 
    the sum of the left and right sub trees 
    of the original tree. 
    
    The values of leaf nodes are changed to 0.

Day 134:

  Q1: Count the elements:

    Given two arrays a and b both of size n. 
    
    Given q queries in an array query each having 
    a positive integer x denoting an index of the array a. 
    
    For each query, your task is to find 
    all the elements less than or equal 
    to a[x] in the array b.

  Q2: Maximize Toys:

    Given an array arr[ ] of length N consisting 
    cost of N toys and an integer K 
    depicting the amount with you. 
    
    Your task is to find maximum number 
    of toys you can buy with K amount. 

  Q3: Minimum Number of Coins:

    Given an infinite supply of each denomination 
    of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } 
    and a target value N.
    
    Find the minimum number of coins and/or 
    notes needed to make the change for Rs N. 
    
    You must return the list containing 
    the value of coins required. 

Day 135:

  Q1: Minimize the Difference:

    You are given an array arr of size n. 
    You have to remove a subarray of size k , 
    such that the difference between the maximum 
    and minimum values of the remaining array is minimized.
    
    Find the minimum value obtained after performing 
    the operation of the removal of the subarray and return it.

  Q2: Plus One:

    Given a non-negative number represented 
    as a list of digits, add 1 to the number 
    (increment the number represented by the digits). 
    
    The digits are stored such that the most 
    significant digit is first element of array.

  Q3: For Loop - primeChec:

    What do you do when you need to execute 
    certain statements more than once? 
    
    You put them in a loop. 
    
    Loops are very powerful. 
    
    Majority of coding questions 
    need loops to work. 
    
    You can't even input testcases without loops!
    
    Here, we will use for loop and check 
    if the given number n is prime or not.
    
    Note: A number is prime if it's divisible ONLY 
    by itself and 1 and not any other number. 
    
    Also, 1 is not prime.

Day 136:

  Q1: Count Pairs in an Array:

    Given an array arr of n integers, 
    count all pairs (arr[i], arr[j]) in it 
    such that i*arr[i] > j*arr[j] and 0 ≤ i < j < n.
    
    Note: 0-based Indexing is followed.

  Q2: K largest elements:

    Given an array of N positive integers, 
    print k largest elements from the array.  

  Q3: Brothers from Different Roots:

    Given two BSTs containing N1 and N2 
    distinct nodes respectively and given a value x, 
    your task is to complete the function countPairs(), 
    that returns the count of all pairs of (a, b), 
    where a belongs to one BST and b 
    belongs to another BST, 
    such that a + b = x.

Day 137:

  Q1: Two repeated elements:

    You are given an integer n and 
    an integer array arr of size n+2. 
    
    All elements of the array are in 
    the range from 1 to n. 
    
    Also, all elements occur once 
    except two numbers which occur twice. 
    
    Find the two repeating numbers.
    
    Note: Return the numbers in their 
    order of appearing twice. 
    
    So, if X and Y are the repeating numbers, 
    and X's second appearance comes before 
    second appearance of Y, 
    then the order should be (X, Y).

  Q2: Get min at pop:
  
    Now, we'll try to solve a famous stack problem.
    
    You are given an array A of size N. 
    
    You need to first push the elements 
    of the array into a stack and then 
    print minimum in the stack at each 
    pop until stack becomes empty.
  
  Q3: Sieve of Eratosthenes:

    Given a number N, calculate the prime numbers 
    up to N using Sieve of Eratosthenes.  

Day 138:

  Q1: Find missing in second array:

    Given two integer arrays a of size 
    n and b of size m, the task is to 
    find the numbers which are present 
    in the first array a, but not 
    present in the second array b.

  Q2: Remove every Kth node:

    Given a singly linked list having n nodes, 
    your task is to remove every kth node 
    from the linked list. 
    
  Q3: Four Elements:

    Given an array A of N integers. 
    You have to find whether a combination 
    of four elements in the array whose sum 
    is equal to a given value X exists or not.

Day 139:

  Q1: Union of Two Sorted Arrays:

    Given two sorted arrays of size n and m respectively, 
    find their union. The Union of two arrays can be 
    defined as the common and distinct elements in the two arrays. 
    
    Return the elements in sorted order.

  Q2: Facing the Sun:

    Given an array H representing heights of buildings. 
    You have to count the buildings which will see the 
    sunrise (Assume : Sun rise on the side of array starting point).
    
    Note : Height of building should be strictly greater 
    than height of buildings in left in order to see the sun.

  Q3: Adding Sun:

    You start with an array A of size N. 
    Initially all elements of the array A are zero. 
    You will be given K positive integers. 
    Let j be one of these integers, 
    you have to add 1 to all A[i], 
    where i ≥ j. 
    
    Your task is to print the array A 
    after all these K updates are done.
    
    Note: Indices in updates array are given in 1-based indexing. 
    That is updates[i] are in range [1,N].

Day 140:

  Q1: Three way partitioning:

    Given an array of size n and a range [a, b]. 
    
    The task is to partition the array around the range 
    such that the array is divided into three parts.
    
    1) All elements smaller than a come first.
    2) All elements in range a to b come next.
    3) All elements greater than b appear in the end.
    The individual elements of three sets 
    can appear in any order. 
    
    You are required to return the modified array.
    
    Note: The generated output is 1 if 
    you modify the given array successfully.
    
    Geeky Challenge: Solve this problem in O(n) time complexity.

  Q2: Roof Top:

    You are given heights of consecutive buildings. 
    You can move from the roof of a building to the 
    roof of next adjacent building. 
    
    You need to find the maximum number of 
    consecutive steps you can put forward 
    such that you gain an increase in altitude 
    with each step.

  Q3: Inorder Traversal and BST:

    Given an array arr of size N, 
    determine whether this array represents 
    an inorder traversal of a BST. 
    
    Note: All keys in BST must be unique.

Day 141:

  Q1: Row with minimum number of 1's:

    Given a 2D binary matrix(1-based indexed) 
    a of dimensions nxm , 
    determine the row that contains 
    the minimum number of 1's.
    
    Note: The matrix contains only 1's and 0's. 
    
    Also, if two or more rows contain 
    the minimum number of 1's, 
    the answer is the lowest of those indices.

  Q2: Seating Arrangements:

    You are given an integer n, 
    denoting the number of people 
    who needs to be seated, 
    and a list of m integers seats, 
    where 0 represents a vacant seat 
    and 1 represents an already occupied seat.
    
    Find whether all n people can find a seat, 
    provided that no two people can sit next to each other.

  Q3: Common Elements:

    Given two lists V1 and V2 of sizes n and m respectively. 
    Return the list of elements common to both the lists 
    and return the list in sorted order. 
    
    Duplicates may be there in the output list.

Day 142:

  Q1: Rohan's Love for Matrix:

    Rohan has a special love for the matrices 
    especially for the first element of the matrix. 
    
    Being good at Mathematics, 
    he also loves to solve the different 
    problem on the matrices. 
    
    So one day he started to multiply 
    the matrix with the original matrix.  
    
    The elements of the original matrix a 
    are given by [a00=1 , a01=1, a10=1, a11=0].
    
    Given the power of the matrix, 
    n calculate the an and return the 
    a10 element mod 1000000007.

  Q2: Primes Sum:

    Given a number N. 
    Find if it can be expressed as 
    sum of two prime numbers.


  Q3: Frequency Game:

    Given an array A of size N. 
    
    The elements of the array consist of positive integers. 
    
    You have to find the largest element with minimum frequency.

Day 143:

  Q1: Copy Set Bits in Range

    Given two numbers X and Y, and a range [L, R] where 
    1 <= L <= R <= 32. You have to copy the set bits of 
    'Y' in the range L to R in 'X'. Return this modified X.
    
    Note: Range count will be from Right to Left & start from 1.

  Q2: Paths to reach origin:

    You are standing on a point (x, y) and 
    you want to go to the origin (0, 0) by 
    taking steps either left or down i.e. 
    from each point you are allowed to move either in 
    (x-1, y) or (x, y-1). 
    
    Find the number of paths from point to origin.

  Q3: Three Great Candidates:

    The hiring team aims to find 3 candidates 
    who are great collectively. Each candidate 
    has his or her ability expressed as an integer. 
    
    3 candidates are great collectively if product 
    of their abilities is maximum. 
    
    Given abilities of N candidates in an array arr[], 
    find the maximum collective ability from the 
    given pool of candidates.

Day 144:

  Q1: Matrix sum of hour glass:

    Given two integers n, m and a 2D matrix 
    mat of dimensions nxm, the task is to find 
    the maximum sum of an hourglass.
    
    An hourglass is defined as a part 
    of the matrix with the following form:
    
    Return -1 if any hourglass is not found.

  Q2: Adding Array Elements:

    Given an array Arr[] of size N and an integer K, 
    you have to choose the first two minimum elements 
    of the array and erase them, then insert the sum 
    of these two elements in the array until all the 
    elements are greater than or equal to K and 
    find the number of such operations required.

  Q3: Missing element of AP:

    Find the missing element from an ordered array arr[], 
    consisting of N elements representing an Arithmetic Progression(AP).
    
    Note: There always exists an element which 
    upon inserting into sequence forms Arithmetic progression. 
    
    Boundary elements (first and last elements) are not missing.

Day 145:

  Q1: Exit Point in a Matrix:

    Given a matrix of size n x m with 0’s and 1’s, 
    you enter the matrix at cell (0,0) in left to right direction. 
    Whenever you encounter a 0 you retain it in the same direction, 
    else if you encounter a 1 you have to change the direction to the 
    right of the current direction and change that 1 value to 0, 
    you have to find out from which index you will leave the matrix at the end.

  Q2: Product Pair:

    Given an array arr[] of size N of distinct elements 
    and a number X, find if there is a pair in arr[] 
    with product equal to X.

  Q3: Find the closest number:

    Given an array arr of positive sorted integers. 
    
    The task is to find the closest value to the 
    given number k in array. 
    
    Array may contain duplicate values.
    
    Note: If the difference is same for two values 
    print the value which is greater than the given number.

Day 146:

  Q1: Merge Sort on Doubly Linked List:

    Given Pointer/Reference to the head 
    of a doubly linked list of n nodes, 
    the task is to Sort the given 
    doubly linked list using Merge Sort 
    in both non-decreasing and non-increasing order.

  Q2: Print Diagonally:

    Give a N * N square matrix A, 
    return all the elements of its 
    anti-diagonals from top to bottom.

  Q3: Two Mirror Trees:
  
    Given a Two Binary Trees, write a function 
    that returns true if one is mirror of other, 
    else returns false.

Day 147:

  Q1: Delete Middle of Linked List:

    Given a singly linked list, 
    delete middle of the linked list. 
    
    For example, if given linked list is 1->2->3->4->5 
    then linked list should be modified to 1->2->4->5.
    
    If there are even nodes, 
    then there would be two middle nodes, 
    we need to delete the second middle element. 
    
    For example, if given linked list is 1->2->3->4->5->6 
    then it should be modified to 1->2->3->5->6.
    If the input linked list has single node, 
    then it should return NULL.

  Q2: Sort by Absolute Difference:

    Given an array of N elements and a number K. 
    The task is to arrange array elements according 
    to the absolute difference with K, i. e., 
    element having minimum difference comes first and so on.
    
    Note : If two or more elements are at equal distance 
    arrange them in same sequence as in the given array.

  Q3: Taking Input:

    Before implementing any algorithm, 
    we should be thorough with taking inputs.
     
    Here, we will learn how to read inputs.
    You are given two inputs: a(integer), and b(string). 
    You need to take the input and print a and b separated by a space.
    
    Note: You have to print a new line 
    at the end after prinintg a and b.

Day 148:

  Q1: Remove every kth node:

    Given a singly linked list having n nodes, 
    your task is to remove every kth node from the linked list. 

  Q2: Make the array beautiful:

    Given an array of negative and non-negative integers. 
    You have to make the array beautiful. 
    An array is beautiful if two adjacent integers, 
    arr[i] and arr[i+1] are either negative or non-negative. 
    
    And you can do the following operation any 
    number of times until the array becomes beautiful.
    
    If two adjacent integers are different i.e. 
    one of them is negative and other is non-negative, 
    remove them.
    
    Return the beautiful array after 
    performing the above operation.
    
    Note:An empty array is also a beautiful array. 
    There can be many adjacent integers which are 
    different as stated above. 
    
    So remove different adjacent integers 
    as described above from left to right.

  Q3: Unique rows in boolean matrix:

    Given a binary matrix your task is to find all 
    unique rows of the given matrix in the order 
    of their appearance in the matrix.

Day 149:

  Q1: Add two numbers represented by linked list:

    Given two decimal numbers, num1 and num2, 
    represented by linked lists of size n and m respectively. 
    
    The task is to return a linked list that 
    represents the sum of these two numbers.
    
    For example, the number 190 will be 
    represented by the linked list, 1->9->0->null, 
    similarly 25 by 2->5->null. Sum of these two numbers 
    is 190 + 25 = 215, which will be represented 
    by 2->1->5->null. 
    
    You are required to return the 
    head of the linked list 2->1->5->null.
    
    Note: There can be leading zeros in the input lists, 
    but there should not be any leading zeros in the output list.

  Q2: Is it Fibonacc:

    Geek just learned about Fibonacci numbers.
    
    The Fibonacci Sequence is the 
    series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    
    where the next number is found by 
    adding up the two numbers before it.
    
    He defines a new series called Geeky numbers. 
    Here the next number is the sum of the K preceding numbers.
    
    You are given an array of size K, GeekNum[ ], 
    where the ith element of the array 
    represents the ith Geeky number. 
    
    Return its Nth term.
    
    Note: This problem can be solved in O(N2) 
    time complexity but the user has to solve this in O(N). 
    
    The Constraints are less because there 
    can be integer overflow in the terms.

  Q3: Sequence Fun:

    You have a sequence 2,5,16,65,........
    
    Given an integer n as input. 
    
    You have to find the value at the 
    nth position in the sequence.

Day 150:

  Q1: Arrange Consonants and Vowels:

    Given a singly linked list having n nodes 
    containing english alphabets ('a'-'z'). 
    
    Rearrange the linked list in such a way that 
    all the vowels come before the consonants 
    while maintaining the order of their arrival. 

  Q2: Ticket Counter:

    N people from 1 to N are standing 
    in the queue at a movie ticket counter. 
    
    It is a weird counter, as it distributes tickets 
    to the first K people and then the last K people 
    and again first K people and so on, once a person 
    gets a ticket moves out of the queue. 
    
    The task is to find the last person to get the ticket.

  Q3: Odd even level difference:

    Given a Binary Tree. 
    
    Find the difference between the 
    sum of node values at even levels 
    and the sum of node values at the odd levels.

Day 151:

  Q1: Serialize and deserialize a binary tree:

    Serialization is to store a tree in an array 
    so that it can be later restored and 
    deserialization is reading tree back 
    from the array. 
    
    Complete the functions
    
    serialize() : stores the tree into an array a and returns the array.
    
    deSerialize() : deserializes the array to the tree 
    and returns the root of the tree.
    
    Note: Multiple nodes can have the same data 
    and the node values are always positive integers. 
    
    Your code will be correct if the tree returned 
    by deSerialize(serialize(input_tree)) 
    is same as the input tree. 
    
    Driver code will print the in-order 
    traversal of the tree returned by 
    deSerialize(serialize(input_tree)).

  Q2: Maximum Sum LCM:

    Given a positive number n. 
    
    You need to write a program to find the 
    maximum sum of distinct numbers such that 
    the LCM of all these numbers is equal to n 
    and those numbers are less than or equal to n.

  Q3: Geek Jump:

    Geek wants to climb from the 0th stair 
    to the (n-1)th stair. At a time the Geek 
    can climb either one or two steps. 
    
    A height[N] array is also given. 
    Whenever the geek jumps from stair i to stair j, 
    the energy consumed in the jump is 
    abs(height[i]- height[j]), where abs() 
    means the absolute difference. 
    
    return the minimum energy that 
    can be used by the Geek to jump 
    from stair 0 to stair N-1.

Day 152:

  Q1: K distance from root:

    Given a binary tree having n nodes and an integer k. 
    Print all nodes that are at distance k from the root 
    (root is considered at distance 0 from itself). 
    
    Nodes should be printed from left to right.

  Q2: Sum of Leaf Nodes:

    Given a Binary Tree of size N. 
    
    The task is to complete the function sumLeaf(), 
    that should return the sum of 
    all the leaf nodes of the given binary tree.

  Q3: Dominant Pairs:

    You are given an array of integers 
    of size n where n being even.. 
    
    You have to calculate the number 
    of dominate pairs (i,j) .
    
    Where a pair is called dominant if 
    ( 0<=i<n/2, n/2<=j<n, arr[i]>=5*arr[j] ) 
    these relation are fulfilled.  
    
    For example  in arr=[10,3,3,1] 
    index i=0, j=3 form a dominating pair
    
    Note : 0 based indexing is used  and n is even 

Day 153:

  Q1: Construct Binary Tree from Inorder and Postorder

    Given inorder and postorder traversals 
    of a binary tree(having n nodes) in the 
    arrays in[] and post[] respectively. 
    
    The task is to construct a binary tree 
    SSSfrom these traversals.
    
    Driver code will print the 
    preorder traversal of the constructed tree.

  Q2: Kth smallest element:

    Given an array arr[] and an integer k 
    where k is smaller than the size of the array, 
    the task is to find the kth smallest element 
    in the given array. 
    
    It is given that all array elements are distinct.
    
    Note:-  l and r denotes the starting and 
    ending index of the array.

  Q3: Minimize the Heights II:

    Given an array arr[] denoting heights of N towers and a positive integer K.
    
    For each tower, you must perform exactly 
    one of the following operations exactly once.
    
    Increase the height of the tower by K
    
    Decrease the height of the tower by K
    
    Find out the minimum possible difference 
    between the height of the shortest and 
    tallest towers after you have modified each tower.
    
    You can find a slight modification of the problem here.
    
    Note: It is compulsory to increase or decrease 
    the height by K for each tower. After the operation, 
    the resultant array should not contain any negative integers.

Day 154:

  Q1: Vertical Sum:

    Given a binary tree having n nodes, 
    find the vertical sum of the nodes that 
    are in the same vertical line. 
    
    Return all sums through different 
    vertical lines starting from the 
    left-most vertical line to the 
    right-most vertical line.

  Q2: Count Inversions:

    Given an array of integers. 
    
    Find the Inversion Count in the array. 
    
    Inversion Count: For an array, 
    inversion count indicates how far (or close) 
    the array is from being sorted. 
    
    If the array is already sorted 
    then the inversion count is 0.
    
    If an array is sorted in the reverse order 
    then the inversion count is the maximum. 
    
    Formally, two elements a[i] and a[j] 
    form an inversion if a[i] > a[j] and i < j.

  Q3: Remove loop in Linked List:

    Given a linked list of N nodes 
    such that it may contain a loop.
    
    A loop here means that the last node 
    of the linked list is connected to the 
    node at position X(1-based index). 
    
    If the linked list does not have any loop, X=0.
    
    Remove the loop from the linked list, 
    if it is present, i.e. unlink the 
    last node which is forming the loop.

Day 155:

  Q1: Print all nodes that don't have sibling:

    Given a Binary Tree of n nodes, 
    find all the nodes that don't have any siblings. 
    
    You need to return a list of integers containing 
    all the nodes that don't have a 
    sibling in sorted order (Increasing).
    
    Two nodes are said to be siblings 
    if they are present at the same level, 
    and their parents are the same.
    
    Note: The root node can not have a sibling 
    so it cannot be included in our answer.

  Q2: Bottom View of Binary Tree:

    Given a binary tree, 
    print the bottom view from left to right.
    
    A node is included in bottom view 
    if it can be seen when we look at 
    the tree from bottom.
    
    
                          20
                        /    \
                      8       22
                    /   \        \
                  5      3       25
                        /   \      
                      10    14
    
    For the above tree, the bottom view is 5 10 3 14 25.
    
    If there are multiple bottom-most nodes 
    for a horizontal distance from root, 
    then print the later one in level traversal. 
    
    For example, in the below diagram, 3 and 4 
    are both the bottommost nodes at 
    horizontal distance 0, we need to print 4.
    
                          20
                        /    \
                      8       22
                    /   \     /   \
                  5      3 4     25
                         /    \      
                     10       14
    
    For the above tree the output should be 5 10 4 14 25.
    
    Note: The Input/Output format and 
    Example given are used for the system's 
    internal purpose, and should be used 
    by a user for Expected Output only. 
    
    As it is a function problem, 
    hence a user should not read 
    any input from the stdin/console. 
    
    The task is to complete the function specified, 
    and not to write the full code.

  Q3: Rotate a Linked List:

    Given a singly linked list of size N. 
    The task is to left-shift the linked list by k nodes, 
    where k is a given positive integer 
    smaller than or equal to length of the linked list.

Day 156:

  Q1: Reverse Order Traversal:

    Given a binary tree of size n, 
    find its reverse level order traversal. 
    ie- the traversal must begin from the last level.

  Q2: Longest Sub-Array with Sum K:

    Given an array containing N integers and an integer K., 
    Your task is to find the length of the longest Sub-Array 
    with the sum of the elements equal to the given value K.

  Q3: Validate an IP Address:

    Write a program to Validate an IPv4 Address.
    
    According to Wikipedia, IPv4 addresses 
    are canonically represented in dot-decimal notation, 
    which consists of four decimal numbers, 
    each ranging from 0 to 255, separated by dots, 
    e.g., 172.16.254.1 .
    
    A valid IPv4 Address is of the form x1.x2.x3.x4 
    where 0 <= (x1, x2, x3, x4) <= 255.
    
    Thus, we can write the generalized form 
    of an IPv4 address as (0-255).(0-255).(0-255).(0-255).
    
    Note: Here we are considering numbers only 
    from 0 to 255 and any additional leading 
    zeroes will be considered invalid.
    
    Your task is to complete the function isValid 
    which returns 1 if the given IPv4 address is 
    valid else returns 0. The function takes the 
    IPv4 address as the only argument in the form of string.

Day 157:

  Q1: Root to Leaf Paths:

    Given a Binary Tree of nodes, 
    you need to find all the possible paths 
    from the root node to all the leaf nodes 
    of the binary tree.

  Q2: Topological Sort:

    Given a Directed Acyclic Graph (DAG) 
    with V vertices and E edges, 
    Find any Topological Sorting of that Graph.

  Q3: Job Sequencing Problem:

    Given a set of N jobs where each jobi 
    has a deadline and profit associated with it.
    
    Each job takes 1 unit of time to complete 
    and only one job can be scheduled at a time. 
    
    We earn the profit associated with job 
    if and only if the job is completed by its deadline.
    
    Find the number of jobs done and the maximum profit.
    
    Note: Jobs will be given in the form (Jobid, Deadline, Profit) 
    associated with that Job. 
    
    Deadline of the job is the time before 
    which job needs to be completed to earn the profit.

Day 158:

  Q1: Divisor Game:

    Alice and Bob take turns playing a game, 
    with Alice starting first.
    
    Initially, there is a number n on the chalkboard. 
    
    On each player's turn, that player makes a move consisting of:
    
    Choosing any x with 0 < x < n  and n % x == 0.
    
    Replacing the number n on the chalkboard with n - x.
    
    Also, if a player cannot make a move, they lose the game.
    
    Return true if and only if Alice wins the game, 
    assuming both players play optimally.

  Q2: Stock Span Problem:

    The stock span problem is a financial problem 
    where we have a series of n daily price quotes 
    for a stock and we need to calculate the 
    span of stocks price for all n days. 
    
    The span Si of the stocks price on a given day i 
    is defined as the maximum number of consecutive days 
    just before the given day, for which the price of 
    the stock on the given day is less than or equal to 
    its price on the current day.
    
    For example, if an array of 7 days prices is given 
    as {100, 80, 60, 70, 60, 75, 85}, then the span values 
    for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

  Q3: Number of Occurence:

    Given a sorted array Arr of size N and a number X, 
    you need to find the number of occurrences of X in Arr.

Day 159:

  Q1: Combination Sum II:

    Given an array of integers arr, 
    the length of the array n, 
    and an integer k, 
    find all the unique combinations 
    in arr where the sum of the combination 
    is equal to k. 
    
    Each number can only be used once in a combination.
    
    Return the combinations in the lexicographically sorted order, 
    where each combination is in non-decreasing order.

  Q2: Number of Coins:

    Given a value V and array coins[] of size M, 
    the task is to make the change for V cents, 
    given that you have an infinite supply of 
    each of coins{coins1, coins2, ..., coinsm} valued coins. 
    
    Find the minimum number of coins to make the change. 
    
    If not possible to make change then return -1.

  Q3: Circular Tour:

    Suppose there is a circle. 
    
    There are N petrol pumps on that circle. 
    
    You will be given two sets of data.
    
    1. The amount of petrol that every petrol pump has.
    2. Distance from that petrol pump to the next petrol pump.
    
    Find a starting point where the truck can start 
    to get through the complete circle without 
    exhausting its petrol in between.
    
    Note :  Assume for 1 litre petrol, 
    the truck can go 1 unit of distance.

Day 160:

  Q1: Juggler Sequence:

    Juggler Sequence is a series of integers 
    in which the first term starts with a 
    positive integer number a and the remaining terms 
    are generated from the immediate previous term 
    using the below recurrence relation:
    
    Juggler Formula
    
    Given a number n, 
    find the Juggler Sequence for this number as 
    the first term of the sequence until it becomes 1.

  Q2: Non Repeating Numbers:

    Given an array A containing 2*N+2 positive numbers, 
    out of which 2*N numbers exist in pairs whereas 
    the other two number occur exactly once and are distinct. 
    
    Find the other two numbers. Return in increasing order.

  Q3: Flattening a Linked List:

    Given a Linked List of size N, 
    where every node represents a sub-linked-list 
    and contains two pointers:
    
    (i) a next pointer to the next node,
    
    (ii) a bottom pointer to a linked list where this node is head.
    
    Each of the sub-linked-list is in sorted order.
    Flatten the Link List such that all the nodes 
    appear in a single level while maintaining the sorted order. 
    
    Note: The flattened list will be printed using 
    the bottom pointer instead of the next pointer.
    
    For more clarity have a look at the 
    printList() function in the driver code.

Day 161:

  Q1: Minimum steps to destination:

    Given an infinite number line. 
    You start at 0 and can go either 
    to the left or to the right.
    
    The condition is that in the ith move, 
    you must take i steps. 
    
    Given a destination d, 
    find the minimum number of steps 
    required to reach that destination.

  Q2: Tower of Hanoi:

    The tower of Hanoi is a famous puzzle 
    where we have three rods and N disks. 
    
    The objective of the puzzle is to move 
    the entire stack to another rod. 
    
    You are given the number of discs N. 
    
    Initially, these discs are in the rod 1. 
    
    You need to print all the steps of discs movement 
    so that all the discs reach the 3rd rod. 
    
    Also, you need to find the total moves.
    
    Note: The discs are arranged such that the top disc 
    is numbered 1 and the bottom-most disc is numbered N. 
    
    Also, all the discs have different sizes and a bigger disc 
    cannot be put on the top of a smaller disc. 
    
    Refer the provided link to get a better clarity about the puzzle.

  Q3: Rotten Oranges:

    Given a grid of dimension nxm where each cell 
    in the grid can have values 0, 1 or 2 
    which has the following meaning:
    
    0 : Empty cell
    1 : Cells have fresh oranges
    2 : Cells have rotten oranges
    
    We have to determine what is the earliest time 
    after which all the oranges are rotten. 
    
    A rotten orange at index [i,j] can rot other 
    fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] 
    (up, down, left and right) in unit time. 

Day 162:

  Q1: Number of Good Components:

    Given an undirected graph with v vertices
    (numbered from 1 to v) and e edges. 
    
    Find the number of good components in the graph.
    
    A component of the graph is good if and 
    only if the component is fully connected.
    
    Note: A fully connected component is a subgraph 
    of a given graph such that there's an edge between 
    every pair of vertices in the component, 
    the given graph can be a disconnected graph. 

  Q2: k largest elements:

    Given an array Arr of N positive integers and an integer K, 
    find K largest elements from the array.  
    
    The output elements should be printed in decreasing order.

  Q3: Merge Sort:

    Given an array arr[], its starting position l 
    and its ending position r. 
    
    Sort the array using merge sort algorithm.

Day 163:

  Q1: Path With Minimum Effort:

    Given two binary trees with head reference 
    as T and S having at most N nodes. 
    
    The task is to check if S is present as subtree in T.
    
    A subtree of a tree T1 is a tree T2 consisting 
    of a node in T1 and all of its descendants in T1.

  Q2: Egg Dropping Puzzle:

    You are given N identical eggs and you have 
    access to a K-floored building from 1 to K.
    
    There exists a floor f where 0 <= f <= K such that 
    any egg dropped from a floor higher than f will break, 
    and any egg dropped from or below floor f will not break.
    
    There are few rules given below. 
    
    An egg that survives a fall can be used again.
    
    A broken egg must be discarded.
    
    The effect of a fall is the same for all eggs.
    
    If the egg doesn't break at a certain floor, 
    it will not break at any floor below.
    
    If the eggs breaks at a certain floor, 
    it will break at any floor above.
    
    Return the minimum number of moves that you need 
    to determine with certainty what the value of f is.
    
    For more description on this problem see wiki page

  Q3: Check if Subtree:

    You are a hiker preparing for an upcoming hike. 
    
    You are given heights[][], a 2D array of size rows x columns, 
    where heights[row][col] represents the height of cell (row, col). 
    
    You are situated in the top-left cell, (0, 0), 
    and you hope to travel to the bottom-right cell, 
    (rows-1, columns-1) (i.e., 0-indexed). 
    
    You can move up, down, left, or right, 
    and you wish to find the route with minimum effort.
    
    Note: A route's effort is the maximum absolute difference 
    in heights between two consecutive cells of the route.

Day 164:

  Q1: Account Merge:

    Given a list of accounts of size n where each element 
    accounts [ i ] is a list of strings, 
    where the first element account [ i ][ 0 ]  is a name, 
    and the rest of the elements are emails 
    representing emails of the account.
    
    Geek wants you to merge these accounts. 
    
    Two accounts belong to the same person if 
    there is some common email to both accounts. 
    
    Note that even if two accounts have the same name, 
    they may belong to different people as people could have the same name. 
    
    A person can have any number of accounts initially, 
    but all of their accounts have the same name.
    
    After merging the accounts, return the accounts 
    in the following format: 
    
    The first element of each account is the name, 
    and the rest of the elements are emails in sorted order.
    
    Note: Accounts themselves can be returned in any order.

  Q2: Total Decoding Messages:

    A top secret message containing letters from A-Z 
    is being encoded to numbers using the following mapping:
    
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    
    You are an FBI agent. 
    You have to determine the total number of ways 
    that message can be decoded, as the answer 
    can be large return the answer modulo 10^9 + 7.
    
    Note: An empty digit sequence is considered to have one decoding. 
    It may be assumed that the input contains valid digits from 0 to 9 
    and If there are leading 0s, extra trailing 0s and two 
    or more consecutive 0s then it is an invalid string.

  Q3: Next Permutation:

    Implement the next permutation, 
    which rearranges the list of numbers into Lexicographically 
    next greater permutation of list of numbers. 
    
    If such arrangement is not possible, 
    it must be rearranged to the lowest possible order i.e. 
    sorted in an ascending order. 
    
    You are given an list of numbers arr[ ] of size N.

Day 165:

  Q1: Divisibility Tree:

    Given a tree with n nodes where n is even. 
    
    The tree is numbered from 1 to n, has n - 1 edges 
    and is rooted at node 1. 
    
    Your task is to eliminate the maximum number 
    of edges resulting in a set of disjoint trees 
    where the number of nodes in each tree is divisible by 2.

  Q2: Max length chain:

    You are given N pairs of numbers. 
    
    In every pair, the first number is always 
    smaller than the second number. 
    
    A pair (c, d) can follow another pair (a, b) if b < c. 
    
    Chain of pairs can be formed in this fashion. 
    
    You have to find the longest chain which 
    can be formed from the given set of pairs. 

  Q3: Boolean Matrix:

    Given a boolean matrix of size RxC 
    where each cell contains either 0 or 1, 
    modify it such that if a matrix cell matrix[i][j] 
    is 1 then all the cells in its i^th row 
    and j^th column will become 1.

Day 166:

  Q1: Find Pair Given Difference:

    Given an array arr[] of size n and an integer x, 
    return 1 if there exists a pair of elements 
    in the array whose absolute difference is x, 
    otherwise, return -1.

  Q2: Multiply two Strings:

    Given two numbers as strings s1 and s2. 
    
    Calculate their Product.
    
    Note: The numbers can be negative and 
    You are not allowed to use any built-in 
    function or convert the strings to integers. 
    
    There can be zeros in the begining of the numbers. 
    
    You don't need to specify '+' sign in the begining of positive numbers.

  Q3: Maximize The Cut Segments:

    Given an integer N denoting the Length of a line segment. 
    
    You need to cut the line segment in such a way that 
    the cut length of a line segment each time is either x , y or z. 
    
    Here x, y, and z are integers.
    
    After performing all the cut operations, 
    your total number of cut segments must be maximum.
    
    Note: if no segment can be cut then return 0.

Day 167:

  Q1: Find the Highest Number:

    Given an integer array a[] of size n, 
    find the highest element of the array. 
    
    The array will either be strictly increasing 
    or strictly increasing and then strictly decreasing.
    
    Note: a[i] != a[i+1]   

  Q2: Nth Catalan Number:

    Given a number N. The task is to find the Nth catalan number.
    
    The first few Catalan numbers for N = 0, 1, 2, 3, … 
    are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
    
    Catalan Number for N is equal to the number 
    of expressions containing N pairs of paranthesis 
    that are correct matched, i.e., for each of the 
    N '(' there exist N ')' on there right and vice versa.
    
    Since answer can be huge return answer modulo 1e9+7.
    
    Note: Positions start from 0 as shown above.

  Q3: Activity Selection:

    Given N activities with their start 
    and finish day given in array start[ ] and end[ ]. 
    
    Select the maximum number of activities that
    can be performed by a single person, 
    assuming that a person can only work 
    on a single activity at a given day.
    
    Note : Duration of the activity includes both starting and ending day.

Day 168:

  Q1: Find the Closest Number:

    Given a sorted array arr[] of positive integers. 
    
    The task is to find the closest value in the 
    array to the given number k. 
    
    The array may contain duplicate values.
    
    Note: If the difference with k is the same for 
    two values in the array return the greater value.

  Q2: Count Total set bits:

    You are given a number N. 
    Find the total count of set bits 
    for all numbers from 1 to N(both inclusive).

  Q3: Merge two sorted linked lists:

    Given two sorted linked lists consisting 
    of N and M nodes respectively. 
    
    The task is to merge both of the list (in-place) 
    and return head of the merged list.

Day 169:

  Q1: Modular Exponentiation for large numbers:

    Implement pow(x, n) % M.

    In other words, for a given value of 
    x, n, and M, find  (xn) % M.

  Q2: Valid Substring:

    Given a string s consisting only of opening 
    and closing parenthesis 'ie '('  and ')', 
    find out the length of the longest 
    valid(well-formed) parentheses substring.
    
    NOTE: The length of the smallest valid substring ( ) is 2.

  Q3: Floyd Warshall:

    The problem is to find the shortest distances 
    between every pair of vertices in a given 
    edge-weighted directed graph. 
    
    The graph is represented as an 
    adjacency matrix of size n*n. 
    
    Matrix[i][j] denotes the weight 
    of the edge from i to j. 
    
    If Matrix[i][j]=-1, it means there 
    is no edge from i to j.
    
    Do it in-place.

Day 170:

  Q1: K closest elements:

    Given a sorted array of unique elements in increasing order, 
    arr[] of n integers, and a value x. 
    
    Find the K closest elements to x in arr[].
    
    Keep the following points in mind:
    
    If x is present in the array, then it need not be considered.
    
    If two elements have the same difference as x, 
    the greater element is prioritized.
    
    If sufficient elements are not present on the right side, 
    take elements from the left and vice versa.

  Q2: Largest BST:

    Given a binary tree. 
    
    Find the size of its largest subtree 
    that is a Binary Search Tree.
    
    Note: Here Size is equal to the 
    number of nodes in the subtree.

  Q3: Lucky Numbers:

    Lucky numbers are subset of integers. 
    
    Rather than going into much theory, 
    let us see the process of arriving at lucky numbers,
    
    Take the set of integers
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,……
    First, delete every second number, 
    we get following reduced set.
    
    1, 3, 5, 7, 9, 11, 13, 15, 17, 19,…………
    
    Now, delete every third number, we get
    1, 3, 7, 9, 13, 15, 19,….….
    
    Continue this process indefinitely……
    
    Any number that does NOT get deleted 
    due to above process is called “lucky”.
    
    You are given a number N, 
    you need to tell whether the number is lucky or not. 
    
    If the number is lucky return 1 otherwise 0.

Day 171:

  Q1: Minimize max distance to gas station:

    We have a horizontal number line. 
    
    On that number line, we have gas stations 
    at positions stations[0], stations[1], ..., stations[N-1], 
    where n = size of the stations array. 
    
    Now, we add k more gas stations so that d, 
    the maximum distance between 
    adjacent gas stations, is minimized. 
    
    We have to find the smallest possible value of d. 
    
    Find the answer exactly to 2 decimal places.

  Q2: Number of Paths:

    The problem is to count all the possible paths 
    from top left to bottom right of an MxN matrix 
    with the constraints that from each cell 
    you can either move to right or down.
    
    Return answer modulo 10^9+7.

  Q3: Rod Cutting:

    Given a rod of length N inches and 
    an array of prices, price[]. 
    
    price[i] denotes the value of a piece of length i. 
    
    Determine the maximum value obtainable by 
    cutting up the rod and selling the pieces.
    
    Note: Consider 1-based indexing.

Day 172:

  Q1: K-Palindrome:

    Given a string str of length n, 
    find if the string is K-Palindrome or not. 
    
    A k-palindrome string transforms into a 
    palindrome on removing at most k characters from it.

  Q2: Minimum Spanning Tree:

    Given a weighted, undirected, 
    and connected graph with V vertices and E edges, 
    your task is to find the sum of the weights 
    of the edges in the Minimum Spanning Tree (MST) of the graph. 
    
    The graph is represented by an adjacency list, 
    where each element adj[i] is a vector containing 
    pairs of integers. Each pair represents an edge, 
    with the first integer denoting the endpoint 
    of the edge and the second integer denoting 
    the weight of the edge.

  Q3: M-Coloring Problem:

    Given an undirected graph and an integer M. 
    
    The task is to determine if the graph can 
    be colored with at most M colors such that 
    no two adjacent vertices of the graph 
    are colored with the same color. 
    
    Here coloring of a graph means the assignment 
    of colors to all vertices. 
    
    Print 1 if it is possible to colour vertices and 0 otherwise.

Day 173:

  Q1: Partitions with Given Difference:

    Given an array arr, 
    partition it into two subsets(possibly empty) 
    such that each element must belong to only one subset. 
    
    Let the sum of the elements of these two subsets be S1 and S2. 
    
    Given a difference d, count the number 
    of partitions in which S1 is greater than 
    or equal to S2 and the difference between S1 
    and S2 is equal to d. 
    
    Since the answer may be large return it modulo 10^9 + 7.

  Q2: Largest prime factor:

    Given a number N, the task is to find 
    the largest prime factor of that number.

  Q3: Maximum path sum in matrix:

    Given a NxN matrix of positive integers. 
    
    There are only three possible moves from a cell Matrix[r][c].
    
    1. Matrix [r+1] [c]
    2. Matrix [r+1] [c-1]
    3. Matrix [r+1] [c+1]
    
    Starting from any column in row 0 return 
    the largest sum of any of the paths up to row N-1.
    
    NOTE: We can start from any column in zeroth row 
    and can end at any column in (N-1)th row.

Day 174:

  Q1: You and your books:

    You have n stacks of books. 
    
    Each stack of books has some nonzero height arr[i] 
    equal to the number of books on that stack 
    ( considering all the books are identical and each book has a height of 1 unit ). 
    
    In one move, you can select any number of
    consecutive stacks of books such that the height 
    of each selected stack of books arr[i] <= k. 
    
    Once such a sequence of stacks is chosen, 
    You can collect any number of books 
    from the chosen sequence of stacks.
    
    What is the maximum number of 
    books that you can collect this way?

  Q2: Check if Tree is Isomorphic:

    Given two Binary Trees. 
    
    Check whether they are Isomorphic or not.
    
    Note: 
    Two trees are called isomorphic if one can be 
    obtained from another by a series of flips, i.e. 
    by swapping left and right children of several nodes. 
    
    Any number of nodes at any level can 
    have their children swapped. 
    
    Two empty trees are isomorphic.
    
    For example, the following two trees are isomorphic 
    with the following sub-trees flipped: 2 and 3, 
    NULL and 6, 7 and 8.

  Q3: Combination Sum:

    Given an array of integers and a sum B, 
    find all unique combinations in the array 
    where the sum is equal to B. 
    
    The same number may be chosen from 
    the array any number of times to make B.
    
    Note:
            1. All numbers will be positive integers.
            2. Elements in a combination (a1, a2, …, ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
            3. The combinations themselves must be sorted in ascending order.

Day 175:

  Q1: Minimum Cost To Make TwoStrings Identical:

    Given two strings x and y, and two values costX and costY, 
    the task is to find the minimum cost required to 
    make the given two strings identical. 
    
    You can delete characters from both the strings. 
    
    The cost of deleting a character from string X is costX and from Y is costY. 
    
    The cost of removing all characters from a string is the same.

  Q2: Stock buy and sell II:

    The cost of stock on each day is given 
    in an array price[] of size n. 
    
    Each day you may decide to either buy 
    or sell the stock i at price[i], 
    you can even buy and sell the stock on the same day, 
    Find the maximum profit which you can get.
    
    Note: Buying and Selling of the stock 
    can be done multiple times, 
    but you can only hold one stock at a time. 
    
    In order to buy another stock, 
    firstly you have to sell the current holding stock.

  Q3: Flood fill Algorithm:

    An image is represented by a 2-D array of integers, 
    each integer representing the pixel value of the image.
    
    Given a coordinate (sr, sc) representing 
    the starting pixel (row and column) 
    of the flood fill, and a pixel value newColor, 
    "flood fill" the image.
    
    To perform a "flood fill", consider the starting pixel, 
    plus any pixels connected 4-directionally to the 
    starting pixel of the same color as the starting pixel, 
    plus any pixels connected 4-directionally to those pixels (
    also with the same color as the starting pixel), and so on.
     
    Replace the color of all of the 
    aforementioned pixels with the newColor.

Day 176:

  Q1: Longest Subsequence-1:

    Given an integer array a[] of size n, 
    find the length of the longest subsequence 
    such that the absolute difference between 
    adjacent elements is 1.

  Q2: Sort a Stack:

    Given a stack, the task is to sort it 
    such that the top of the stack has the greatest element.

  Q3: Predecessor and Successor:

    There is BST given with the root node 
    with the key part as an integer only. 
    
    You need to find the in-order successor 
    and predecessor of a given key. 
    
    If either predecessor or successor 
    is not found, then set it to NULL.
    
    Note:- In an inorder traversal the number just smaller 
    than the target is the predecessor and the number 
    just greater than the target is the successor. 

Day 177:

  Q1: Minimum cost to fill given weight in a bag:

    Given an array cost[] of positive integers 
    of size n and an integer w, where cost[i] 
    represents the cost of an i kg packet of oranges, 
    the task is to find the minimum cost to buy 
    exactly w kg of oranges. 
    
    The cost array has a 1-based indexing. 
    
    If buying exactly w kg of oranges is impossible, 
    then return -1.
    
    
    Note:
    1. cost[i] = -1 means that i kg packet of orange is unavailable.
    2. It may be assumed that there is an infinite 
    supply of all available packet types.

  Q2: K Sum Paths:
    
    Given a binary tree and an integer K.
    
    Find the number of paths in the tree 
    which have their sum equal to K.
    
    A path may start from any node and end 
    at any node in the downward direction.

  Q3: Connect Nodes at Same Level:

    Given a binary tree, 
    connect the nodes that are at same level. 
    
    You'll be given an addition nextRight pointer for the same.
    
    Initially, all the nextRight pointers point to garbage values. 
    Your function should set these 
    pointers to point next right for each node.
    
           10                       10 ------> NULL
          / \                       /      \
         3   5       =>     3 ------> 5 --------> NULL
        / \     \               /  \           \
       4   1   2          4 --> 1 -----> 2 -------> NULL

Day 178:

  Q1: Geek and its Game of Coins:

    Given three numbers n, x, and y, 
    Geek and his friend are playing a coin game. 
    
    In the beginning, there are n coins. 
    
    In each move, a player can pick x, y, or 1 coin. 
    
    Geek always starts the game. 
    
    The player who picks the last coin wins the game. 
    
    The task is to determine whether Geek will win 
    the game or not if both players play optimally.

  Q2: Interleaved Strings:

    Given strings A, B, and C, 
    find whether C is formed by 
    an interleaving of A and B.
    
    An interleaving of two strings S and T 
    is a configuration such that it creates 
    a new string Y from the concatenation substrings 
    of A and B and |Y| = |A + B| = |C|
    
    For example:
    
    A = "XYZ"
    
    B = "ABC"
    
    so we can make multiple interleaving string Y like, 
    XYZABC, XAYBCZ, AXBYZC, XYAZBC and many more so here 
    your task is to check whether you can create 
    a string Y which can be equal to C.
    
    Specifically, you just need to create substrings 
    of string A and create substrings B and 
    concatenate them and check whether it is equal to C or not.
    
    Note: a + b is the concatenation of strings a and b.
    
    Return true if C is formed by an 
    interleaving of A and B, else return false.

  Q3: Minimum sum:

    Given an array Arr of size N 
    such that each element is 
    from the range 0 to 9. 
    
    Find the minimum possible sum 
    of two numbers formed using the 
    elements of the array. 
    
    All digits in the given array must 
    be used to form the two numbers.

Day 179:

  Q1: String Subsequence:

    Given two strings, s1 and s2, 
    count the number of subsequences 
    of string s1 equal to string s2.
    
    Return the total count modulo 1e9+7.

  Q2: Number of Provinces:

    Given an undirected graph with V vertices. 
    
    We say two vertices u and v belong to a 
    single province if there is a path from 
    u to v or v to u. 
    
    Your task is to find the number of provinces.
    
    Note: A province is a group of directly or indirectly 
    connected cities and no other cities outside of the group.

  Q3: Smallest distinct window:

    Given a string 's'. 
    
    The task is to find the smallest window 
    length that contains all the characters 
    of the given string at least one time.
    
    For eg. A = aabcbcdbca, then the result 
    would be 4 as of the smallest window will be dbca.

Day 180:

  Q1: Swap two nibbles in a byte:

    Given a number n, 
    Your task is to swap the 
    two nibbles and find the resulting number. 
    
    A nibble is a four-bit aggregation, or half an octet. 
    
    There are two nibbles in a byte. 
    
    For example, the decimal number 150 
    is represented as 10010110 in an 8-bit byte. 
    
    This byte can be divided into two nibbles: 1001 and 0110.

  Q2: Infix to Postfix:

    Given an infix expression in the form of string str. 
    
    Convert this infix expression to postfix expression.
    
    Infix expression: The expression of the form a op b. 
    
    When an operator is in-between every pair of operands.
    
    Postfix expression: The expression of the form a b op. 
    
    When an operator is followed for every pair of operands.
    
    Note: The order of precedence is: ^ greater than * 
    equals to / greater than + equals to -. 
    Ignore the right associativity of ^.

  Q3: Choose and Swap:

    You are given a string s of lower case english alphabets. 
    
    You can choose any two characters in the string and 
    replace all the occurences of the first character 
    with the second character and replace all the occurences 
    of the second character with the first character. 
    
    Your aim is to find the lexicographically smallest 
    string that can be obtained by doing this operation at most once.

Day 181:

  Q1: Odd Even Problem:

    Given a string s of lowercase English characters, 
    determine whether the summation of x and y is EVEN or ODD.
    where:
    
    x is the count of distinct characters that occupy 
    even positions in the English alphabet and have even frequency.
     
    y is the count of distinct characters that 
    occupy odd positions in the English alphabet 
    and have odd frequency.
    
    Ex: string = "ab" here 'a' has an odd(1) 
    position in the English alphabet & has an 
    odd(1) frequency in the string so a is odd 
    but b has an even(2) position in the English 
    alphabet & has odd(1) frequency so it doesn't 
    count(since string doesn't have 2 b's) 
    so the final answer x + y = 1+0 = 1(odd) 
    would be "ODD".
    
    Note: Return "EVEN" if the sum of x & y 
    is even otherwise return "ODD".
    
  Q2: Largest number in K swaps:

    Given a number K and string str of digits 
    denoting a positive integer, 
    build the largest number possible by performing 
    swap operations on the digits of str at most K times.

  Q3: Count number of substrings:

    Given a string of lowercase alphabets, 
    count all possible substrings 
    (not necessarily distinct) that 
    have exactly k distinct characters. 

Day 182:

  Q1: Construct list using given q XOR queries:

    Given a list s that initially 
    contains only a single value 0. 
    
    There will be q queries of the following types:
    
    0 x: Insert x in the list
    1 x: For every element a in s, 
    replace it with a ^ x. ('^' denotes the bitwise XOR operator)
    
    Return the sorted list after performing the given q queries.

  Q2: Unique BSTs:

    Given an integer. 
    
    Find how many structurally unique binary search 
    trees are there that stores the values from 1 
    to that integer (inclusive). 

  Q3: Mother Vertex:

    Given a Directed Graph, 
    find a Mother Vertex in the Graph (if present). 
    
    A Mother Vertex is a vertex through which 
    we can reach all the other vertices of the Graph.

Day 183:

  Q1: Trail of Ones:

    Given a number n, find the number of binary strings 
    of length n that contain consecutive 1's in them. 
    
    Since the number can be very large, 
    return the answer after modulo with 1e9+7.

  Q2: Number of distinct Islands:

    Given a boolean 2D matrix grid of size n * m. 
    
    You have to find the number of distinct islands 
    where a group of connected 1s (horizontally or vertically) 
    forms an island. 
    
    Two islands are considered to be distinct if 
    and only if one island is not equal to another 
    (not rotated or reflected).

  Q3: Arranging the array:

    You are given an array of size N. 
    
    Rearrange the given array in-place such that 
    all the negative numbers occur before all non-negative numbers.
    
    (Maintain the order of all -ve and 
    non-negative numbers as given in the original array).

Day 184:

  Q1: Binary Representation of next number:

    Given a binary representation in the form of a string(s) 
    of a number n, the task is to find a binary representation of n+1.
    
    Note: Output binary string should not contain leading zeros.

  Q2: Reverse a Stack:

    You are given a stack St. 
    You have to reverse the stack using recursion.

  Q3: Number of Enclaves:

    You are given an n x m binary matrix grid, 
    where 0 represents a sea cell and 1 represents 
    a land cell.
    
    A move consists of walking from one land cell to 
    another adjacent (4-directionally) land cell or
    walking off the boundary of the grid.
    
    Find the number of land cells in grid for which 
    we cannot walk off the boundary of the grid 
    in any number of moves.

Day 185:

  Q1: Swapping pairs make sum equal:

    Given two arrays of integers a[] and b[] 
    of size n and m, the task is to check if 
    a pair of values (one value from each array) 
    exists such that swapping the elements of the 
    pair will make the sum of two arrays equal.
    
    Note: Return 1 if there exists any such pair otherwise return -1.

  Q2: Array to BST:

    Given a sorted array. 
    
    Convert it into a Height balanced 
    Binary Search Tree (BST). 
    
    Find the preorder traversal of height balanced BST. 
    
    If there exist many such balanced BST consider 
    the tree whose preorder is lexicographically smallest.
    
    
    Height balanced BST means a binary tree in which 
    the depth of the left subtree and the right subtree 
    of every node never differ by more than 1.

  Q3: Union of Two Linked Lists:

    Given two linked lists, 
    your task is to complete the function makeUnion(), 
    that returns the union list of two linked lists. 
    
    This union list should include all the distinct elements only 
    and it should be sorted in ascending order.

Day 186:


  Q1: Max sum in the configuration:

    Given an integer array(0-based indexing) a of size n. 
    
    Your task is to return the maximum value of the sum 
    of i*a[i] for all 0<= i <=n-1, where a[i] is the 
    element at index i in the array. 
    
    The only operation allowed is to rotate
    (clockwise or counterclockwise) 
    the array any number of times.

  Q2: Print Anagrams Together:

    Given an array of strings, 
    return all groups of strings that are anagrams. 
    
    The groups must be created in order of their 
    appearance in the original array. 
    
    Look at the sample case for clarification.
    
    Note: The final output will be in lexicographic order.

  Q3: Negative weight cycle:

    Given a weighted directed graph with n nodes and m edges. 
    
    Nodes are labeled from 0 to n-1, 
    the task is to check if it contains 
    a negative weight cycle or not.
    
    Note: edges[i] is defined as u, v and weight.

Day 187:

  Q1: Maximum Occured Integer:

    Given n integer ranges, 
    the task is to return the maximum occurring 
    integer in the given ranges. 
    
    If more than one such integer exists, 
    return the smallest one.
    
    The ranges are in two arrays l[] and r[].  
    
    l[i] consists of the starting point of the range 
    and r[i] consists of the corresponding endpoint 
    of the range & a maxx which is the maximum value of r[].
    
    For example, consider the following ranges.
    l[] = {2, 1, 3}, r[] = {5, 3, 9)
    
    Ranges represented by the above arrays are.
    
    [2, 5] = {2, 3, 4, 5}
    [1, 3] = {1, 2, 3}
    [3, 9] = {3, 4, 5, 6, 7, 8, 9}
    
    The maximum occurred integer in these ranges is 3.

  Q2: Jump Game:
  
    Given an positive integer N and a list of N integers A[]. 
    
    Each element in the array denotes the 
    maximum length of jump you can cover. 
    
    Find out if you can make it to the 
    last index if you start at the 
    first index of the list.

  Q3: Prerequisite Tasks:

    There are a total of N tasks, labeled from 0 to N-1. 
    
    Some tasks may have prerequisites, 
    for example to do task 0 you have 
    to first complete task 1, 
    which is expressed as a pair: [0, 1]
    
    Given the total number of tasks N and 
    a list of prerequisite pairs P, 
    find if it is possible to finish all tasks.

Day 188:

  Q1: Index of an Extra Element:

    You have given two sorted arrays arr1[] & arr2[] of distinct elements. 
    
    The first array has one element extra added in between. 
    
    Return the index of the extra element.
    
    Note: 0-based indexing is followed.

  Q2: Subset Sums:

    Given a list arr of n integers, 
    return sums of all subsets in it. 
    
    Output sums can be printed in any order.

  Q3: Kth ANcestor in a Tree:

    Given a binary tree of size  N, 
    a node, and a positive integer k. 
    
    Your task is to complete the function kthAncestor(), 
    the function should return the kth ancestor of the 
    given node in the binary tree. 
    
    If there does not exist any 
    such ancestor then return -1.
    
    Note:
    
    1. It is guaranteed that the node exists in the tree.
    
    2. All the nodes of the tree have distinct values.

Day 189:

  Q1: Convert array into Zig-Zag fashion:

    Given an array arr of distinct elements of size n, 
    the task is to rearrange the elements of the array 
    in a zig-zag fashion so that the converted 
    array should be in the below form: 
    
    arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] 
    < . . . . arr[n-2] < arr[n-1] > arr[n]. 
    
    Note: Modify the given arr[] only, 
    If your transformation is correct, 
    the output will be 1 else the output will be 0. 

  Q2: Merge k Sorted Arrays:

    Given K sorted arrays arranged in the 
    form of a matrix of size K*K. 
    
    The task is to merge them into one sorted array.

  Q3: Find whether path exist:

    Given a grid of size n*n filled with 0, 1, 2, 3. 
    
    Check whether there is a path possible 
    from the source to destination. 
    
    You can traverse up, down, right and left.
    
    The description of cells is as follows:
    
    A value of cell 1 means Source.
    A value of cell 2 means Destination.
    A value of cell 3 means Blank cell.
    A value of cell 0 means Wall.
    
    Note: There are only a single source and a single destination.

Day 190:

  Q1: Nuts and Bolts Problem:

    Given a set of n nuts & bolts. 
    
    There is a one-on-one mapping between nuts and bolts. 
    
    You have to Match nuts and bolts efficiently. 
    
    Comparison of a nut to another nut or a bolt 
    to another bolt is not allowed. 
    
    It means the nut can only be compared with 
    the bolt and the bolt can only be compared 
    with the nut to see which one is bigger/smaller.
    
    The elements should follow the following order: 
    { !,#,$,%,&,*,?,@,^ }
    
    Note: Make all the required changes directly 
    in the given arrays, output will be handled 
    by the driver code.

  Q2: Jumping Numbers:

    Given a positive number X. 
    Find the largest Jumping Number 
    which is smaller than or equal to X. 
    
    Jumping Number: A number is called Jumping Number 
    if all adjacent digits in it differ by only 1. 
    
    All single-digit numbers are considered 
    as Jumping Numbers. 
    
    For example 7, 8987 and 4343456 are 
    Jumping numbers but 796, 677 and 89098 are not.

  Q3: Bleak Numbers:

    Given an integer, check whether it is Bleak or not.
    
    A number n is called Bleak 
    if it cannot be represented as 
    sum of a positive number x and 
    set bit count in x, i.e., 
    x + countSetBits(x) is not equal 
    to n for any non-negative number x.

Day 191:


  Q1: Maximum Tip Calculator:

    In a restaurant, two waiters, 
    A and B, receive n orders per day, 
    earning tips as per arrays arr[i] 
    and brr[i] respectively. 
    
    If A takes the ith order, 
    the tip is arr[i] rupees; if B takes it, 
    the tip is brr[i] rupees.
    
    To maximize total tips, they must distribute the orders such that:
    
    A can handle at most x orders
    
    B can handle at most y orders
    
    Given that x + y ≥ n, all orders can be managed 
    by either A or B. Return the maximum possible 
    total tip after processing all the orders.

  Q2: Word Boggle:

    Given a dictionary of distinct words 
    and an M x N board where every cell 
    has one character. 
    
    Find all possible words from the 
    dictionary that can be formed by 
    a sequence of adjacent characters 
    on the board. 
    
    We can move to any of 8 adjacent characters
    
    Note: While forming a word we can move to 
    any of the 8 adjacent cells. 
    
    A cell can be used only once in one word.

  Q3: Binary Heap Operations:

    A binary heap is a Binary Tree with the following properties:
    
    1) Its a complete tree (All levels are completely 
    filled except possibly the last level and the 
    last level has all keys as left as possible). 
    
    This property of Binary Heap makes them 
    suitable to be stored in an array.
    
    2) A Binary Heap is either Min Heap or Max Heap. 
    
    In a Min Binary Heap, the key at the root 
    must be minimum among all keys present in Binary Heap. 
    
    The same property must be recursively 
    true for all nodes in Binary Tree. 
    
    Max Binary Heap is similar to MinHeap.
    
    You are given an empty Binary Min Heap and 
    some queries and your task is to implement 
    the three methods insertKey,  deleteKey,  
    and extractMin on the Binary Min Heap and 
    call them as per the query given below:
    
    1) 1  x  (a query of this type means to insert an element in the min-heap with value x )
    
    2) 2  x  (a query of this type means to remove an element at position x from the min-heap)
    
    3) 3  (a query like this removes the min element from the min-heap and prints it ).

Day 192:

  Q1: Count numbers containing 4:

    You are given a number n, 
    Return the count of total numbers from 
    1 to n containing 4 as a digit.

  Q2: Kth element in a Matrix:

    Given a N x N matrix, where every row 
    and column is sorted in non-decreasing order. 
    
    Find the kth smallest element in the matrix.

  Q3: Minimum Deletions:

    Given a string of S as input. 
    
    Your task is to write a program to 
    delete the minimum number of characters 
    from the string so that the resultant 
    string is a palindrome.
    
    Note: The order of characters in 
    the string should be maintained.

Day 193:

  Q1: Padovan sequence: 

    Given a number n, 
    find the nth number in the Padovan Sequence.
    
    A Padovan Sequence is a sequence which is 
    represented by the following recurrence relation
    
    P(n) = P(n-2) + P(n-3)
    P(0) = P(1) = P(2) = 1
    
    Note: Since the output may be too large, 
    compute the answer modulo 10^9+7.

  Q2: Count the Reversals:

    Given a string S consisting of only opening 
    and closing curly brackets '{' and '}', 
    find out the minimum number of reversals 
    required to convert the string into a balanced expression.
    
    A reversal means changing '{' to '}' or vice-versa.

  Q3: IPL 2021 - Match Day 2

    Due to the rise of covid-19 cases in India, 
    this year BCCI decided to organize 
    knock-out matches in IPL rather than a league.
    
    Today is matchday 2 and it is between 
    the most loved team Chennai Super Kings 
    and the most underrated team - Punjab Kings. 
    
    Stephen Fleming, the head coach of CSK, 
    analyzing the batting stats of Punjab. 
    
    He has stats of runs scored by all N players 
    in the previous season and he wants to 
    find the maximum score for each and 
    every contiguous sub-list of size K 
    to strategize for the game.

Day 194:

  Q1: Armstrong Numbers:

    You are given a 3-digit number n, 
    Find whether it is an Armstrong number or not.
    
    An Armstrong number of three digits is 
    a number such that the sum of the cubes 
    of its digits is equal to the number itself. 
    
    371 is an Armstrong number since 3^3 + 7^3 + 1^3 = 371. 
    
    Note: Return "true" if it is an 
    Armstrong number else return "false".

  Q2: Preorder to BST:

    Given an array arr[] of N nodes representing 
    preorder traversal of some BST. 
    
    You have to build the BST  
    from the given preorder traversal. 
    
    In Pre-Order traversal, 
    the root node is visited 
    before the left child and 
    right child nodes.

  Q3: Eventual Safe States:

    A directed graph of V vertices and E edges 
    is given in the form of an adjacency list adj.
    
    Each node of the graph is labelled with a 
    distinct integer in the range 0 to V - 1.
    
    A node is a terminal node if there are no outgoing edges. 
    
    A node is a safe node if every possible 
    path starting from that node leads to a terminal node.
    
    You have to return an array containing 
    all the safe nodes of the graph. 
    
    The answer should be sorted in ascending order.

Day 195:

  Q1: Armstrong Numbers:

    You are given a 3-digit number n, 
    Find whether it is an Armstrong number or not.
    
    An Armstrong number of three digits is 
    a number such that the sum of the cubes 
    of its digits is equal to the number itself. 
    
    371 is an Armstrong number since 3^3 + 7^3 + 1^3 = 371. 
    
    Note: Return "true" if it is an 
    Armstrong number else return "false".

  Q2: Preorder to BST:

    Given an array arr[] of N nodes representing 
    preorder traversal of some BST. 
    
    You have to build the BST  
    from the given preorder traversal. 
    
    In Pre-Order traversal, 
    the root node is visited 
    before the left child and 
    right child nodes.

  Q3: Eventual Safe States:

    A directed graph of V vertices and E edges 
    is given in the form of an adjacency list adj.
    
    Each node of the graph is labelled with a 
    distinct integer in the range 0 to V - 1.
    
    A node is a terminal node if there are no outgoing edges. 
    
    A node is a safe node if every possible 
    path starting from that node leads to a terminal node.
    
    You have to return an array containing 
    all the safe nodes of the graph. 
    
    The answer should be sorted in ascending order.

Day 196:

  Q1: Prime Pair with Target Sum:

    Given a number n, find out if n 
    can be expressed as a+b, 
    where both a and b are prime numbers. 
    
    If such a pair exists, 
    return the values of a and b, 
    otherwise return [-1,-1] as an array of size 2.
    
    Note: If [a, b] is one solution with a <= b, 
    and [c, d] is another solution with c <= d, 
    and a < c then  [a, b] is considered as our answer.

  Q2: Smallest factorial number:

    Given a number n. 
    
    The task is to find the smallest number 
    whose factorial contains at least 
    n trailing zeroes.

  Q3: Hamiltonian Path: 

    A Hamiltonian path, is a path in an 
    undirected graph that visits each 
    vertex exactly once. 
    
    Given an undirected graph, 
    the task is to check if a 
    Hamiltonian path is present 
    in it or not.

Day 197:

  Q1: Check if two Line segments Intersect:  

    Given the coordinates of the endpoints(p1,q1, and p2,q2) 
    of the two line segments. 
    
    Check if they intersect or not. 
    
    If the Line segments intersect return 
    true otherwise return false.
    
    Note: Please check the intersection 
    lies within the line segments.

  Q2: Make Matrix Beautiful:

    A beautiful matrix is a matrix in which 
    the sum of elements in each row and column is equal. 
    
    Given a square matrix of size NxN. 
    
    Find the minimum number of operation(s) 
    that are required to make the matrix beautiful. 
    
    In one operation you can increment the 
    value of any one cell by 1.

  Q3: Snake and Ladder Problem:

    Given a 5x6 snakes and ladders board, 
    find the minimum number of dice throws 
    required to reach the destination or 
    last cell (30th cell) from the source (1st cell).
    
    You are given an integer N denoting 
    the total number of snakes and ladders 
    and an array arr[] of 2*N size where 2*i 
    and (2*i + 1)th values denote the starting 
    and ending point respectively of ith 
    snake or ladder. 
    
    The board looks like the following.
    
    Note: Assume that you have complete 
    control over the 6 sided dice. 
    
    No ladder starts from 1st cell.

Day 198:

  Q1: Number of Rectangles in a Circle:

    Given a circular sheet of radius, r. 
    
    Find the total number of rectangles with 
    integral length and width that can be cut 
    from the sheet that can fit on the circle, 
    one at a time.

  Q2: Special Keyboard:

    Imagine you have a special keyboard with the following keys: 
    
    Key 1:  Prints 'A' on screen
    Key 2: (Ctrl-A): Select screen
    
    Key 3: (Ctrl-C): Copy selection to buffer
    Key 4: (Ctrl-V): Print buffer on screen 
    appending it after what has already been printed.
    
    Find maximum numbers of A's that can be 
    produced by pressing keys on the 
    special keyboard N times.

  Q3: Bridge edge in a graph:

    Given a Graph of V vertices and E edges 
    and another edge(c - d), 
    the task is to find if the 
    given edge is a Bridge. i.e., 
    removing the edge disconnects the graph.

Day 199:

  Q1: Find maximum volume of a cuboid:
  
    You are given a perimeter & the area. 
    
    Your task is to return the maximum volume 
    that can be made in the form of a cuboid 
    from the given perimeter and surface area.
    
    Note: Round off to 2 decimal places 
    and for the given parameters, 
    it is guaranteed that an answer always exists.

  Q2: Tree Boundary Traversal:

    Given a Binary Tree, find its Boundary Traversal. 
    
    The traversal should be in the following order: 
    
    Left boundary nodes: defined as the path 
    from the root to the left-most node ie- 
    the leaf node you could reach when you 
    always travel preferring the left subtree 
    over the right subtree. 
    
    Leaf nodes: All the leaf nodes except for 
    the ones that are part of left or right boundary.
    
    Reverse right boundary nodes: defined as the path 
    from the right-most node to the root. 
    
    The right-most node is the leaf node you 
    could reach when you always travel preferring 
    the right subtree over the left subtree. 
    
    Exclude the root from this as it was 
    already included in the traversal 
    of left boundary nodes.
    
    Note: If the root doesn't have a 
    left subtree or right subtree, 
    then the root itself is the left 
    or right boundary. 

  Q3: Smallest Positive Missing:

    You are given an array arr[] of N integers. 
    
    The task is to find the smallest 
    positive number missing from the array.
    
    Note: Positive number starts from 1.

Day 200:

  Q1: Integral Points Inside Triangle:

    Given three non-collinear points whose 
    co-ordinates are p(p1, p2), q(q1, q2) and 
    r(r1, r2) in the X-Y plane. Return the number 
    of integral / lattice points strictly inside 
    the triangle formed by these points.
    
    Note: - A point in the X-Y plane is said to be 
    an integral / lattice point if both its 
    coordinates are integral.

  Q2: K-th smallest element in BST:

    Given a BST and an integer K. 
    
    Find the Kth Smallest element 
    in the BST using O(1) extra space.

  Q3: Heap Sort:

    Given an array of size N. 
    
    The task is to sort the array elements 
    by completing functions heapify() and 
    buildHeap() which are used to implement Heap Sort.  

Day 201:

  Q1: Compare two fractions:

    You are given a string str containing two fractions 
    a/b and c/d, compare them and return the greater. 
    
    If they are equal, then return "equal".
    
    Note: The string str contains "a/b, c/d"
    (fractions are separated by comma(,) & space( )).

  Q2: Palindrome Linked List:

    Given a singly linked list of size N of integers. 
    
    The task is to check if the given 
    linked list is palindrome or not.

  Q3: nCr:

    Given two integers n and r, find nCr.
    
    Since the answer may be very large, 
    calculate the answer modulo 10^9+7.
    
    Note : If r is greater than n, return 0.

Day 202:

  Q1: Directed Graph Cycle:

    Given a Directed Graph with V vertices 
    (Numbered from 0 to V-1) and E edges, 
    check whether it contains any cycle or not.

  Q2: K Sized Subarray Maximum:

    Given an array arr[] of size N and an integer K. 
    
    Find the maximum for each and every 
    contiguous subarray of size K.

  Q3: Extract the Number from the String:

    Given a sentence containing several words and numbers. 
    
    Find the largest number among them which does not contain 9. 
    
    If no such number exists, return -1.
    
    Note: Numbers and words are separated by spaces only.
    
    It is guaranteed that there are no leading zeroes in the answer.

Day 203:

  Q1: Print Bracket Number:

    Given a string str, the task is 
    to find the bracket numbers, 
    i.e., for each bracket in str, 
    return i if the bracket is the 
    i^th opening or closing bracket 
    to appear in the string. 

  Q2: Minimum Jumps:

    Given an array arr[] of size n of non-negative integers. 
    
    Each array element represents the maximum length 
    of the jumps that can be made forward from that element. 
    
    This means if arr[i] = x, then we can 
    jump any distance y such that y ≤ x.
    
    Find the minimum number of jumps to reach the 
    end of the array starting from the first element. 
    
    If an element is 0, then you cannot move through that element.
    Note: Return -1 if you can't reach the end of the array.

  Q3: Sort 0s, 1s and 2s:

    Given an array of size N containing only 
    0s, 1s, and 2s; sort the array in 
    ascending order.

