"""
The function of the characteristcs module
is to explain in a more detailed way the characteristics,
like the category, ingridiets, taste, instruction and
glass to be serve with, of the cocktails
that can be found into our database.
The function first checks if the input
the user inserted is present in
the database, if not the system will warn the user
and invite him to check if it is correctly written.
"""

import csv
import pandas as pd



def return_chr(drink):

    db = pd.DataFrame(pd.read_csv('cocktails_data.csv'))
    drinks = list(db["Drink"])
    """
    This function comes into play once the user inputs a value
    and wants to obtain as output the complete list of information that
    can be found inside the database, or when, after
    the input, the user writes the optional argument -chr.
    It recognizes the input if it is a name of a drink inside the dataset.
    """
    if drink in drinks:
        print("to do the ",db["Drink"].loc[
            db["Drink"].str.lower() == drink.lower()].values[0]," that is a ",
            db["Category"].loc[db["Drink"].str.lower() == drink.lower()].values[0],
            ", you need ", db["Ingridients"].loc[db["Drink"].str.lower() == drink.lower()].values[0],
            " and", db["Instruction"].loc[db["Drink"].str.lower() == drink.lower()].values[0],
            " . Finally serve in "  ,db["Glass"].loc[db["Drink"].str.lower() == drink.lower()].values[0])
    else:
         print(drink, " seems not to be present in our database." +
               "Are you sure that you wrote" +
               " the name of the cocktail correctly?" +
               " Use -d to check if it is already in our database," +
               "maybe there is a spelling error in the input." +
               " Check it and then try again, if it is not present," +
               "use -a to insert the new drink," +
               " thank you for your patience!")

