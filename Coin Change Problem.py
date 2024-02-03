# Coin Change Problem
# Problem: Given a set of coin denominations and a target amount, find the number of ways to make the target amount using any combination of coins.

def coin_change_ways(coins, target):
    # Create a table to store the number of ways for each amount
    dp = [0] * (target + 1)

    # There is one way to make amount 0, i.e., using no coins
    dp[0] = 1

    # Iterate through each coin denomination
    for coin in coins:
        # Update the table for each amount from the current coin denomination up to the target
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]

    return dp[target]

# Example Usage:
coins = [1, 2, 5]
target = 10
result = coin_change_ways(coins, target)
print(f"Number of ways to make {target} using given coins: {result}")
