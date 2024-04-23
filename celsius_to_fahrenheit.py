print("This program converts temperature from Celsius to Fahrenheit.\n\n")

temperature_in_celsius = input("Enter a tempersture value (in celsius): ")

temperature_in_fahrenheit = (float(temperature_in_celsius) * 9/5) + 32

print(f"{str(temperature_in_celsius)} degree Celsius converted to Fahrenheit will give {str(temperature_in_fahrenheit)}")