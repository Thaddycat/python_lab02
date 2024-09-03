from math import pi

#Part 1 Variables and Assignments
name = "Thaddeus"
age = 29
height = 5.75
favorite_color = "Purple"

#print each variable one at a time
print(name)
print(age)
print(height)
print(favorite_color)

#print all variables in a single print statement
print(name,age,height,favorite_color)

#print in variables in a more structured fashion
print(f"Hi, I am {name}, I am {age:d} years old, I am {height:.1f} feet tall, and my favorite color is {favorite_color}")
print(f"Name: {name:10} | Age: {age:3d} | Height: {height:5.1f}")

#print with format specifiers within a multi-line string
print(f"""
Name: {name}
      Age: {age:^12}
      Height: {height:^8.1f}
Favorite Color: {favorite_color:^5}""")

#Create a new variable
radius = 5
circle_area = pi * radius ** 2
print(f"The area of a circle with a radius of {radius} is {circle_area:.1f}")

#Part 2 Statements and Modules
#Import the math module
import math

#Calculate the square root
print(f"The square root of my age({age}) is {math.sqrt(age):.2f}")

#Calculate the Sine and Cosine
print(f"The sine of my height({height}) is {math.sin(height):.2f} and the cosine of my height({height}) is {math.cos(height):.2f}")

#Part 3: Expressions and Operators
#Arithmetic operators, calculate the following:

#The sum of age and 5
print(f"My age plus five is {age + 5} years")

#The difference between height and 4
print(f"My height minus four is {height - 4} feet")

#The product of age and height
print(f"My age multiplied by my height is {age * height}")

#The quotient of height and 2
print(f"My height divided by 2 is {height / 2:.2f}")

#The remainder of age divided by 3
print(f"The remainder left over after dividing my age by 3 is {age % 3}")

#Age raised to the power of 2
print(f"My age squared would be {age ** 2}")

#Part 4: Temperature Conversion
#Create a temperature conversion program
temp_far = input("Input temperature in Fahrenheit: ")
degree_sign = u'\N{DEGREE SIGN}'
print(f"{temp_far}{degree_sign} Fahrenheit is {(int(temp_far) - 32) * (5 / 9):.2f}{degree_sign} Celsius.")

