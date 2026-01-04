class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        
        if not nums1 or not nums2 or k == 0:
            return []
        
        heap = []
        res = []
        
        # Initialize heap
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        while heap and k > 0:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            k -= 1
            
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return res
