# Longest Common Subsequence
# The Longest Common Subsequence (LCS) problem involves finding the length of the longest subsequence common to two given sequences. 
def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)

    # Create a 2D DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the DP table using bottom-up approach
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from the DP table
    lcs_length = dp[m][n]
    lcs = [''] * lcs_length
    i, j, k = m, n, lcs_length - 1

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[k] = str1[i - 1]
            i -= 1
            j -= 1
            k -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)

# Take input from the user
sequence1 = input("Enter the first sequence: ")
sequence2 = input("Enter the second sequence: ")

result = longest_common_subsequence(sequence1, sequence2)
print(f"Longest Common Subsequence: {result}")

