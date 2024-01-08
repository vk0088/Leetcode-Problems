class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        l = len(num)-1
        if l%2 == 0:
            return num[l//2]
        else:
            return (num[l//2] + num[l//2+1])/2