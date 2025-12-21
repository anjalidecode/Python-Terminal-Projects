print("Metric Conversion Tool")
print("1) Kilometers to Meters")
print("2) Meters to Centimeters")
print("3) Kilograms to Grams")
print("4) Celsius to Fahrenheit")
print("5) Fahrenheit to Celsius")

choice = input("Choose a conversion (1-5): ")

value = float(input("Enter the value: "))

if choice == "1":
    print(value, "km =", value * 1000, "meters")

elif choice == "2":
    print(value, "meters =", value * 100, "cm")

elif choice == "3":
    print(value, "kg =", value * 1000, "grams")

elif choice == "4":
    print(value, "°C =", (value * 9/5) + 32, "°F")

elif choice == "5":
    print(value, "°F =", (value - 32) * 5/9, "°C")

else:
    print("Invalid choice")
