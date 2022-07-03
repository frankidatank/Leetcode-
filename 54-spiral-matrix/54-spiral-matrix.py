class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top,bottom = 0,len(matrix) - 1
        left,right = 0, len(matrix[0]) - 1
        
        while left <= right and top <= bottom:
            #get first row
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top += 1
            #now right col down
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                #bottom col
                for i in range(right ,left - 1,-1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                #finally left col up
                for i in range(bottom , top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res
                    