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
