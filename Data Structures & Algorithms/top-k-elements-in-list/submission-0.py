class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for num, frequency in count.items():
            buckets[frequency].append(num)
        result = []
        for frequency in range(len(nums), 0, -1):
            result.extend(buckets[frequency])
            if len(result) >= k:
                return result[:k]
