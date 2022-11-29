class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_num=-101
        k=0
        for list_num in nums:
            if (list_num > last_num):
                last_num=list_num
                nums[k]=list_num
                k+=1
        return k
