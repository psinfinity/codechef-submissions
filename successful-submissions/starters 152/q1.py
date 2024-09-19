# https://www.codechef.com/START152D/problems/CHOLY

xyz = [int(x) for x in input().split()]
# x = 1, y=0.5, z=0

if xyz[0] + xyz[1]*0.5 +(4-sum(xyz)) > 2:
    print('YES')

else:
    print('NO')