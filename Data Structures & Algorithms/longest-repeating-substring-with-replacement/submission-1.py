class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        ans = {}
        best = 0

        l = 0
        maxf = 0

        for r in range(len(s)):
            ans[s[r]] = 1 + ans.get(s[r], 0)
            maxf = max(maxf, ans[s[r]])

            while (r - l + 1) - maxf > k:
                ans[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best