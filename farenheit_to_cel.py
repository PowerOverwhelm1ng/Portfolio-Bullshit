def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def main():
    try:
        choice = input("Enter 'F' to convert Fahrenheit to Celsius, or 'C' to convert Celsius to Fahrenheit: ").upper()

        if choice == 'F':
            fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
            celsius_output = fahrenheit_to_celsius(fahrenheit_input)
            print(f"{fahrenheit_input:.2f} Fahrenheit is equal to {celsius_output:.2f} Celsius.")
        elif choice == 'C':
            celsius_input = float(input("Enter temperature in Celsius: "))
            fahrenheit_output = celsius_to_fahrenheit(celsius_input)
            print(f"{celsius_input:.2f} Celsius is equal to {fahrenheit_output:.2f} Fahrenheit.")
        else:
            print("Invalid choice. Please enter 'F' or 'C'.")

    except ValueError:
        print("Invalid input. Please enter a valid temperature.")

if __name__ == "__main__":
    main()


