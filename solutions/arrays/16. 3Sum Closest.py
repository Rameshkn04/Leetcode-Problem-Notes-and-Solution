class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1
            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if abs(target-total) < abs(target-closest):
                    closest = total
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return target
        return closest
'''
Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''
