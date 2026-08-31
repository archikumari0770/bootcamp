def findMaxLength(nums: list[int]) -> int:
    prefix_map = {0: -1}
    curr = max_len = 0
    for i, num in enumerate(nums):
        curr += 1 if num == 1 else -1
        if curr in prefix_map:
            max_len = max(max_len, i - prefix_map[curr])
        else:
            prefix_map[curr] = i
    return max_len