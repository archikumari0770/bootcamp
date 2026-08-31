def rob(nums: list[int]) -> int:
    rob1, rob2 = 0, 0
    for num in nums:
        rob1, rob2 = rob2, max(num + rob1, rob2)
    return rob2