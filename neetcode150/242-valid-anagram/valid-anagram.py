class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the length is not equal return False and exit 
        if len(s) != len(t):
            return False
        
        #make two dictionaries
        countS, countT = {}, {}

        #now just keep log of characters present in both the strings and their frequency
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
        
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT