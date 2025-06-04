import os # Import for clear screen on console

def bualat_mainmenu():
    # Bualat's program loop
    while True:
        os.system('cls')  # Clear the console for better readability
        # Display the menu options
        print("\nWelcome to Bualat's menu!")
        print("Please select an option to learn more about me:")
        print ("1. Basic Information")
        print ("2. Goals")
        print ("3. Motto")
        print ("4. Comment from Besa")
        print ("5. Comment from Serquina")
        print ("6. Comment from Maestre")
        print ("7. Comment from Salespara")
        print ("8. Exit")

        # Get user input for menu selection
        user_choice = int(input("Select an option (1-8): "))

        # Handle user choice using match-case
        match user_choice:
            case 1:
                print("\nI am Bench Brian Bualat, "
                    "a member of the team, PyKachu.")
                print("I am 20 years old.")
                print("I am from the Philippines.")
                print("I have been single in my entire life.")
            case 2:
                print("\nMy goal in life:")
                print("I want to be rich and happy.")
            case 3:
                print("\nMy mottos in life:")
                print("Be kind to everyone, even if they are not kind to you.")
                print("Kindness is a strength, not a weakness.")
                print("Kindness is free, sprinkle that stuff everywhere.")
                print("Being kind doesn't cost anything.")
            case 4:
                print("\nBesa's Comment:")
                print("Bench is a great team player, "
                    "always ready to help others.")
            case 5:
                print("\nSerquina's Comment:")
                print("\nBench always puts in the effort to help the team.")
            case 6:
                print("\nMaestre's Comment:")
                print("Bench is a very kind person")
            case 7:
                print("\nSalespara's Comment:")
                print("Best of luck in reaching your goals, Bench!")
            case 8:
                break # Exit the loop and terminate program
            case _:
                # Handle invalid inputs
                print("\nInvalid option, please try again")

        # Wait for user input before clearing the screen
        input("\nPress 'Enter' to continue...")