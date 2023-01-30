print("Hello, If you want to see my biography, please enter the password: ")


def info():
    print("Привет, я Кайратулы Темир, 2001 года рождения. Я из города Шымкент.")


while True:
    password = input("Enter the password: ")
    if password == "pass":
        info()
        passshow = input("You want leave ?:")
    elif passshow == "okay":
        break
    else:
        print("Password is not correct, Try again!")
