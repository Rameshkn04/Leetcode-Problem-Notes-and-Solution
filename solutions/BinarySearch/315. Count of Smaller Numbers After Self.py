class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        enum = list(enumerate(nums))  # (index, value)

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            merged = []
            i = j = 0
            right_count = 0

            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    merged.append(left[i])
                    res[left[i][0]] += right_count
                    i += 1
                else:
                    merged.append(right[j])
                    right_count += 1
                    j += 1

            while i < len(left):
                merged.append(left[i])
                res[left[i][0]] += right_count
                i += 1

            merged.extend(right[j:])
            return merged

        merge_sort(enum)
        return res
