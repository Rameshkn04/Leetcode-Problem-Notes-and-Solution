class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0
        while left < right:

            width = right - left
            area = min(height[left],height[right]) * width
            maxarea = max(area,maxarea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea
