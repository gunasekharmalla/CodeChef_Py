
# cook your dish here

for _ in range(int(input())):
    a,b = map(int,input().split())
    if b > a:
        print(0)
    else:
        print(a-b)
