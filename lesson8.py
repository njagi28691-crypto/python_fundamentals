#phone_number = input("Enter your phone number: ")

#name = input("Enter your full name: ")
# result = len(name)
#result = name.find("e")
#result = name.rfind("g")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit()
#result = phone_number.count("-")
#phone_number = phone_number.replace("-","")
#validate user input exercise
# 1.username is no more than 12 characters
# 2.username must nit contain spaces
# 3. username must not contain digits

username = input("Enter your username ")

if len(username) > 12:
    print("Username cant be more than 12 characters")
elif not username.isalpha() :
    print("Username cant contain digits")
elif not username.find(" ") == -1:
    print("Your username cant contain spaces")
else:
    print(f"Welcome {username}")



