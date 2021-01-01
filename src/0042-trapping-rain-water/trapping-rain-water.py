# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
#  
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#  
# Constraints:
#
#
# 	n == height.length
# 	0 <= n <= 3 * 104
# 	0 <= height[i] <= 105
#
#


#####################################双指针   1
"""
class Solution:
    def trap(self, height):
 
        """
        #:type height: List[int]
        #:rtype: int
"""
        #双指针法
        if not height: return 0
        n, res = len(height), 0
        left_max, right_max = [0] * n, [0] * n
 
        left_max[0] = height[0]
        for i in range(1, n):  # 从左向右扫描一遍，求出每个位置左边最高的边
            left_max[i] = max(height[i], left_max[i - 1])
 
        right_max[n - 1] = height[n - 1]
        for i in range(n-2, -1, -1):  # 从右向左扫描一遍，求出每个位置右边最高的边
            right_max[i] = max(height[i], right_max[i + 1])
 
        for i in range(1, n-1):  # 扫描每一个位置，用当前位置左右最短的边，作为长度，并减去当前位置的值，就是当前位置的容量
            res += min(left_max[i], right_max[i]) - height[i]
        return res
 
 
if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solu = Solution()

"""

###################################双指针法  2    
class Solution:
    def trap(self, height):
 
        if not height: return 0
        left_max = right_max = res = 0
        left, right = 0, len(height) - 1
 
        while left < right:
            if height[left] < height[right]:  # 左指针操作
                if height[left] < left_max:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1  # 移动左指针
            else:
                if height[right] < right_max:  # 右指针操作
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1  # 移动右指针
        return res
 
 
if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solu = Solution()
    print(solu.trap(height))
    
###################################动态栈栈法  3

