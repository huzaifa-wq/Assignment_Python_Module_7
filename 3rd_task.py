airport_database = {}

while True:
    print("Press 1 to add airport details :")
    print("Press 2 to see airport details :")
    print("Press 3 to exit")

    user_input = input(":")
    if user_input == "1":
        airport_name = input("Enter airport name: ")
        ICOA_code = input("Enter ICOA code: ")
        airport_database[ICOA_code] = airport_name
        print("airport added")
    elif user_input == "2":

        ICOA_code = input("Enter ICOA code: ")
        print(f"Name of the Airport is {airport_database[ICOA_code]}")
    elif user_input == "3":
        break






