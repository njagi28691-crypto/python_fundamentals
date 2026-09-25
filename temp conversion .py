# temp conversion programme
unit = input("Is the temp in Celsius of Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
  temp = round((9 * temp) / 5 + 32,1)
  print(f"The temperature is in Farenheit is: {temp} F")
elif unit =="F":
  temp = round((temp - 32) * 5 / 9,1)
  print(F"The temperature in Celsius is: {temp} C")
else:
    print(f"{unit} is invalid")
