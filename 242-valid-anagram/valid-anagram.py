class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 1)

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 1)

        return (countS == countT)