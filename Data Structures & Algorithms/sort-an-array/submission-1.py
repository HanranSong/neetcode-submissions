class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        offset = 50000
        count = [0] * 100001
        for i in nums:
            count[i + offset] += 1
        result = []
        for i in range(100001):
            result.extend([i - 50000] * count[i])
        return result