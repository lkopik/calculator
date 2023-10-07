#this is a calculator
ferst_number = int(input("1 number: "))
opperation = input("operation: ")
two_numder = int(input("2 number: "))

x = ""

if opperation == "+":
    x = ferst_number + two_numder
if opperation == "-":
    x = ferst_number - two_numder
if opperation == "*":
    x = ferst_number * two_numder
if opperation == "**":
    x = ferst_number ** two_numder
if two_numder != 0:
    if opperation == "//":
        x = ferst_number // two_numder
    if opperation == "/":
        x = ferst_number / two_numder
else:
    print("aboba?")

print(x)