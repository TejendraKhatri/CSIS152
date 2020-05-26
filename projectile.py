"""
In the program we determine the projectile of the turtle for different values of T using the formula:
X = Xo + V * T and
Y = Yo -G/2 * T ** 2

TABLE:
    Xo       Yo     G     V     T      X=Xo+V*T    Y=Yo-G/2*T**2
   -300     225     4     20    1       -280         223
   -300     225     4     20    5       -200         175
   -300     225     4     20    10      -100          25
   -300     225     4     20    13       -40        -113
   -300     225     4     40    15       300        -225
"""
__author__ = "Tejendra Khatri"
__date__ = "Feb 22,2017"
                 
import turtle                     #importing the turtle module
import myfunctions

def main():
    wn = turtle.Screen()          #creation of screen
    tejendra = turtle.Turtle()    #creation of turtle
    V = 40                        #horizontal velocity of the turtle in units per second
    G = 4                         #acceleration due to gravity (units per second squared)
    Xo = -300                     #X-coordinate of initial position
    Yo = 225                      #y-coordinate of initial position
    tejendra.shape("turtle")      #assigning shape to the turtle
    tejendra.up()                 #picking up the turtle's tail
    tejendra.goto(Xo,Yo)          #placing the turtle at the initial position
    tejendra.down()               #putting the turtle's tail down
    tejendra.stamp()              #leaving an impression of the turtle
    print("X-Coordinate = ", Xo,"Y-Cordinate = ", Yo)
    for T in range(1,16):         #creating a loop for time 1 to 15 seconds inclusive
        X = Xo + V * T
        Y = myfunctions.altitude(Yo,T)
        tejendra.goto(X,Y)
        tejendra.stamp()
        print("X-Coordinate = ",X,"Y-Coordinate = ",Y)

    tejendra.color("green")      #assigning a color to the turtle
    tejendra.stamp()
    wn.exitonclick()
    

if __name__ == "__main__":
    main()
