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

  
