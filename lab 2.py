## Problem 1: Course Marks

marks = [75, 82, 68, 91, 45]

print("Total:", sum(marks))
print("Average:", sum(marks)/len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))

passed = 0

for mark in marks:
    if mark >= 50:
        passed += 1

print("Passed Courses:", passed)

## Problem 2: Weekend Temperatures

temperatures = (30, 32, 31, 29, 35, 33)

print("Temperatures:")

for temp in temperatures:
    print(temp)

print("Highest Temperature:", max(temperatures))
print("Lowest Temperature:", min(temperatures))

## Problem 3: Word Analyzer

text = input("Enter a word or sentence: ")

characters = len(text)
vowels = 0
spaces = 0

for ch in text:

    if ch.lower() in "aeiou":
        vowels += 1

    if ch == " ":
        spaces += 1


print("Characters:", characters)
print("Vowels:", vowels)
print("Spaces:", spaces)

## Problem 4: Grade Calculator Function

def calculate_grade(marks):

    average = sum(marks) / len(marks)

    if average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


marks = [80, 75, 90, 85, 70]

print("Grade:", calculate_grade(marks))

## Problem 5: Shopping Cart Processor

products = [
    {"name":"Notebook", "price":120, "quantity":3},
    {"name":"Pen", "price":20, "quantity":5},
    {"name":"USB Drive", "price":850, "quantity":2},
    {"name":"Mouse", "price":650, "quantity":1}
]


total = 0

for product in products:

    cost = product["price"] * product["quantity"]
    total += cost


def apply_discount(total):

    if total >= 2000:
        return total * 0.90

    else:
        return total


print("Total Cost:", total)
print("After Discount:", apply_discount(total))

## Problem 6: Countdown using while loop

number = int(input("Enter a non-negative integer: "))

while number >= 0:

    print(number)
    number = number - 1

 ## Problem 7: Student Record Analyzer  

  students = [
    {"name":"Rahim","department":"CSE","marks":85,"attendance":92},
    {"name":"Karim","department":"CSE","marks":48,"attendance":76},
    {"name":"Sara","department":"DS","marks":91,"attendance":95},
    {"name":"Nadia","department":"DS","marks":67,"attendance":84},
    {"name":"Hasan","department":"CSE","marks":73,"attendance":78}
]


total = 0
passed = 0
highest_student = students[0]


for student in students:

    print(student["name"], student["marks"])

    total += student["marks"]

    if student["marks"] >= 50:
        passed += 1

    if student["marks"] > highest_student["marks"]:
        highest_student = student


print("Passed Students:", passed)
print("Class Average:", total/len(students))
print("Highest Mark Student:", highest_student["name"])

## Problem 8: Product Inventory Summary

products = [
    {"name":"Notebook","price":120,"quantity":3},
    {"name":"Pen","price":20,"quantity":5},
    {"name":"USB Drive","price":850,"quantity":2},
    {"name":"Mouse","price":650,"quantity":1}
]


total_inventory = 0
highest_product = ""
highest_value = 0


for product in products:

    line_total = product["price"] * product["quantity"]

    print(product["name"], "=", line_total)

    total_inventory += line_total


    if line_total > highest_value:

        highest_value = line_total
        highest_product = product["name"]



print("Total Inventory Value:", total_inventory)
print("Highest Value Product:", highest_product)