class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        storeVals = []
        totalLen = len(nums1)+len(nums2)

        if(len(nums2)<len(nums1)):
            temp=nums1
            nums1=nums2
            nums2=temp

        while(len(nums1)!=0):
            if(len(nums2) == 0):
                storeVals+=nums1
                break
            if (nums1[i] > nums2[0]):
                storeVals.append(nums2.pop(0))
            elif nums1[i] == nums2[0]:
                storeVals.append(nums2.pop(0))
                storeVals.append(nums1.pop(0))
            else:
                storeVals.append(nums1.pop(0))

        if len(nums2) != 0:
            storeVals+=nums2
            
        if (totalLen % 2 == 0):
            indexVal = int(totalLen/2)
            return ((storeVals[indexVal-1] + storeVals[indexVal])/2)
        else:
            indexVal = int(math.floor(totalLen/2))
            return storeVals[indexVal]
