class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights)-1
        i =0

        maxam =(j - i) * min(heights[i], heights[j])

        while i < j :
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j-= 1
            else :

                t=i
                k=j
                while t < k and heights[t] == heights[k]:
                    t+= 1
                    k -= 1
                if heights[t] < heights[k]:
                        j-= 1
                else:
                        i +=1
            
            if maxam < (j - i) * min(heights[i], heights[j]):
                maxam =(j - i) * min(heights[i], heights[j])
        
        return maxam ;



