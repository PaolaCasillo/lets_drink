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
            

def add_element(drink, response=""):

            
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

