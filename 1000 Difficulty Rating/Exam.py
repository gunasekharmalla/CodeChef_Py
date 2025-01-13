#coock your dish here

t = int(input())
for _ in range(t):
    x,y,z = map(int,input().split())
    tot = x * y 
    per = (z/tot)*100
    if per > 50:
        print("yes")
    else:
        print("no")
