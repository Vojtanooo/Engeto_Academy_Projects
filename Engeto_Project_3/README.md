The Assignment
Write a script that downloads election results of every municipality in every district into csv file.

At this page(https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ), you first have to choose the district by the X key in the column Výber obce (on the right). So for when you choose i.e. district Příbram you then have to choose the municipality. This time you choose by the number of the municipality (column číslo on the left). So, i.e. Dobříš will have the number 540111.

Input
The script expects two inputs:

1) Link where the list of the municipalities is located
2) name of the csv file without the suffix .csv

Output
The header of the csv file should have the following: municipality code, name of location, voters in the list, distributed voting envelopes, valid votes, candidate parties. Each row of the csv file will then represent individual municipalities.


# odkaz_1 = https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202
# odkaz_2 = https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302
