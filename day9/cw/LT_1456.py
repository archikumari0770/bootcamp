def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    curr = sum(1 for i in range(k) if s[i] in vowels)
    ans = curr
    for i in range(k, len(s)):
        curr += (s[i] in vowels) - (s[i - k] in vowels)
        ans = max(ans, curr)
    return ans