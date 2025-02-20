
# cook your dish here

t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    amt = x * y 
    bags = amt/100
    print(int(bags))
