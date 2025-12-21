distance = float(input("Enter travel distance in KM: "))

if distance <= 2:
    fare = 10
elif distance <= 5:
    fare = 20
elif distance <= 10:
    fare = 30
elif distance <= 15:
    fare = 35
elif distance <= 20:
    fare = 40
else:
    fare = 50  # Default extra for >20 km (simple version)

print("Ticket Price: ₹", fare)
