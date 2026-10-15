## Problem 1: Sum, Difference, Product and Quotient
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)

## Problem 2: Student Profile

name = input("Enter student name: ")
student_id = input("Enter student ID: ")
age = int(input("Enter age: "))
department = input("Enter department: ")
cgpa = float(input("Enter CGPA: "))

print("\nStudent Profile")
print("Name:", name)
print("ID:", student_id)
print("Age:", age)
print("Department:", department)
print("CGPA:", cgpa)

## Problem 3: Celsius to Fahrenheit and Kelvin

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)

## Problem 4: Student Marks Analysis

marks = []

for i in range(5):
    mark = int(input("Enter course mark: "))
    marks.append(mark)

total = sum(marks)
average = total / 5
highest = max(marks)
lowest = min(marks)

passed = 0

for mark in marks:
    if mark >= 50:
        passed += 1

print("Total:", total)
print("Average:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Number of Passed Courses:", passed)

