# Show options to user
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

#  create variable to take input option from user
choice = input("Select a conversion option 1 OR 2: ")

# create temperature conversion program through conditional statment
if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    celsius_to_fahrenheit = ((celsius*(9/5))+32)
    print(celsius, "°C is equal to ",celsius_to_fahrenheit, "°F.")
    
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    fahrenheit_to_celsius = ((fahrenheit-32)*5/9)
    print(fahrenheit, "°F is equal to ",fahrenheit_to_celsius, "°C.")
    
else:
    print("Invalid choice. Please select 1 or 2.")

