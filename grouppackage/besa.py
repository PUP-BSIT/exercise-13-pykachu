import os # Import for clear screen on console

def besa_menu():
    # Besa's program loop
    while True: 
        os.system('cls')  # Clear the console for better readability
        # Display the menu options
        print("\nGreetings! I am Vince Adrian Besa.\n")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Motto")
        print("4. Comment from Bualat")
        print("5. Comment from Maestre")
        print("6. Comment from Salespara")
        print("7. Comment from Serquina")
        print("8. Exit")

        # Get user input for menu selection
        choice = int(input("\nSelect an option (1-8): "))

        # Handle user choice using match-case
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
                print("Vince is a great team player and always " 
                    "brings positive energy to the group.")
            case 5:
                print("\nComment from Maestre:")
                print("Vince is a dedicated and hardworking individual.")
            case 6:
                print("\nComment from Salespara:")
                print("Best of luck in reaching your goals, Vince!")
            case 7:
                print("\nComment from Serquina:")
                print("\nVince is a reliable team member.")
            case 8: 
                print("\nProgram Terminated.")
                break # Exit the loop and terminate program
            case _:
                # Handle invalid inputs
                print("\nInvalid choice. Please select a valid option (1-8).")

        # Wait for user input before clearing the screen
        input("\nPress 'Enter' to continue...")