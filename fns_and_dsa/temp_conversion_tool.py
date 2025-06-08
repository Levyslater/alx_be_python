"""
This script will define functions to convert temperatures between Celsius and Fahrenheit
"""
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def main():
    def convert_to_celsius(fahrenheit):
        return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32) 
    def convert_to_fahrenheit(celsius):
        return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32  
    try:
        value_to_convert = int(input("Enter the temperature to convert: "))
    except ValueError:
        print("Please enter an integer for temperature")
    else:
        operation = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if operation == "C":
            print(f"{value_to_convert}\u00B0C is {convert_to_fahrenheit(value_to_convert)}\u00B0F")
        elif operation == "F":
            print(f"{value_to_convert}\u00B0F is {convert_to_celsius(value_to_convert)}\u00B0C")
        else:
            print("Please select 'C' for celsius or 'F' for fahrenheit")

if __name__ == "__main__":
    main()