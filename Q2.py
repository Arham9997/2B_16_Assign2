class Solution:
    def rotateMatrix(self, mat):
        n = len(mat)
        for i in range(n):
            mat[i] = mat[i][::-1]
        for i in range(n):
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
