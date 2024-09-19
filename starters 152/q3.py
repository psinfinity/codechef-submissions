# https://www.codechef.com/START152D/problems/WFWIN

for _ in range(int(input())):
    mp = [int(x) for x in input().split()]
    n = 0
    while sum(mp) + 21 * (n+1) <= 1000 and n < 299-mp[0]:
        n+=1
    print(n)