num = int(input("Enter a number (1-100): "))

roman = ""

if num >= 100:
    roman += "C"
    num -= 100

if num >= 90:
    roman += "XC"
    num -= 90

if num >= 50:
    roman += "L"
    num -= 50

if num >= 40:
    roman += "XL"
    num -= 40

while num >= 10:
    roman += "X"
    num -= 10

if num == 9:
    roman += "IX"
    num -= 9

if num >= 5:
    roman += "V"
    num -= 5

if num == 4:
    roman += "IV"
    num -= 4

while num >= 1:
    roman += "I"
    num -= 1

print("Roman numeral:", roman)
