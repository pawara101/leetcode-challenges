def tribonacci(n):
    # T0 = 0 T1 = 1 T2 = 1
    T0,T1,T2 = 0,1,1

    if n==0:
        T2 = 0

    elif n==1:
        T2 = 1

    elif n == 2:
        T2 = 1

    else:
        for j in range (n-2):

            Tnew = T0+T1+T2
            T0 = T1
            T1 = T2
            T2 = Tnew

    return T2

print(tribonacci(25))