# https://www.codechef.com/START152D/problems/MNR

for _ in range(int(input())):
    array_length = int(input())
    arr = sorted([int(x) for x in input().split()])

    print(min([arr[-3]-arr[0],arr[-2]-arr[1],arr[-1]-arr[2]]))