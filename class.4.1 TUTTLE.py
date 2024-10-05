import turtle #import library
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() #defined viarible
num_sides = 6 #viarible
side_lenght = 70
angle = 360.0/num_sides
#liturate loop for total number of side
for i in range(num_sides):
    polygon.forward(side_lenght)
    polygon.right(angle)

turtle.done()