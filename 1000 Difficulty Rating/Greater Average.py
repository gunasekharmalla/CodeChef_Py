
t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    
    avg = (a + b ) / 2
    if avg > c:
        print("yes")
    else:
        print("no")
