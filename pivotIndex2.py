nums = [1,7,3,6,5,6]

def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    for i in range(1,len(nums)):
        Left = nums[:i]
        Right = nums[i+1:]

        sumLeft = sum(Left)
        sumRight = sum(Right)

        if sumLeft==sumRight:
            #print(i)
            index =i
            break
        
        else:
            index =-1

    return index

print(pivotIndex(nums))
'''nums = [1,7,3,6,5,6]
i=5

Left = nums[:i]
Right = nums[i+1:]

print(Left)

print(Right)'''