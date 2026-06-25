class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seenChar = set()
        left = 0
        right = 0
        best = 0
        while right < len(s):
            while s[right] in seenChar:
                seenChar.remove(s[left])
                left += 1
            seenChar.add(s[right])
            right += 1
            best = max(best,len(seenChar))
        return best
