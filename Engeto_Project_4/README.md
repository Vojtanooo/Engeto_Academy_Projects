Your task is to create the car rental database, which enables you to compare different cars based on various parameters. You will go through working with files and data type dictionary.

The database files are devided to two categories:

files that store information about one particular car - name of this file represents car's ID
2 files which stores IDs of rented / not rented cars
From this not_rented file you will construct a dictionary (or another data structure - depending what suits you the most) from which you will extract needed information later.

The program shall be user friendly and it's supposed to present availible cars to customer and let him rent a car. The program should:

greet the customer,
display simple menu and let the customer choose from those options,
show all availible cars,
search cars,
rent a car,
exit the program,

When searching cars, customer should be able to aply multiple conditions and he should be able to choose how to compare entered value and database value.

When renting cars, the program shall check if that car is availible, if yes then print some message and the move ID of that car form not_rented file to rented file.

edit: First use of modul Tkinter and make simple GUI.
