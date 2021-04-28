import turtle as turtle
import random
import math

class Chaosgame():
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Chaos Game")
        self.t = turtle.Turtle()
        self.window.tracer(0,0)
        self.t.hideturtle()
        self.t.speed(0)
        self.t.up()
        self.V=[]

    def generate_vertices(self,sides,length):
        angle = 360 / sides
        self.V = []
        if sides % 2 == 1:
            phi = 90
            for i in range(sides):
                x = length*math.cos(phi*math.pi/180)
                y = length*math.sin(phi*math.pi/180)
                self.V.append((x, y))
                phi = phi + angle
        else:
            phi = angle/2
            for i in range(sides):
                x = length*math.cos(phi*math.pi/180)
                y = length*math.sin(phi*math.pi/180)
                self.V.append((x, y))
                phi = phi + angle

        return self.V
    
    def generate_polygon(self,sides):
        self.t.penup()
        self.t.goto(self.V[0])
        self.t.pendown()
        for i in range(sides):
            self.t.goto(self.V[i])
        self.t.goto(self.V[0])

    def generate_sierpinsky(self,sides,n,length):
        self.generate_vertices(sides,length)
        self.t = turtle.Turtle()
        self.t.up()
        self.t.hideturtle()
        p=self.V[0]
        print(p)
        if(sides==3):
            self.generate_polygon(sides)
            for i in range(n):
                self.t.goto(p)
                self.t.dot(2,'blue')
                r = random.randrange(len(self.V)) # pick a random vertex
                p = ((self.V[r][0]+p[0])/2,(self.V[r][1]+p[1])/2) # go to mid point between the random vertex and point   
                if i % 1000 == 0: # update for every 1000 moves
                    self.t = turtle.Turtle() # use new turtle
                    self.t.up()
                    self.t.hideturtle()
                    self.window.update()
        elif(sides==4):
            for i in range(n):
                self.t.goto(p)
                self.t.dot(3,'red')
                r = random.randrange(len(self.V)) # pick a random vertex
                if random.randint(0,1) == 0: # randomly decide to use edge or vertex
                    q = self.V[r] # vertex
                else:
                    q = ((self.V[r][0]+self.V[(r+1)%len(self.V)][0])/2,(self.V[r][1]+self.V[(r+1)%len(self.V)][1])/2) # go to mid point between two vertices  

                p = ((q[0]+p[0])/3,(q[1]+p[1])/3) # go 1/3 towards target 
                if i % 1000 == 0: # update for every 1000 moves
                    self.t = turtle.Turtle() # use new turtle
                    self.t.up()
                    self.t.hideturtle()
                    self.window.update()

sides=int(input("Enter no. of sides(Triangle or Square): "))
while True:
    if(sides==3 or sides==4):
        n=int(input("Enter no. of points: "))
        ini_length=int(input("Enter length(to calculate vertices): "))
        c=Chaosgame()
        c.generate_sierpinsky(sides,n,ini_length)
        break
    else:
        print("Invalid no. of sides")
        sides=int(input("Enter no. of sides(Triangle or Square): "))
        