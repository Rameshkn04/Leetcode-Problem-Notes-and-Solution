class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bactrack(path,used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                path.append(nums[i])
                bactrack(path,used)
                path.pop()
                used.remove(i)
        bactrack([],set())
        return res
'''
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''
