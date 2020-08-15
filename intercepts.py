# Calculator for calculating x and y intercepts
xaxis = int(input("Enter the x axis(excluding the variable): "))
yaxis =  int(input("Enter the y axis(excluding the variable): "))
equality = int(input("What is the equation equal to: "))

# example 3x + 4y = 6
# x - intercept can be found out by supposing y = 0
# 3x = 6
# x = 6/3
# x = 2

def x_intercept():
    xint = equality / xaxis  
    printansx = str(xint)
    print("x-intercept = " + printansx)

def y_intercept():
    yint = equality /yaxis
    printansy = str(yint)
    print("y-intercept = " + printansy)

x_intercept()
y_intercept()        