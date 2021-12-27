"""
# Create 3 variables : 1) string of your full name
                     2) string of your mail
                     3) int of your age

# print all of them to the screen
# than print your name from the end to beginning and print it only with your age*3
# then check if your name is stored inside this full string: "idan ben dudu yuval shimon yael gal adam shahar yana"
"""

full_name = "Baruch Bazak"
mail = "FakeMail@gmail.com"
age = 26

print(f"My full name is : {full_name}\nMy mail is : {mail}\nMy age is : {age}")
print("Name from the end to beginning :", full_name[::-1], "\nage*3 :", str(age * 3))

names_string = "idan ben dudu yuval shimon yael gal adam shahar yana"

print("My name is stored inside names_string :", "Baruch" in "idan ben dudu yuval shimon yael gal adam shahar yana")
