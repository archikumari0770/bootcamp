from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    q = deque()
    res = []
    for i, num in enumerate(nums):
        while q and q[-1] < num:
            q.pop()
        q.append(num)
        if i >= k and nums[i - k] == q[0]:
            q.popleft()
        if i >= k - 1:
            res.append(q[0])
    return res