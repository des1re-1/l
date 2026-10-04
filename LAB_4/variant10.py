k=0
sm=0
for i in range(int(input())):
    a=int(input())
    if a>=10:
        k+=1
        sm+=a
print(k, sm)