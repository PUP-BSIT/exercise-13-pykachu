import os # Import for clear screen on console

# Import menu functions from each member's module
from grouppackage.besa import besa_menu
from grouppackage.bualat import bualat_mainmenu
from grouppackage.maestre import maestre_mainmenu
from grouppackage.salespara import salespara_menu
from grouppackage.serquina import serquina_menu 

def main():
    # Main program loop
    while True:
        # Display main menu options
        os.system('cls')
        print("\nWelcome to the Group Package Program!")
        print("1. Besa Module")
        print("2. Bualat Module")
        print("3. Maestre Module")
        print("4. Salespara Module")
        print("5. Serquina Module")
        print("6. Exit")

        # Get user input for menu selection
        choice = int(input("\nSelect an option (1-6): "))

        # Handle user choice using match-case
        match choice:
            case 1:
                os.system('cls') # Clear the console for better readability
                besa_menu() # Call Besa's module
            case 2:
                os.system('cls')
                bualat_mainmenu() # Call Bualat's module
            case 3:
                os.system('cls')
                maestre_mainmenu() # Call Maestre's module
            case 4:
                os.system('cls')
                salespara_menu() # Call Salespara's module
            case 5:
                os.system('cls')
                serquina_menu() # Call Serquina's module
            case 6:
                print("Program Terminated.")
                break # Exit the loop and terminate program
            case _:
                # Handle invalid inputs
                print("Invalid choice. Please select a valid option (1-6).")

# Entry point for the program
if __name__ == "__main__":
    main()