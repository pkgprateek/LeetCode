class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        cross = set()
        for pair in nums:
            for j in range(pair[0], pair[1]+1):
                cross.add(j)
        return len(cross)