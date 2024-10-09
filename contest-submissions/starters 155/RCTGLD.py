# https://www.codechef.com/START155D/problems/RCTGLD

for _ in range(int(input())):
    n = int(input())
    if n&1==1:
        n-=1
    n = int(n/2)

    if n&1==1:
        n = int((n-1)/2)
        print(n*(n+1))
    else:
        n = int(n/2)
        print(n**2)