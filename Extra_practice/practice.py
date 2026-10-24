'''import random
def random_list(length):
    randlist=[]
    for i in range(1,length+1):
        n=random.randint(1,10)
        randlist.append(n)
    return randlist

r=random_list(20)
print(r)'''

'''l1=[]
for i in range(1,31):
    l1.append(i)
print(l1)

l2=[]
for i in l1:
    if i%2==0:
        l2.append(i)
print(l2)

l3=[]
l3.append(l2[0:5])
print(l3)'''

'''from turtle import*
color('red',"blue")
begin_fill()
forward(200)
left(120)
forward(200)
left(120)
forward(200)
end_fill()
done()'''

'''import turtle
#initialising turtle
t=turtle.Turtle()

colors=['green','purple','blue']
r=10
n=7
for i in range(n+1,0,-1):
    t.color('black',colors[i%3])
    t.begin_fill()
    t.circle(r*i)
    t.end_fill()'''

sides=int(input("enter number of sides:"))
length=int(input("enter side length:"))
angle=360/sides

from turtle import*
color('purple','green')
begin_fill()

for i in range(sides):
    forward(length)
    left(angle)

end_fill()