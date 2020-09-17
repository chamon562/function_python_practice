def f():
    # the word pass tells python to skip this line and do nothing
    # in pythone you group code by indentation
    pass

# to call the function type the name and parenthesis f()
f()
# the function f will do nothing just like how we told it to
# f

# this function will take in no argument and will return an object
def ping():
    # to return a value type return then the object
    return "Ping!"
    # this function will return the string Ping!
    # return values are optional
ping()

# can store the return value to a variable 
x = ping()
# to see the value print(x)
print(x)
# call the function dir() and printing it will show function ping and the variable listed
print(dir())
# this is the output from print(dir())
# ['__annotations__', '__builtins__', '__cached__', 
# '__doc__', '__file__', '__loader__', '__name__', 
# '__package__', '__spec__', 'f', 'ping', 'x']

# importing math module needed to find the volume of a sphere 
import math
# if you display the dir of the math module you will see pi listed
# print out print(dir(math)) you will see pi listed and all of its 
# print(dir(math))
# ['__doc__', '__file__', '__loader__', '__name__',
#  '__package__', '__spec__', 'acos', 'acosh', 'asin',
#   'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb',
#    'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e',
#     'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial',
#      'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd',
#       'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
#        'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10',
#         'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow',
#          'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt',
#           'tan', 'tanh', 'tau', 'trunc']
# can now access the number pi
# this is for terminal
# math.pi
# print(math.pi) console out put is 3.141592653589793

# define the volume function
# this function will have a single argument the radius r
def volume(r):
    # Returns the volume of a sphere with radius r
    # next we compute the volume 
    # made volume the variable and called v and made that = the equation of the sphere
    v = (4.0/3) * math.pi * r**3
    # use decimals for the fraction 4/3 because in python2 if you devide one integer to another
    # it returns the quotient not the exact value
    # double asterisk for exponents r**3 
    # now return the volume
    # to return a value type return then the object v is the object which has the eqation inside of it
    return v
# lets test this function
# compute the volume of the sphere with the radus of 2
print(volume(2)) #output is 33.510321638291124

# made up a variable to take the users input which is w used to be r gonna change it to radius to see where it goes clearer
radius = int(input('enter a radius number to get volume of sphere:'))
# instead of typing in the number in the method volume(2) we will give the user interaction by using the input setting that to the variable radius
print('volume is {}'.format(volume(radius)))
# above we want to print the string 'volume is {} <- this is the interpoloation that will hold the out put of (volume(radius)) and use .format to work that into the {}
# print(help(volume))

def area_of_triangle(b, h):
    area = (0.5) * b * h
    return area


# putting in your arguments for b and h which is 2 and 4 to get thrown the area toget computed
print(area_of_triangle(2, 4))
# area = (0.5) * (2) * (4)
# 2*4 = 8 and 8 divided by .5 or 1/2 is 4.0
b = int(input("enter the base:"))
h = int(input("enter the height:"))

print('{} is the area of your triangle'.format(area_of_triangle(b,h)))

# python can take on another kind of argument called keyowrd arguments 
# example of keyword arguments is cm(feet=0, inches=0)
# assigning a default value of 0 to each argument 
# for this reason python call these default arguments 
def cm(feet=0, inches=0):
    # doc string describing the function 
    # Converts a length from feet and inches to centimeters

    # first convert inches to centimeters
    inches_to_cm = inches * 2.54
    # convert feet to centimeters
    # feet is the the default value 12 would be the inches and times that by 2.54 to get the total to centimeters
    feet_to_cm = feet * 12 * 2.54
    # when returning must combine the two dont know why yet...
    return inches_to_cm + feet_to_cm

# heres how you call a function with keyword arguments
cm(feet = 5)
cm(inches = 70)
cm(feet = 5, inches = 8)
# we can perform this calculation with inches first
print(cm(inches = 8, feet = 5))

# def add(x = 0, y):
# 	return x+y
# You’ll get a syntax error because the keyword argument has to be last in the argument

# Python will call these default arguments

# To fix this you must list the non default argument first 
# Aka required arguments

# To call this argument must pass in the required argument for y

def add(y, x=0):
	return x+y
add(5)
