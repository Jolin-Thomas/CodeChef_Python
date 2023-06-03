n = int(input())
for i in range(n):
    v = input()
    val = list(map(int, v.split()))
    if((val[1] - val[2]) >= val[0]):
        print("YES")
    else:
        print("NO")