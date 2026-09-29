def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f-32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def main():
    print("--- Temperature Converter ---")
    print("1.Celsius to fahrenheit")
    print("2.Fahrenheit to celsius")
    print("3.Celsius to kelvin")
    print("4.Kelvin to celsius")

choice = input("Choose an option (1-4): ")
if choice in ["1" , "2" , "3" , "4"]:
    try:
        temp = float(input("Enter the temperature: "))

        if choice == "1":
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {result:.2f}°F")
        elif choice == "2":
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F is equal to {result:.2f}°C")
        elif choice == "3":
            result = celsius_to_kelvin (temp)
            print(f"{temp}°C is equal to {result:.2f}K")
        elif choice == "4":
            result = kelvin_to_celsius(temp)
            print(f"{temp}K is equal to {result:.2f}°C")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
else:
    print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()


    


