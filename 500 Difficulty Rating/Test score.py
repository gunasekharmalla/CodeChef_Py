
# cook your dish here

for _ in range(int(input())):
    n, x, y =map(int,input().split())
    if y%x==0:
        print("yes")
    else:
        print("no")
