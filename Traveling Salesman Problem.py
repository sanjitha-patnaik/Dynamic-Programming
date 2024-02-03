# Traveling Salesman Problem

def tsp(graph):
    n = len(graph)
    # dp[mask][i]: minimum cost to visit all cities in the mask ending in city i
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Starting from city 0
    
    # Iterate over all subsets of cities
    for mask in range(1, 1 << n, 2):  # Start from 1 to skip the subset with only city 0
        for u in range(1, n):
            if mask & (1 << u):  # Check if city u is in the subset represented by the mask
                for v in range(n):
                    if mask & (1 << v) and u != v:
                        dp[mask][u] = min(dp[mask][u], dp[mask ^ (1 << u)][v] + graph[v][u])

    # Reconstruct the tour and calculate the minimum cost
    mask = (1 << n) - 1
    u = 0
    min_cost = min(dp[mask][v] + graph[v][u] for v in range(1, n))

    return min_cost

# Example Usage:
# Representing the graph as an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

result = tsp(graph)
print("Minimum Cost of TSP:", result)

