print("Choose a shape:")
print("1) Square")
print("2) Rectangle")
print("3) Triangle")
print("4) Circle")

choice = input("Enter option (1-4): ")

if choice == "1":
    side = float(input("Enter side: "))
    print("Area =", side * side)

elif choice == "2":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area =", length * width)

elif choice == "3":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area =", 0.5 * base * height)

elif choice == "4":
    radius = float(input("Enter radius: "))
    print("Area =", 3.14 * radius * radius)

else:
    print("Invalid choice")
