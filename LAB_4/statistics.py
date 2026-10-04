k=0
e=0
mx=-1000000
for i in range(int(input())):
    b=int(input())
    if b>0:
        k+=1
        e+=b
        mx=max(mx,b)
print(k, e, mx)
