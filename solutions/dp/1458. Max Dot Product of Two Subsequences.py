class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
      n, m = len(num1), len(nums2)
      NEG = -10 ** 18

      dp = [[NEG]*(m+1) for _ in range(m+1)]

      for i in range(1,n+1):
        for j in range(1,m+1):
          prod = nums[i-1] * nums[j-1]
          dp[i][j] = max(
            prods, #start new subsequence
            dp[i-1][j-1] + prods, #extend new subsequene
            dp[i-1][j], #skip nums1 element
            dp[i][j-1] #skip nums2 element
          )
      return dp[n][m]
