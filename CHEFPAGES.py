# cook your dish here
n = input()
val = list(map(int, n.strip().split()))
if (val[0] and val[1]):
    print("https://discuss.codechef.com")
if (((val[0] == 1) and (val[1] == 0))):
    print("https://www.codechef.com/contests")
if (((val[0] == 0) and (val[1] == 1)) or ((val[0] == 0) and (val[1] == 0))):
    print("https://www.codechef.com/practice")


