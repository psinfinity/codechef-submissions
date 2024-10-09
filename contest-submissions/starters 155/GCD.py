# https://www.codechef.com/START155D/problems/GCD_1
import sys

for _ in range(int(sys.stdin.readline())):
    row,column = [int(x) for x in sys.stdin.readline().split()]
    prime_list = [2,3]
    i=4
    while len(prime_list)<row+column:
        i+=1
        for j in prime_list:
            if i%j==0:
                break
            if j==prime_list[-1] or j**2>i:
                prime_list.append(i)
                break
    for n in range(row):
        for m in range(column):
            if m==column-1:
                print(prime_list[m+n])
            else:
                print(prime_list[m+n], end=" ")
