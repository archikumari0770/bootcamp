def numOfSubarrays(arr: list[int], k: int, threshold: int) -> int:
    target = k * threshold
    curr = sum(arr[:k])
    count = 1 if curr >= target else 0
    for i in range(k, len(arr)):
        curr += arr[i] - arr[i - k]
        if curr >= target:
            count += 1
    return count