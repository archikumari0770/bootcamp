from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not t or not s: return ""
    target_counts = Counter(t)
    required = len(target_counts)
    left = right = formed = 0
    window_counts = {}
    ans = (float("inf"), None, None)

    while right < len(s):
        character = s[right]
        window_counts[character] = window_counts.get(character, 0) + 1
        if character in target_counts and window_counts[character] == target_counts[character]:
            formed += 1

        while left <= right and formed == required:
            character = s[left]
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            window_counts[character] -= 1
            if character in target_counts and window_counts[character] < target_counts[character]:
                formed -= 1
            left += 1

        right += 1

    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]