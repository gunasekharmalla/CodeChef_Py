
import math as m
t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    q = n / 6
    print(m.ceil(q) * x)
