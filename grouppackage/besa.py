def besa_menu():
    while True: 

        print("\nGreetings! I am Vince Adrian Besa.\n")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Motto")
        print("4. Comment from Bualat")
        print("5. Comment from Maestre")
        print("6. Comment from Salespara")
        print("7. Comment from Serquina")
        print("8. Exit")

        choice = int(input("\nSelect an option (1-8): "))

        match choice:
            case 1:
                print("\nBasic Information:")
                print("Name: Vince Adrian Besa")
                print("Age: 20")
                print("Birthday: June 4, 2005")
                print("Address: Central Bicutan, Taguig City\n")

            case 2:
                print("\nGoals:")
                print("1. Become a software engineer")
                print("2. Make a positive impact in the tech industry")
                print("3. Continuously learn and grow in my field")
                print("4. Contribute to open-source projects\n")

            case 3:
                print("\nMotto:")
                print("'Everyday you wake up, be better.'\n") 

            case 4: 
                print("\nComment from Bualat:")
                # TODO: Add comment from Bualat

            case 5:
                print("\nComment from Maestre:")
                # TODO: Add comment from Maestre

            case 6:
                print("\nComment from Salespara:")
                # TODO: Add comment from Salespara

            case 7:
                print("\nComment from Serquina:")
                # TODO: Add comment from Serquina

            case 8: 
                print("Program Terminated.")
                break

            case _:
                print("Invalid choice. Please select a valid option (1-8).")