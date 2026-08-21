class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        nums1.sort()
        if(len(nums1)==m+n):
            return nums1
        elif(len(nums1)>m+n):
            while(len(nums1)!=m+n):
                nums1.remove(0)
            return nums1
        else:
            while(len(nums1)!=m+n):
                nums1.append(0)
            nums1.sort()
            return nums1
