# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.


class Solution:
    def numSquares(self, n: int) -> int:
        Q = collections.deque([n])
        visited, level = set(), 0
        while Q:
            # 按层处理
            for i in range(len(Q)):
                n = Q.popleft()
                # 若n==0，则返回当前层数
                if n == 0: return level
                # 依次减去所有比n小的平方数
                for i in range(1,int(n**0.5)+1):
                    val = n - i**2
                    if val in visited: continue
                    Q.append(val)
                    visited.add(val)
            level = level + 1
        return (level)
