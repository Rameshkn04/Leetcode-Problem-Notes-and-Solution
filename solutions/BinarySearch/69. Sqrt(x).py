class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l,h = 1,x
        ans = 0
        while l<= h:
            mid = (l+h)//2
            if mid*mid <= x:
                ans = mid
                l = mid + 1
            else:
                h = mid - 1
        return ans
'''
Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
'''
