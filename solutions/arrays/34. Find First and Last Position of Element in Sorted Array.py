class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums,target):
            left = 0
            right = len(nums) -1
            index = -1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    index = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else :
                    right = mid - 1
            return index
        def find_right(nums,target):
            left = 0
            right = len(nums) -1
            index = -1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    index = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else :
                    right = mid - 1
            return index
        left_index = find_left(nums,target)
        right_index = find_right(nums,target)
        return [left_index, right_index]

