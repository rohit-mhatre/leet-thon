class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        temp1, temp2 = cost[0], cost[1]
        for i in range(2, n):
            temp3 = min(temp1, temp2) + cost[i]
            temp1 = temp2
            temp2 = temp3
        return min(temp1,temp2)