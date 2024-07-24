def celsius_to_fahrenheit(celsius):
  """Converts temperature from Celsius to Fahrenheit.

  Args:
    celsius: Temperature in Celsius.

  Returns:
    Temperature in Fahrenheit.
  """

  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# Get Celsius temperature from user
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Print the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit")
