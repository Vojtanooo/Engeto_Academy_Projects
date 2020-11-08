ODDELOVAC = 26 * "="


def main():
    greeting()
    while True:
        menu()
        ch = choose()
        if ch == "1":
            option_1()
        elif ch == "2":
            print(ODDELOVAC)
            op_2 = option_2()
            find(op_2)
        elif ch == "3":
            print(ODDELOVAC)
            renting()
        elif ch == "4":
            print(f"{ODDELOVAC}\n"
                  f"Good bye. Nice to meet you :)")
            return False


def greeting():
    return print(f"Welcome to our rental database!\n"
                 f"How can i help you?\n"
                 f"{ODDELOVAC}")


def menu():
    return print(f"1) Show all availible cars."
                 f"\n2) Search for car.\n"
                 f"3) Rent a car.\n"
                 f"4) Exit program.\n"
                 f"{ODDELOVAC}")


def choose():
    choose = input("Choose number please: ")
    return choose


def option_1():
    for number in range(1,10):
        with open(f"/Users/VojtaJanecek/python-academy/"
                  f"Project_4_Engeto/files/{number}.txt", "r") as r:
            print(ODDELOVAC)
            print("|{0:^12}|".format("ID"), "{0:^10}|".format(f"{number}"))
            vys = r.readlines()
            for i in vys:
                splt = i.split("=")
                right = splt[1].rstrip("\n")
                left_strp = splt[0].lstrip(" ")
                print("|{0:^12}|".format(left_strp), "{0:^10}|".format(right))
            print(ODDELOVAC)


def option_2():
    
        print(f"You can search our database by:\n"
              f"1) Model year\n"
              f"2) Fuel (Gas/Diesel)\n"
              f"3) Transmission\n"
              f"4) Category\n"
              f"5) Price\n"
              f"{ODDELOVAC}")

        choose = input("Select number for choose please: ")
        if choose == "1":
            word = input("Enter model year you want: ")
            return word
        elif choose == "2":
            word = input("Enter what fuel you want (gas,diesel): ")
            return word
        elif choose == "3":
            word = input("Enter which transmisson you want "
                         "(automatic,manual): ")
            return word
        elif choose == "4":
            word = input("Enter Category (luxury,sedan,SUV,hatchback): ")
            return word
        elif choose == "5":
            word = input("Enter max price: ")
            for number in range(1, 10):
                with open(f"/Users/VojtaJanecek/python-academy/"
                          f"Project_4_Engeto/files/{number}.txt", "r") as r:
                    x = r.readlines()
                    y = x.pop()
                    y = y.split("=")
                    if int(word) >= int(y[1]):
                        print(ODDELOVAC)
                        print("|{0:^12}|".format("ID"),
                              "{0:^10}|".format(f"{number}"))
                        r.seek(0)
                        vys = r.readlines()
                        for i in vys:
                            splt = i.split("=")
                            right = splt[1].rstrip("\n")
                            left_strp = splt[0].lstrip(" ")
                            print("|{0:^12}|".format(left_strp),
                                  "{0:^10}|".format(right))
                        print(ODDELOVAC)
                    else:
                        pass
            return None


def find(word):
    if word is not None:
        for number in range(1, 10):
            with open(f"/Users/VojtaJanecek/python-academy/"
                      f"Project_4_Engeto/files/{number}.txt", "r") as r:
                if word in r.read():
                    print(ODDELOVAC)
                    print("|{0:^12}|".format("ID"),
                          "{0:^10}|".format(f"{number}"))
                    r.seek(0)
                    vys = r.readlines()
                    for i in vys:
                        splt = i.split("=")
                        right = splt[1].rstrip("\n")
                        left_strp = splt[0].lstrip(" ")
                        print("|{0:^12}|".format(left_strp),
                              "{0:^10}|".format(right))
                    print(ODDELOVAC)
                else:
                    pass


def renting():
    print(f"Which car you want to rent?\n"
          "Insert ID or go back to our database.")
    choose = input(f"Write 'ID' or 'back': ")
    if choose == "ID":
        id = input("Insert ID: ")
        with open("/Users/VojtaJanecek/python-academy/"
                  "Project_4_Engeto/files/not_rented.txt", "r") as read:
            if id in read.read():
                print("Car is available!")
                inpt = input("Do you really want to rent this car? (Y/N): ")
                if inpt == "Y":
                    with open("/Users/VojtaJanecek/python-academy/"
                              "Project_4_Engeto/files/rented.txt", "a+")\
                            as write:
                        write.write(f"{id}\n")
                        print(f"{ODDELOVAC}\nCar ID: {id} "
                              f"added to the rented cars database.\n"
                        f"{ODDELOVAC}")
                        read.seek(0)
                        lines = read.readlines()
                        with open(f"/Users/VojtaJanecek/python-academy/"
                                  f"Project_4_Engeto/files/"
                                  f"not_rented.txt", "w+") as output:
                            for line in lines:
                                if line.strip("\n") != id:
                                    output.write(line)
            else:
                print(f"{ODDELOVAC}\n"
                      f"Car is not available! Choose another please.\n"
                      f"{ODDELOVAC}")
    elif choose == "back":
        return print(f"Back to main menu...\n"
                     f"{ODDELOVAC}")


if __name__ == '__main__':
    main()