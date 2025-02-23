class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(r - l):
                t1, t2 = l, r
                topLeft = matrix[t1][l + i]
                matrix[t1][l + i] = matrix[t2 - i][l]
                matrix[t2 - i][l] = matrix[t2][r - i]
                matrix[t2][r - i] = matrix[t1 + i][r]
                matrix[t1 + i][r] = topLeft

            r-=1
            l+=1