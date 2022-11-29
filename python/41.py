class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        testDict = {}
        nums.append(0)
        for num in nums:
            testDict[num]=0
        for i in range(1,len(nums)+1):
            if testDict.get(i) == None:
                return i
