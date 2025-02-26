
# cook your dish here

for _ in range(int(input())):
    x,y,z = map(int,input().split())
    if x==0 and y==0 and z==0:
        print("Water filling time")
    elif x==1 and y==1 and z==1:
        print("Not now")
    elif ((x==0 and y==0 and z==1) or (x==1 and y==0 and z==0) or (x==0 and y==1 and z==0)):
        print("Water filling time")
    elif ((x==1 and y==1 and z==0)or(x==0 and y==1 and z==1)or(x==1 and y==0 and z==1)):
        print("Not now")
    
