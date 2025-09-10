class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(ch):
            return ch in "aeiou"
        n = len(s)
        cnt = ans = 0
        for i in range(k):
            if is_vowel(s[i]):
                cnt += 1
        ans = max(ans, cnt)
        if ans == k:
            return ans
        for i in range(k, n):
            if is_vowel(s[i]):
                cnt += 1
            if is_vowel(s[i - k]):
                cnt -= 1
            ans = max(ans, cnt)
        return ans