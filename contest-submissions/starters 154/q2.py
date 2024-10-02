# https://www.codechef.com/START154D/problems/CALLIM
for _ in range(int(input())):
    nk = [int(x) for x in input().split()]
    sweets = [int(x) for x in input().split()]

    for i in range(nk[0]):

        if sweets[0] > nk[1]:
            print(0)
            break
        elif sum(sweets[:i+2]) > nk[1] and sum(sweets[:i+1]) <= nk[1]:
            print(i+1)
            break
        elif i==nk[0]-1:
            print(nk[0])
