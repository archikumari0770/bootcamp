def minCostClimbingStairs(cost: list[int]) -> int:
    a, b = 0, 0
    for c in reversed(cost):
        a, b = c + min(a, b), a
    return min(a, b)