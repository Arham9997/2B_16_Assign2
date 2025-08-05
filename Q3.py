class Solution:
    def DiagonalSum(self, mat):
        s=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j:
                    s+=mat[i][j]
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i+j==len(mat)-1:
                    s+=mat[i][j]
        return s
