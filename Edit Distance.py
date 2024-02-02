# EDIT DISTANCE IMPLEMENTATION
# Problem: Find the minimum number of operations (insert, delete, replace) required to convert one string into another.
# Approach: Use dynamic programming to build a table of edit distances between substrings.


def edit_distance(str1, str2):
    m, n = len(str1), len(str2)

    # Create a 2D DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the DP table
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # If the first string is empty, insert all characters from the second
            elif j == 0:
                dp[i][j] = i  # If the second string is empty, delete all characters from the first
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed if characters are the same
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],        # Deletion
                                   dp[i][j - 1],        # Insertion
                                   dp[i - 1][j - 1])    # Substitution

    return dp[m][n]

# Take input from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = edit_distance(str1, str2)
print("Edit Distance between '{}' and '{}': {}".format(str1, str2, result))

