# https://www.codechef.com/START152D/problems/MAXHAMDIST

for _ in range(int(input())):
    hammed_sum = 0
    nm = [int(x) for x in input().split()]
    # n = length of string
    # m = number of string
    binaries = []
    for _ in range(nm[1]):
        binaries.append(input())

    for i in range(nm[0]):

        q_counter = 0
        counter0 = 0
        counter1 = 0

        for j in binaries:
            if j[i] == '1':
                counter1+=1
            elif j[i] == '0':
                counter0+=1
            else:
                q_counter+=1

        while q_counter > 0:
            q_counter -= 1
            if counter1 > counter0:
                counter0 += 1
            else:
                counter1 += 1

        hammed_sum += counter1*counter0

    print(hammed_sum)