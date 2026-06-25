class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
       
        if len(s) != len(t):
            return False
       
        mapS = defaultdict(int)
        mapT = defaultdict(int)

        
        for i in range(len(s)):
            mapT[t[i]] += 1
            mapS[s[i]] += 1

        if mapS == mapT:
            return True
        
        return False 