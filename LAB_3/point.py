x=int(input())
y=int(input())
if (x<5 and x>0) and (y>0 and y<3):
    print('Внутри прямоугольника')
elif ((x==5 or x==0) and 0<=y<=3) or ((y==0 or y==3) and 0<=x<=5):
    print('На границе')
elif (x>0 or x>5) or (y<0 or y>3):
    print('За границей')