
#factorial


def fac(n):
    if n==1 or n==0:
        return 1
    elif n<0:
        print("n is negative")
        return
    else:
        return n*fac((n-1))

print(fac(2))