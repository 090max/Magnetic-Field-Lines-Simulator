import turtle
a=input("Enter \"alternate\" or \"possitive\" or \"negative\" ")
turtle.speed(10)
if a=='alternate':
    turtle.penup()
    turtle.setposition(-100,0)
    turtle.pd()
    turtle.circle(50,360)
    turtle.pu()
    turtle.setposition(-110,50)
    turtle.pd()
    turtle.forward(20)
    turtle.pu()
    turtle.setposition(-100,40)
    turtle.pd()
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)

    turtle.penup()
    turtle.setposition(100,0)
    turtle.pd()
    turtle.circle(50,360)
    turtle.pu()
    turtle.setposition(90,50)
    turtle.pd()
    turtle.forward(20)

    turtle.pu()
    turtle.setposition(-100,0)
    turtle.pd()
    turtle.right(90)
    turtle.circle(100,180)

    turtle.left(180)
    turtle.pu()
    turtle.setposition(-90,4)
    turtle.pd()
    turtle.circle(90,180)

    turtle.right(180)
    turtle.pu()
    turtle.setposition(-80,7)
    turtle.pd()
    turtle.circle(80,180)

    turtle.left(180)
    turtle.pu()
    turtle.setposition(-60,20)
    turtle.pd()
    turtle.circle(60,180)

    turtle.right(90)
    turtle.pu()
    turtle.setposition(-50,50)
    turtle.pd()
    turtle.forward(100)
    #the above

    turtle.pu()
    turtle.setposition(100,100)
    turtle.pd()
    turtle.left(90)
    turtle.circle(100,180)

    turtle.pu()
    turtle.setposition(90,95)
    turtle.pd()
    turtle.right(180)
    turtle.circle(90,180)

    turtle.pu()
    turtle.setposition(80,90)
    turtle.pd()
    turtle.right(180)
    turtle.circle(80,180)

    turtle.pu()
    turtle.setposition(60,80)
    turtle.pd()
    turtle.right(180)
    turtle.circle(60,180)

    
    #for arrow
    turtle.left(90)
    turtle.pu()
    turtle.setposition(-100,250)
    turtle.pd()
    turtle.forward(200)
    print(turtle.position())
    turtle.left(150)
    turtle.forward(50)
    turtle.setposition(100.00,250.00)
    turtle.right(300)
    turtle.forward(50)

    

elif a=='possitive':
    turtle.penup()
    turtle.setposition(-100,0)
    turtle.pd()
    turtle.circle(50,360)
    turtle.pu()
    turtle.setposition(-110,50)
    turtle.pd()
    turtle.forward(20)
    turtle.pu()
    turtle.setposition(-100,40)
    turtle.pd()
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)

    turtle.penup()
    turtle.setposition(100,0)
    turtle.pd()
    turtle.circle(50,360)
    turtle.pu()
    turtle.setposition(90,50)
    turtle.pd()
    turtle.forward(20)
    turtle.pu()
    turtle.setposition(100,40)
    turtle.pd()
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)

#for lines
    turtle.pu()
    turtle.setposition(-110,95)
    turtle.pd()
    turtle.left(90)
    turtle.circle(90,180)

    turtle.pu()
    turtle.setposition(-120,90)
    turtle.pd()
    turtle.right(180)
    turtle.circle(80,180)

    turtle.pu()
    turtle.setposition(-270,6)
    turtle.pd()
    turtle.circle(80,180)

    turtle.pu()
    turtle.setposition(-290,4)
    turtle.pd()
    turtle.right(180)
    turtle.circle(90,180)

    turtle.pu()
    turtle.setposition(-100,100)
    turtle.pd()
    turtle.circle(100,180)

    turtle.pu()
    turtle.setposition(-300,0)
    turtle.pd()
    turtle.circle(100,180)

    turtle.pu()
    turtle.setposition(290,95)
    turtle.pd()
    turtle.circle(90,180)

    turtle.pu()
    turtle.setposition(280,90)
    turtle.pd()
    turtle.right(180)
    turtle.circle(80,180)

    turtle.pu()
    turtle.setposition(110,4)
    turtle.pd()
    turtle.circle(90,180)

    turtle.pu()
    turtle.setposition(120,6)
    turtle.pd()
    turtle.right(180)
    turtle.circle(80,180)

    turtle.pu()
    turtle.setposition(100,0)
    turtle.pd()
    turtle.right(180)
    turtle.circle(100,180)

    turtle.pu()
    turtle.setposition(300,100)
    turtle.pd()
    turtle.circle(100,180)

#for arrows
    turtle.pu()
    turtle.setposition(100,180)
    turtle.pd()
    turtle.left(135)
    turtle.forward(140)
    turtle.left(150)
    turtle.forward(50)
    turtle.setposition(198.99,278.99)
    turtle.right(300)
    turtle.forward(50)
    turtle.left(15)#pointing down

    turtle.pu()
    turtle.setposition(-100,180)
    turtle.pd()
    turtle.right(135)
    turtle.forward(140)
    print(turtle.position())
    turtle.right(150)
    turtle.forward(50)
    turtle.setposition(-198.99,278.99)
    turtle.left(300)
    turtle.forward(50)
    turtle.right(15)#pointing down

if a=='negative':
    turtle.penup()
    turtle.setposition(100,0)
    turtle.pd()
    turtle.circle(50,360)
    turtle.pu()
    turtle.setposition(90,50)
    turtle.pd()
    turtle.forward(20)

    turtle.penup()
    turtle.setposition(-100,0)
    turtle.pd()
    turtle.circle(50,360)
    turtle.pu()
    turtle.setposition(-110,50)
    turtle.pd()
    turtle.forward(20)

    #for lines
    turtle.pu()
    turtle.setposition(-110,95)
    turtle.pd()
    turtle.left(90)
    turtle.circle(90,180)

    turtle.pu()
    turtle.setposition(-120,90)
    turtle.pd()
    turtle.right(180)
    turtle.circle(80,180)

    turtle.pu()
    turtle.setposition(-270,6)
    turtle.pd()
    turtle.circle(80,180)

    turtle.pu()
    turtle.setposition(-290,4)
    turtle.pd()
    turtle.right(180)
    turtle.circle(90,180)

    turtle.pu()
    turtle.setposition(-100,100)
    turtle.pd()
    turtle.circle(100,180)

    turtle.pu()
    turtle.setposition(-300,0)
    turtle.pd()
    turtle.circle(100,180)

    turtle.pu()
    turtle.setposition(290,95)
    turtle.pd()
    turtle.circle(90,180)

    turtle.pu()
    turtle.setposition(280,90)
    turtle.pd()
    turtle.right(180)
    turtle.circle(80,180)

    turtle.pu()
    turtle.setposition(110,4)
    turtle.pd()
    turtle.circle(90,180)

    turtle.pu()
    turtle.setposition(120,6)
    turtle.pd()
    turtle.right(180)
    turtle.circle(80,180)

    turtle.pu()
    turtle.setposition(100,0)
    turtle.pd()
    turtle.right(180)
    turtle.circle(100,180)

    turtle.pu()
    turtle.setposition(300,100)
    turtle.pd()
    turtle.circle(100,180)

    #for arrows
    turtle.pu()
    turtle.setposition(180,280)
    turtle.pd()
    turtle.right(45)
    turtle.forward(140)
    print(turtle.position())
    turtle.right(150)
    turtle.forward(50)
    turtle.setposition(81.01,181.01)
    turtle.left(300)
    turtle.forward(50)
    turtle.right(105)#pointing down

    turtle.pu()
    turtle.setposition(-180,280)
    turtle.pd()
    turtle.left(45)
    turtle.forward(140)
    print(turtle.position())
    turtle.left(150)
    turtle.forward(50)
    turtle.setposition(-81.01,181.01)
    turtle.right(300)
    turtle.forward(50)
    turtle.left(105)#pointing down

input()


    


    
 


    
    





    




    






    



