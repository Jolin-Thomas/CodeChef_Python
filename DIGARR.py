count = 0
n = int(input())
for i in range(n):
    dig = int(input())
    val = input()
    for i in val:
        if(i == '5' or i == '0'):
            count+=1
    if(count > 0):
        print("YES")
    else:
        print("NO")
    count = 0    
