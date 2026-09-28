class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(target in nums):
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if(nums[i]<target):
                    try: 
                        if(nums[i+1]>target):
                            nums.insert(i+1,target)
                        else:
                            nums.append(target)
                    except:
                        nums.append(target)
                if(target<nums[0]):
                    nums.insert(0,target)
                    
            return nums.index(target)
