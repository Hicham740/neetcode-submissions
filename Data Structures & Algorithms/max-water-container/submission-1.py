class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights)-1
        i =0

        maxam =(j - i) * min(heights[i], heights[j])

        while i < j :
            if heights[i] < heights[j]:
                i += 1
            else:
                j-= 1
            
            
            if maxam < (j - i) * min(heights[i], heights[j]):
                maxam =(j - i) * min(heights[i], heights[j])
        
        return maxam ;



