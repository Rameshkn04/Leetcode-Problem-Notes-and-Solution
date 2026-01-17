class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    res = mid
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        
        def findRight():
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    res = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        
        return [findLeft(), findRight()]
'''
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''
