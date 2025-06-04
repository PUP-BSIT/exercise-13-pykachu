def maestre_mainmenu():
    while True:
        print("\nHello World! I am Michael Rua S. Maestre!")
        print("Please select an option to learn more about me:")
        print ("1. Basic Information")
        print ("2. Goals")
        print ("3. Motto")
        print ("4. Besa's Comment")
        print ("5. Serquina's Comment")
        print ("6. Bualat's Comment")
        print ("7. Salespara's Comment")
        print ("8. Exit\n")

        user_choice = int(input("Select an option (1-8): "))

        match user_choice:
            case 1:
                print("\Name: Michael Rua Solis Maestre")
                print("Program & Year: BSIT 2-1")
                print("Age: 20 years old")
                print("Birthday: November 22, 2004")
                print("Address: Block 78 Lot 18 Upper Bicutan Taguig City")
            case 2:
                print("\nMy goal in life:")
                print("I want to have a job that love and enjoy.")
                print("I want improve my skills in programming")
                print("I want to become a full servant of Jehovah God.")
            case 3:
                print("\nMy mottos in life:")
                print("For all things I have the strength through " 
                    "the one who gives me power.\n")
            case 4:
                print("\nBesa's Comment:")
                #TODO: add your comment here: Besa
            case 5:
                print("\nSerquina's Comment:")
                #TODO: add your comment here: Serquina
            case 6:
                print("\nBualat's Comment:")
                print("Michael you are very religious, "
                        "and I respect that.")
            case 7:
                print("\nSalespara's Comment:")
                #TODO: add your comment here: Salespara
            case 8:
                break
            case _:
                print("\nInvalid option, please try again")

 