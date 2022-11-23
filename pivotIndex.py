nums = [1,-1,4]

def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    for i in range(0,len(nums)):
        #print(nums[i])

        Left,Right =list(),list()
        for j in range(0,len(nums)):
            if j<i :
                Left.append(nums[j])
            if j>i:
                Right.append(nums[j])

        sumLeft = sum(Left)
        sumRight = sum(Right)

        #print(sumLeft)
        #print(sumRight)


        #print(i)

        if sumLeft==sumRight:
            #print(i)
            index =i
            break
        
        else:
            index =-1

    return index

print(pivotIndex(nums))
