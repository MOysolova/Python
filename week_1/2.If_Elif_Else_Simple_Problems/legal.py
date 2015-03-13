age = input("Enter your age: ")
age = int(age)
if age == 21:
    print("You are lucky :) You may enter.")
elif age < 21:
    print("You are too young... Come back when you get older.")
elif age > 21:
    print("You are legal, you may enter.")