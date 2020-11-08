import tkinter as tk
import tkinter.font as font


def main_menu():
    frame = tk.Frame(root, bg="#476b6b")
    frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

    button_1 = tk.Button(frame, text="Show all available cars", bg="#c2d6d6",
                         fg="black", command=lambda: button_1_open(1))
    button_2 = tk.Button(frame, text="Search cars", bg="#c2d6d6", fg="black",
                         command=button_2_open)
    button_3 = tk.Button(frame, text="Rent car", bg="#c2d6d6", fg="black",
                         command=lambda:
                         button_3_open(f"Which car you want to rent?\n"
                             f"Insert ID or go back to our database."))
    button_4 = tk.Button(frame, text="Exit program", bg="#c2d6d6", fg="red",
                         command=root.quit)
    button_1.place(relx=0.05, rely=0.04, relwidth=0.90, relheight=0.20)
    button_2.place(relx=0.05, rely=0.28, relwidth=0.90, relheight=0.20)
    button_3.place(relx=0.05, rely=0.52, relwidth=0.90, relheight=0.20)
    button_4.place(relx=0.05, rely=0.76, relwidth=0.90, relheight=0.20)


def generate_dict():
    dct = {}
    for number in range(1,10):
        with open(f"/Users/VojtaJanecek/python-academy/"
                  f"Project_4_Engeto/files/{number}.txt", "r") as iput:
            dct[f"ID{number}"] = {}
            dct[f"ID{number}"]["ID"] = number
            for line in iput:
                (key, val) = line.split("=")
                dct[f"ID{number}"][key.strip(" ")] = val.strip("\n")
    return dct


def printing_by_id(dictionary, input_id):
    return dictionary[input_id]


def returned_dict_by_id(id):
    dict_by_id = "\n".join("{0:<12}      |{1:^18}".format(k, v)
        for k, v in printing_by_id(generate_dict(), f"ID{id}").items())
    return dict_by_id


def find_word(word):
    number_id = []
    for number in range(1, 10):
        with open(f"/Users/VojtaJanecek/python-academy/"
                  f"Project_4_Engeto/files/{number}.txt", "r") as r:
            if word in r.read():
                number_id.append(number)
    return number_id


def find_price(word):
    number_id = []
    for number in range(1, 10):
        with open(f"/Users/VojtaJanecek/python-academy/"
                  f"Project_4_Engeto/files/{number}.txt", "r") as r:
            x = r.readlines()
            y = x.pop().strip("\n").split("=")
            if int(y[1]) <= int(word):
                number_id.append(number)
    return number_id


def open_by_id(id):
    with open("/Users/VojtaJanecek/python-academy/"
              "Project_4_Engeto/files/not_rented.txt", "r") as read:
        if id in read.read():
            return f"Car is available!\n" \
                   f"Do you want to rent it?"
        else:
            return f"Sorry, Car isn't available.\n" \
                   f"Go back to our database\n" \
                   f"and choose another."


def click_yes(id):
    with open("/Users/VojtaJanecek/python-academy/"
              "Project_4_Engeto/files/not_rented.txt", "r") as read:
        read.read()
        with open("/Users/VojtaJanecek/python-academy/"
                  "Project_4_Engeto/files/rented.txt", "a+") as write:
            write.write(f"{id}\n")
            read.seek(0)
            lines = read.readlines()
            with open(f"/Users/VojtaJanecek/python-academy/"
                      f"Project_4_Engeto/files/not_rented.txt", "w+")\
                    as output:
                for line in lines:
                    if line.strip("\n") != id:
                        output.write(line)
                return "Car added to rented cars!"


def button_1_open(numb):

    font_size = font.Font(font=("Monaco", 19))
    frame = tk.Frame(root, bg="#476b6b")
    frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

    label = tk.Label(frame, text="Take a look to our showroom", bg="#c2d6d6")
    label.place(relx=0.05, rely=0.03, relwidth=0.90, relheight=0.07)

    label_text = tk.Label(frame, bg="#c2d6d6", text=returned_dict_by_id(numb),
                          font=font_size)
    label_text.place(relx=0.05, rely=0.13, relwidth=0.9, relheight=0.65)

    button_1 = tk.Button(frame, text="<<<<", bg="#c2d6d6", fg="black",
                         command=lambda: next_back_button(numb - 1))
    button_1.place(relx=0.05, rely=0.80, relwidth=0.44, relheight=0.07)
    button_2 = tk.Button(frame, text=">>>>", bg="#c2d6d6", fg="black",
                         command=lambda: next_back_button(numb + 1))
    button_2.place(relx=0.51, rely=0.80, relwidth=0.44, relheight=0.07)
    button_3 = tk.Button(frame, text="Back to Main menu", bg="#c2d6d6",
                         fg="black", command=main_menu)
    button_3.place(relx=0.05, rely=0.90, relwidth=0.90, relheight=0.07)


def button_2_open():
    frame = tk.Frame(root, bg="#476b6b")
    frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

    button_1 = tk.Button(frame, text="Model year", bg="#c2d6d6", fg="black",
                         command=lambda:
                         finding_window(0,
                                        "Write year you want:\n(exp.: 2015)"))
    button_2 = tk.Button(frame, text="Fuel", bg="#c2d6d6", fg="black",
                         command=lambda:
                         finding_window(0,
                                        "Write what fuel you want:"
                                        "\n(gas/diesel)"))
    button_3 = tk.Button(frame, text="Transmission", bg="#c2d6d6", fg="black",
                         command=lambda:
                         finding_window(0,
                                        "Write what transmission you want:"
                                        "\n(manual/automatic)"))
    button_4 = tk.Button(frame, text="Category", bg="#c2d6d6", fg="black",
                         command=lambda:
                         finding_window(0,
                                        "Write category you want:"
                                        "\n(exp.: SUV,luxury,hatchback)"))
    button_5 = tk.Button(frame, text="Price", bg="#c2d6d6", fg="black",
                         command=lambda:
                         finding_window_price(0,
                                              "Write your max price: "))
    button_6 = tk.Button(frame, text="Back to Main menu", bg="#c2d6d6",
                         fg="black", command=main_menu)

    button_1.place(relx=0.05, rely=0.03, relwidth=0.90, relheight=0.13)
    button_2.place(relx=0.05, rely=0.19, relwidth=0.90, relheight=0.13)
    button_3.place(relx=0.05, rely=0.35, relwidth=0.90, relheight=0.13)
    button_4.place(relx=0.05, rely=0.51, relwidth=0.90, relheight=0.13)
    button_5.place(relx=0.05, rely=0.67, relwidth=0.90, relheight=0.13)
    button_6.place(relx=0.05, rely=0.83, relwidth=0.90, relheight=0.13)


def button_3_open(func):
    frame = tk.Frame(root, bg="#476b6b")
    frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

    label = tk.Label(frame, bg="#c2d6d6")
    label.place(relx=0.05, rely=0.03, relwidth=0.90, relheight=0.07)
    label_entry = tk.Entry(label, bg="#c2d6d6", fg="black", textvariable=var)
    label_entry.place(relx=0.02, rely=0.10, relwidth=0.67, relheight=0.80)
    label_button = tk.Button(label, text="ENTER", bg="#c2d6d6", fg="black",
                             command=lambda:
                             button_3_open(open_by_id(var.get())))
    label_button.place(relx=0.70, rely=0.10, relwidth=0.28, relheight=0.80)

    font_size = font.Font(font=("Monaco", 19))
    label_text = tk.Label(frame, bg="#c2d6d6", text=func, font=font_size)
    label_text.place(relx=0.05, rely=0.13, relwidth=0.9, relheight=0.65)

    button_1 = tk.Button(frame, text="YES", bg="#c2d6d6", fg="black",
                         command=lambda: button_3_open(click_yes(var.get())))
    button_1.place(relx=0.05, rely=0.80, relwidth=0.44, relheight=0.07)
    button_2 = tk.Button(frame, text="NO", bg="#c2d6d6", fg="black",
                         command=lambda: button_3_open(
                             f"Which car you want to rent?\n"
                             f"Insert ID or go back to our database."))
    button_2.place(relx=0.51, rely=0.80, relwidth=0.44, relheight=0.07)
    button_3 = tk.Button(frame, text="Back", bg="#c2d6d6", fg="black",
                         command=main_menu)
    button_3.place(relx=0.05, rely=0.90, relwidth=0.90, relheight=0.07)


def finding_window(numb, func):

    frame = tk.Frame(root, bg="#476b6b")
    frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

    label = tk.Label(frame, bg="#c2d6d6")
    label.place(relx=0.05, rely=0.03, relwidth=0.90, relheight=0.07)
    label_entry = tk.Entry(label, bg="#c2d6d6", fg="black", textvariable=var)
    label_entry.place(relx=0.02, rely=0.10, relwidth=0.67, relheight=0.80)
    label_button = tk.Button(label, text="ENTER", bg="#c2d6d6", fg="black",
                             command=lambda:
                             finding_window(numb, returned_dict_by_id(
                                     find_word(var.get())[numb])
                                 ))
    label_button.place(relx=0.70, rely=0.10, relwidth=0.28, relheight=0.80)

    font_size = font.Font(font=("Monaco", 19))
    label_text = tk.Label(frame, bg="#c2d6d6", text=func, font=font_size)
    label_text.place(relx=0.05, rely=0.13, relwidth=0.9, relheight=0.65)

    button_1 = tk.Button(frame, text="<<<<", bg="#c2d6d6", fg="black",
                         command=lambda: finding_next_back_button(numb - 1)
                         )
    button_1.place(relx=0.05, rely=0.80, relwidth=0.44, relheight=0.07)
    button_2 = tk.Button(frame, text=">>>>", bg="#c2d6d6", fg="black",
                         command=lambda: finding_next_back_button(numb + 1)
                         )
    button_2.place(relx=0.51, rely=0.80, relwidth=0.44, relheight=0.07)
    button_3 = tk.Button(frame, text="Back", bg="#c2d6d6", fg="black",
                         command=button_2_open)
    button_3.place(relx=0.05, rely=0.90, relwidth=0.90, relheight=0.07)


def finding_window_price(numb, func):

    frame = tk.Frame(root, bg="#476b6b")
    frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

    label = tk.Label(frame, bg="#c2d6d6")
    label.place(relx=0.05, rely=0.03, relwidth=0.90, relheight=0.07)
    label_entry = tk.Entry(label, bg="#c2d6d6", fg="black", textvariable=var)
    label_entry.place(relx=0.02, rely=0.10, relwidth=0.67, relheight=0.80)
    label_button = tk.Button(label, text="ENTER", bg="#c2d6d6", fg="black",
                             command=lambda:
                             finding_window_price(numb, returned_dict_by_id(
                                     find_price(var.get())[numb])
                                 ))
    label_button.place(relx=0.70, rely=0.10, relwidth=0.28, relheight=0.80)

    font_size = font.Font(font=("Monaco", 19))
    label_text = tk.Label(frame, bg="#c2d6d6", text=func, font=font_size)
    label_text.place(relx=0.05, rely=0.13, relwidth=0.9, relheight=0.65)

    button_1 = tk.Button(frame, text="<<<<", bg="#c2d6d6", fg="black",
                         command=lambda:
                         finding_price_next_back_button(numb - 1)
                         )
    button_1.place(relx=0.05, rely=0.80, relwidth=0.44, relheight=0.07)
    button_2 = tk.Button(frame, text=">>>>", bg="#c2d6d6", fg="black",
                         command=lambda:
                         finding_price_next_back_button(numb + 1)
                         )
    button_2.place(relx=0.51, rely=0.80, relwidth=0.44, relheight=0.07)
    button_3 = tk.Button(frame, text="Back", bg="#c2d6d6", fg="black",
                         command=button_2_open)
    button_3.place(relx=0.05, rely=0.90, relwidth=0.90, relheight=0.07)


def finding_price_next_back_button(numb):
    if 0 <= numb < len(find_price(var.get())):
        return finding_window_price\
            (numb, returned_dict_by_id(find_price(var.get())[numb]))


def finding_next_back_button(numb):
    if 0 <= numb < len(find_word(var.get())):
        return finding_window\
            (numb, returned_dict_by_id(find_word(var.get())[numb]))


def next_back_button(numb):
    if 0 < numb < 10:
        return button_1_open(numb)


root = tk.Tk()
root.title("Car Database")
var = tk.StringVar()
canvas = tk.Canvas(root, height=510, width=510)
canvas.pack()
main_menu()
root.mainloop()
