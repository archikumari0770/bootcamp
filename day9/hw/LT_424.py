from collections import Counter

def characterReplacement(s: str, k: int) -> int:
    counts = Counter()
    max_freq = left = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        max_freq = max(max_freq, counts[s[right]])
        if (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1
    return len(s) - left