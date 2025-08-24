class Solution:
    def countZeroes(self, A, N):
        s=0
        for i in range(N):
            for j in range(N):
                if A[i][j]==0:
                    s+=1
        return s
