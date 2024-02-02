# Problem: Longest Increasing Subsequence (LIS)

Given an array of integers, find the length of the Longest Increasing Subsequence.

## Input:
An array of integers nums (0 <= len(nums) <= 1000).

## Output:
An integer representing the length of the Longest Increasing Subsequence.
Example: In the sequence 3 8 5 7 2 5 9 6 7
         The longest increasing subsequence is 4 (The sequence being - 3 5 7 9)

## Note:
The Longest Increasing Subsequence does not need to be contiguous. The elements should be in strictly increasing order.

# Time Complexity:
The time complexity of the Longest Increasing Subsequence (LIS) problem using dynamic programming is O(n^2), where n is the length of the input sequence. The nested loops iterate through each pair of elements in the sequence, and for each pair, constant time operations are performed. Therefore, the overall time complexity is quadratic.

# Space Complexity:
The space complexity is O(n), where n is the length of the input sequence. This is because we use an array (lis_lengths) of size n to store the lengths of the increasing subsequences ending at each position in the input sequence.


# Code Overview:
1.The function longest_increasing_subsequence_length takes a list of integers (nums) as input.
2.It initializes an array lis_lengths to store the length of the longest increasing subsequence ending at each position. The initial value for each position is set to 1
3.It then iterates through each pair of indices in the input sequence, comparing the elements at those indices.
4.If the element at the current index is greater than the element at the previous index and the length of the subsequence at the current index can be extended, it updates the length.
5.The function returns the maximum value in the lis_lengths array, representing the length of the overall Longest Increasing Subsequence.


# Applications:

1.Longest Increasing Subsequence has applications in various areas such as data compression, DNA sequencing, and optimizing resource allocation.
2.In bioinformatics, LIS is used to find the longest chain of nucleotides in a DNA sequence that is in increasing order.
3.In finance, it can be applied to analyze stock prices or currency exchange rates to identify trends.
4.In computer graphics, it is used in algorithms for finding the longest increasing subsequence of points in a given two-dimensional space, which can be applied to tasks like gesture recognition.




