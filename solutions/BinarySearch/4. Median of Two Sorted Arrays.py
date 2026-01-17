class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x , y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low+high) // 2
            partitionY = (x + y + 1)// 2 - partitionX

            mxlx = float('-inf') if partitionX ==  0 else nums1[partitionX - 1]
            mnrx = float('inf') if partitionX == x  else nums1[partitionX]

            mxly = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            mnry = float('inf') if partitionY == y else nums2[partitionY]

            if mxlx <= mnry and mxly <= mnrx:
                if(x+y)% 2 == 0:
                    return (max(mxlx,mxly)+ min(mnrx,mnry)) / 2
                else:
                    return max(mxlx,mxly)
            elif mxlx > mnry:
                high = partitionX - 1
            else:
                low = partitionX + 1
'''
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
