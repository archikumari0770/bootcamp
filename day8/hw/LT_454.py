from collections import Counter

def fourSumCount(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    count1 = Counter(a + b for a in nums1 for b in nums2)
    return sum(count1[-(c + d)] for c in nums3 for d in nums4)