nums = [1,2,3,4]
def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    #self.nums = nums
    for i in range(1,len(nums)):
        nums[i] = nums[i] + nums[i-1] 
    
    #print (nums)
        
    return nums


summed_nums=runningSum([1,2,3,4])
print(summed_nums)