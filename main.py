from grouppackage.besa import besa_menu
from grouppackage.bualat import bualat_mainmenu
from grouppackage.maestre import maestre_mainmenu
from grouppackage.salespara import salespara
from grouppackage.serquina import serquina_menu 

def main():
    while True:
        print("\nWelcome to the Group Package Program!")
        print("1. Besa Module")
        print("2. Bualat Module")
        print("3. Maestre Module")
        print("4. Salespara Module")
        print("5. Serquina Module")
        print("6. Exit")

        choice = int(input("\nSelect an option (1-6): "))

        match choice:
            case 1:
                besa_menu()
            case 2:
                bualat_mainmenu()
            case 3:
                maestre_mainmenu()
            case 4:
                salespara()
            case 5:
                serquina_menu()
            case 6:
                print("Program Terminated.")
                break
            case _:
                print("Invalid choice. Please select a valid option (1-6).")

if __name__ == "__main__":
    main()