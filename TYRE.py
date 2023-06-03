n = int(input())
for i in range(n):
    v = input()
    val = list(map(int, v.split()))
    tot = (val[0]*2) + (val[1]*4)
    print(tot)