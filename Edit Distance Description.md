# Edit Distance

## Problem Statement:
The Edit Distance problem involves finding the minimum number of operations (insertion, deletion, or substitution) required to transform one string into another. Each operation has a cost of 1, and the goal is to minimize the total cost of transforming one string into the other.

## Approach:
Dynamic programming is used to solve the Edit Distance problem by constructing a table (dp) where dp[i][j] represents the minimum edit distance between the first i characters of the first string and the first j characters of the second string. The three possible operations (insertion, deletion, and substitution) are considered, and the minimum cost is calculated.



# Code Overview:

The function edit_distance takes two strings (str1 and str2) as input.

A 2D DP table (dp) is created, initialized, and filled using a bottom-up approach.

The base cases are set for an empty string or when one of the strings is empty.

The DP table is filled based on the three possible operations, and the minimum cost is calculated.

The final result is stored in dp[m][n], where m and n are the lengths of the two strings.



# Time Complexity:
The time complexity of the Edit Distance problem using dynamic programming is O(m * n), where m and n are the lengths of the two input strings. The nested loops iterate through each cell in the DP table, and constant time operations are performed.



# Space Complexity:
The space complexity is O(m * n), where m and n are the lengths of the two input strings. The DP table of size (m + 1) x (n + 1) is created to store the minimum edit distances between substrings.



# Applications:


## Spell Checking and Correction:
Used in spelling correction algorithms to suggest corrections for misspelled words.

## DNA Sequencing:
Applied in bioinformatics to compare and align DNA sequences, identifying genetic variations.

## Machine Translation:
Utilized in machine translation systems to determine the optimal alignment between source and target language sentences.

## Natural Language Processing (NLP):
Used in applications like text summarization and sentiment analysis to understand and transform textual data.

## Version Control Systems:
Employed in version control systems (e.g., Git) to compute the differences between different versions of files.
