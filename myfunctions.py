'''
a collection of functions
'''
__author__ = "Tejendra Khatri"
__date__ = "21 March, 2017"


def square(x):
    """calculate the square of a number"""
    return power(x,2)

def mpg(prev, curr, gal):
    """calculate the miles per gallon between prev and curr"""
    miles = curr - prev
    mpg = miles / gal
    return mpg

def windChill(air_temp, wind_speed):
    """calculate the corresponding wind chill"""
    windchill=35.74+(0.6215*air_temp)-35.75*(wind_speed**0.16)+0.4275 * air_temp *(wind_speed**0.16)
    return windchill

def altitude(initial_altitude, time):
    """calculate the altitude at a certain time"""
    G=4
    return initial_altitude - G/2 * power(time,2)

def power(base, int_exponent):
    """calculate the base raised to the power exponent"""
    # initialize the value  of x and power .
    x = 0
    power = 1
    # test the value of loop control variable .
    while x  < int_exponent :
        # modify the value of power and x .
        power = base * power
        x += 1
    return power

def lucas(p):
    """calculate the nth value from the lucas sequence"""
    return 11

def sqrt(n):
    """calculate the square root of a number"""
    # initialize the value of approx and better 
    approx = 0.5 *n
    better = 0.5 *(approx + n/approx)
    # test the value in while loop 
    while better != approx:
        # modify the value of approx and better .
        approx = better
        better = 0.5 * (approx + n/approx)
    return approx

def isLucas(z):
    """determines whether the number is a Lucas number or not."""
    return True

def median(x,y,z):
    """calculate the median of the three numbers"""
    if x<y<z or z<y<x:
        return y
    elif y<x<z or z<x<y:
        return x
    else:
        return z
    




if __name__ == "__main__":
    import test
    print('square')
    test.testEqual(square(-10),100)
    test.testEqual(square(7),49)
    print('mpg')
    test.testEqual(mpg(49500,49800,10),30)
    test.testEqual(mpg(49800,50000,8),25)
    test.testWithin(mpg(50000,50100,3),33.33,2)
    print('windChill')
    test.testWithin(windChill(-40,60),-90.8735,2)
    test.testWithin(windChill(20,35),0.1281,2)
    print('altitude')
    test.testEqual(altitude(225,15),-225)
    test.testEqual(altitude(225,10),25)
    test.testEqual(altitude(225,8),97)
    print('power')
    test.testEqual(power(2,2),4)
    test.testEqual(power(-3,3),-27)
    test.testEqual(power(-4,4),256)
    test.testEqual(power(8,3),512)
    print('lucas')
    test.testEqual(lucas(4),7)
    test.testEqual(lucas(6),18)
    print('sqrt')
    test.testEqual(sqrt(64),8)
    test.testWithin(sqrt(66),8.1240,2)
    test.testEqual(sqrt(100),10)
    test.testWithin(sqrt(89),9.43398,2)
    print('isLucas')
    test.testEqual(isLucas(7),True)
    test.testEqual(isLucas(18),True)
    print('median')
    test.testEqual(median(13,6,-55),6)
    test.testEqual(median(27,28,26),27)
    test.testEqual(median(70,45,68),68)
    test.testEqual(median(6,6,-55),6)
    test.testEqual(median(27,28,17),27)
    test.testEqual(median(70,62,62),62)
    test.testEqual(median(5,5,5,),5)
