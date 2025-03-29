class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev = [0] * (len(t) + 1)
        prev[len(t)] = 1
        curr = [0] * (len(t) + 1)


        for i in range(len(s) -1, -1, -1) :
            curr[len(t)] = 1
            for j in range(len(t) -1, -1, -1):
                if s[i] == t[j]:
                    curr[j] = prev[j+1] + prev[j]
                else:
                    curr[j] = prev[j]

            prev, curr = curr, prev

        return prev[0]
