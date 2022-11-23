# Each time can climb up 1 or 2 stairs.
def climbStairs(n):
    one,two = 1,1
    for j in range(n-1):
        temp = one
        one=one+two
        two = temp
    return one

climbStairs(5)
