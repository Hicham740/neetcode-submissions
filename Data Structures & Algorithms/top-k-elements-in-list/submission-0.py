class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        arr =[]

        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1

        for i in range(k):

            max_key = max(d, key=d.get)
            arr.append(max_key);
            d[max_key]=0;

        return arr ;