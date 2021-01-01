# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
#  
#
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#  
#
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
#  
#
# Example:
#
#
# Input: [2,1,5,6,2,3]
# Output: 10
#
#


###单调栈
class Solution:
    def largestRectangleArea(self, heights):
        
        """
        :type heights: List[int]
        :rtype: int
        """
        
        i = 0
        max_value = 0
        stack = []
        heights.append(0)
       
        while i < len(heights):
            
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                now_idx = stack.pop()
                
                if len(stack) == 0:
                    max_value = max(max_value,i * heights[now_idx])
                else:                    
                    max_value = max(max_value,(i- stack[-1] -1) * heights[now_idx])
                    
        return max_value


##动态规划
