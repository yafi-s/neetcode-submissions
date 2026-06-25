class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        best = 0
        left = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[r])
            best = max(best, len(charSet))
        return best