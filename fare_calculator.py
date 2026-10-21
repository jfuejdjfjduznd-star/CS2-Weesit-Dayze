# Travel Fare Calculator
FARE_RATE = 14

# Validate passenger name: it must not be empty.
while True:
    name = input("Enter passenger name: ").strip()
    if name:
        break
    print("Invalid name. Passenger name cannot be empty. Please try again.")

# Validate distance: it must be a number greater than 0.
while True:
    distance_input = input("Enter distance (km): ").strip()
    try:
        distance = float(distance_input)
        if distance > 0:
            break
        print("Invalid distance. Enter a number greater than 0.")
    except ValueError:
        print("Invalid distance. Please enter a numeric value.")

# Validate passengers: it must be a positive whole number.
while True:
    passengers_input = input("Enter number of passengers: ").strip()
    if passengers_input.isdigit() and int(passengers_input) > 0:
        passengers = int(passengers_input)
        break
    print("Invalid number of passengers. Enter a positive whole number.")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
