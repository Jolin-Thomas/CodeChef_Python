n=int(input())
for i in range(n):
    v = input();
    val = list(map(int, v.split()))
    if(val[0] >= val[1]):
        print("YES")
    else:
        print("NO")

