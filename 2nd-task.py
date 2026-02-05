name = set()

while True:
    user_input = input("Please enter your name(prezz enter to exit): ")
    if user_input == "":
        break
    elif user_input in name:
        print("existing name")

    else:
        print("new name")
        name.add(user_input)


print("List of names:")
for name in name:
    print(name)