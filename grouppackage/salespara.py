def salespara():
    while True:
        print("Hello! I am Rica Genevive B. Salespara.\n")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Mottos")
        print("4. Comment from Besa")
        print("5. Comment from Bualat")
        print("6. Comment from Maestre")
        print("7. Comment from Serquina")
        print("8. Exit")

        user_choice = int(input("Select an option (1 -8): "))

        match user_choice:
            case 1:
                print("\nPersonal Information")
                print("Name: Rica Genevive B. Salespara")
                print("Age: 20")
                print("Birthday: September 22, 2004")
                print("Address: Lower Bicutan, Taguig City")
            case 2:
                print("\nGoals")
                print("1. To earn a degree in Information Technology.")
                print("2. To become a successful UI/UX designer.")
                print("3. To achieve financial independence by age 28.")
            case 3:
                print("\nMottos")
                print("1. The best way to predict the future is to create it.")
                print("2. Every setback is a setup for a comeback.")
                print("3. Never stop learning.")
            case 4:
                print("\nComment from Besa: ")
                # TODO : Add comment from Besa
            case 5:
                print("\nComment from Bualat: ")
                # TODO : Add comment from Bualat
            case 6:
                print("\nComment from Maestre: ")
                # TODO : Add comment from Maestre
            case 7:
                print("\nComment from Serquina: ")
                # TODO : Add comment from Serquina
            case 8:
                print("")
                break
            case _:
                print("Invalid option, please try again")