class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = defaultdict(int)
        left = 0
        best = 0
        maxf = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            maxf = max(freq[s[right]], maxf)

            if right - left + 1 - maxf > k:
                freq[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best