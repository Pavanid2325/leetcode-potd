class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = [False]*len(matrix[0])
        for i in range(len(matrix)):
            zero = False
            for j in range(len(matrix[0])):
                if(matrix[i][j] == 0):
                    zero = True
                    row[j] = True
            if(zero):
                matrix[i]=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(row[j]):
                    matrix[i][j] = 0 
        return 
        