# Step 1: Get the temperature value and unit from the user
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (Celsius or Fahrenheit): ").lower()

# Step 2: Perform the temperature conversion
if unit == 'celsius':
    converted_temperature = (temperature * 9/5) + 32
    converted_unit = 'Fahrenheit'
elif unit == 'fahrenheit':
    converted_temperature = (temperature - 32) * 5/9
    converted_unit = 'Celsius'
else:
    print("Invalid unit. Please enter 'Celsius' or 'Fahrenheit'.")
    exit()  # Exit the program if the unit is not valid

# Step 3: Display the converted temperature
print(f"The converted temperature is {converted_temperature:.2f} {converted_unit}.")
