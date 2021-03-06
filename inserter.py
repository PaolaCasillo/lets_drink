"""
The function of the inserter module
allows to append new drink into our database.
The function requires to add all the
other additional information, to generate
a list of 8 items.
Finally the list is inserted in a new
row becoming part
of our database.
"""

import csv
import pandas as pd
from checking import Check
from csv import writer


def add_element(drink, response=""):

    """
    This function comes into play once the user inputs a value
    that is not inside the database, or when, after
    the input, the user writes the optional argument -a.
    It uses the neme of the new drink precedently imputed,
    then it asks for the remaining values to insert in all the 8 columns
    of the database.
    """
    db = pd.DataFrame(pd.read_csv('cocktails_data.csv'))

    ingridients = input(
        "Now enter the ingridients of the drink->")
    while(ingridients == ""):
        ingridients = input(
            "You can't enter nothing..." + "please put anything ->")

    instruction = input("Now enter the intruction to do it -> ")
    while(instruction == ""):
        instruction = input("You can't enter nothing... " +

                                  "so please... put anything -> ")
    Alcohol_type = input(
        "Now enter the Alcohol_type -> ")
    while(Alcohol_type == ""):
        Alcohol_type = input(
            "You can't enter nothing..." + "please put anything ->")

    glass = input("Now enter the type of glass to use to serve it->")
    while(glass == ""):
        glass = input("You can't enter nothing..." + "please put anything ->")

    Basic_taste = input("Now enter the basic taste of the drink->")
    while(Basic_taste == ""):
        Basic_taste = input("You can't enter nothing..." + "please put anything ->")
                
    category = input(
        "Now enter the category of the drink->")
    while(category == ""):
        category = input(
            "You can't enter nothing..." + "please put anything ->")


    with open(r'cocktails_data.csv', 'a') as write_obj:
        writer = csv.writer(write_obj)
        row = len(db)
        write_obj.write("\n")
        writer.writerow([row, drink, glass, instruction, Basic_taste,
                                 category, ingridients, Alcohol_type])
        write_obj.close()
        return print("Thank you for your contribution!")


            



            
