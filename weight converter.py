# project 3

weight = float(input("Enter weight: "))
unit = input("Kilograms or pounds? (K or L): ")

if unit == "K":
   weight = weight * 2.205
   unit = "lbs."
   print(f"Your weight is: {round(weight,2)} {unit}")
elif unit == "L":
   weight = weight / 2.205
   unit = "kgs."
   print(f"Your weight is: {round(weight,2)} {unit}")
else:
   print(f"{unit} not valid")




