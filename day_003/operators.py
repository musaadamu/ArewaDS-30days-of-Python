# 1. age declaration
age = 30

# 2. height as float variable
height = 17.5

# 3. a variable that stores a complex number
num_complex = 3 + 34j

# 4. base and height of triangle to calculate its area
b = int(input('Enter the base of the triangle: '))
h = int(input('Enter the height of the triangle: '))
area = 0.5 * b * h

# 5. Enter side a, side b and side c of a triangle
a = int(input('Enter side a of the triangle: '))
b = int(input('Enter side b of the triangle: '))
c = int(input('Enter side c of the triangle: '))
perimeter = a + b + c

# 6. Getting the width and length of a rectangle to calculate it area
length = int(input('Enter the length of the rectangle: '))
width = int(input('Enter the width of the rectangle: '))
area = length * width

# 7. Getting the radius of a circlce using prompt
r = int(input('Enter the radius of a circle'))
pi = 3.14
area = pi * r * r
circumference = 2 * pi * r
# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
a,b,p,q=map(int,input('Enter the coordinates of the points:').split())

slope2=m=(q-b)/(p-a)
y=b
x=a
c=y-(m*x)

#to find x-intercept.
y=0
x=(y-c)/m
print('x-intercept of the line:',x)

#to find y-intercept.
x=0
y=(m*x)+c
print('y-intercept of the line:',y)
# to find the slope


# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Import the math module to use the square root function.
import math
p1 = [2, 2]
p2 = [6, 10]
slope2 = (10-2)/6-2
# The formula computes the Euclidean distance in a 2D space.
distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

# 10. Compare the slopes in tasks 8 and 9.
m1 <= m2

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
y = x**2 + 6*2 + 9 
y = x**2 + 6*4 + 9 
y = x**2 + 6*8 + 9 
y = x**2 + 6*12 + 9 
y = x**2 + 6*-2 + 9 

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
p_length = 40
d_length = 30
if p_length<= d_length:
	print("True")
else:
	print("False")

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
if python == 1 and dragon == 1 :
    Print('The ariables are on')
else:
    print('The variables are of')

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
if (jargon): 
    pass
# 15. There is no 'on' in both dragon and python
if not(python == 1 and dragon == 1):
    pass
# 16. Find the length of the text python and convert the value to float and convert it to string
_python = len(python)
float_python = float(_python)
str_python = str(float_python)

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
if(n%2 == 0):
    print('The number is even')
else:
    print('The number is odd')
    
# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
if(7//3 == 2.7):
    print('The result equals to 2.7')
else:
    print('The value is not equal to 2.7')
    
# 19. Check if type of '10' is equal to type of 10
if(type(10) == type('10')):
    print('The numbers are the same')
else:
    print('The numbers are not the same')
    
# 20. Check if int('9.8') is equal to 10
if int('9.8'== 10):
    print('The numbers are the same')
else:
    print('The numbers are not the same')
    
# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
rs=input("Enter Hour:")
rate=input("Eenter Rate per Hour:")
pay=float(hrs)*float(rate)
print("Pay:", pay)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
y = float(input("How many years? "))

number_of_seconds_100 = y * 365 * 24 * 60 * 60
print(number_of_seconds_100, "Number of Seconds per 100 Years: ")

# 23. Write a Python script that displays the following table

[[i^j for j in range(1,4)] for i in range(6)]
