val = []
T = int(input())
for i in range(T):
    v = input()
    val = list(map(int, v.split()))
    if(val[0]<val[1]):
        print("FIRST")
    elif(val[0]>val[1]):
        print("SECOND")
    else:
        print("ANY")




