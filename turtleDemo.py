'''
This program constructs a string and draws a figure using turtle
'''
__author__ = "Tejendra Khatri"
__date__ = "3/4/2017"

import turtle

def conststring(x):
    """This function constructs a string"""
    output = "FLGLG"
    for i in range(x):
        new_string= ""
        for eachChar in output:
            if eachChar == "F":
                new_string = new_string + "FLGRFRGLF"
            elif eachChar == "G":
                new_string = new_string + "GG"
            else:
                new_string = new_string + eachChar
            output= new_string
    return output

def turtle_run(X):
    wn = turtle.Screen()
    tejendra = turtle.Turtle()
    for eachChar in X:
        if eachChar == "F" or eachChar == "G":
            tejendra.forward(10)
        elif eachChar == "L":
            tejendra.left(120)
        elif eachChar== "R":
            tejendra.right(120)
    wn.exitonclick()
    
def main():
    X = int(input("How many generation of iterations would you prefer?"))
    Y = conststring(X)
    print(Y)
    drawing = turtle_run(Y)

if __name__ == "__main__":
    main()
sss
