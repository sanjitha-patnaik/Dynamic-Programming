# Longest Increasing Subsequence
# Problem: Find the length of the longest subsequence common to two sequences.
# Approach: Use dynamic programming to store the length of the longest common subsequence for substrings.


def longest_increasing_subsequence_length(nums):
    if not nums:
        return 0

    n = len(nums)
    lis_lengths = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and lis_lengths[i] < lis_lengths[j] + 1:
                lis_lengths[i] = lis_lengths[j] + 1

    return max(lis_lengths)

# Take input from the user
sequence_str = input("Enter the sequence of integers separated by spaces: ")
sequence = list(map(int, sequence_str.split()))

result = longest_increasing_subsequence_length(sequence)
print("Length of Longest Increasing Subsequence:", result)
