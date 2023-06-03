n = int(input())
for i in range(n):
    v = input()
    val = list(map(int, v.split()))
    print(val[0] - val[1])