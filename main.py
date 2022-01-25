"""
This is the main file where we created
the interaction between the user and the
database of drinks.
We used the argparse module to configure
all the positional and optional arguments.
Depending on the arguments given,
the program leads the user to a series of steps
to either check the presence of the cocktail imputed
inside the database and/or add it.
There is also the possibility to check out
the association between cocktails and alchol type.
"""

from inserter import add_element
from checking import Check
from similarities import similarities
from characteristics_function import return_chr
import argparse
import pandas as pd

db = pd.DataFrame(pd.read_csv('cocktails_data.csv'))
parser = argparse.ArgumentParser(description='This program will' +
                                             ' check if the Cocktail you put is' +
                                             ' inside our database of ' +                                             ' If the names have ' +
                                             'more than one space, ' +
                                             'wrap them ' +
                                             'around quotes ("").')
group = parser.add_mutually_exclusive_group()
parser.add_argument("drink",
                    help="input the name of a known cocktail")
group.add_argument("-a", "--add", action="store_true",
                   help="add a new cocktail")
group.add_argument("-d", "--database", action="store_true",
                   help="show cocktails and their ingridients")
group.add_argument("-p", "--alc_type", action="store_true",
                   help="show the list of Alcohool type")
group.add_argument("-drk", "--drinks", action="store_true",
                   help="show the list of cocktails")
group.add_argument("-s", "--similarities", action="store_true",
                   help="show similar drink alt / cat")
group.add_argument("-chr", "--characteristics", action="store_true",
                   help="entire characteristcs of a cocktail")
args = parser.parse_args()
answer = args.drink

check = Check()

if args.alc_type:
    print("Now you can see by yourself if a particular alcohol type " +
          "is present in our database!")
    print(db["Alcohol_type"])
elif args.drinks:
    print("Now you can see by yourself if the cocktail " +
          "is present in our database!")
    print(db["Drink"])

if args.similarities:
    response2 = input("Do you want to see the similarities according " +
                      "to cocktail category or Alcohol type " +
                      "of cocktails? (cat or alt) -> ")
    if response2 == "alt":
        similarities("Alcohol_type", db.loc[db['Drink'] == answer, 'Alcohol_type'].iloc[0])
    elif response2 == "cat":
        similarities("Category", db.loc[db['Drink'] == answer, 'Category'].iloc[0])


elif args.characteristics:
    return_chr(answer)

elif args.database:
    print("Now you can see by yourself which cocktails " +
          "you can do with your availale ingridients")
    print(db["Drink"] + " : " + db["Ingridients"])
else:
    if args.add:
        add_element(answer)
    elif check.check_drink(answer):
        print("In order to do " + db["Drink"].loc[db["Drink"].str.lower() == answer.lower()]
              .values[0] + " you need: "+
              db["Ingridients"].loc[db["Drink"].str.lower() ==
              answer.lower()].values[0] + "\nInstruction: " +
              db["Instruction"].loc[db["Drink"].str.lower() ==
              answer.lower()].values[0])
    else:
        response = input(answer + " is not present in our database. Are you " +
                         "sure that you wrote it correctly " +
                         "(use -d to check if it is " +
                         "already in our database)?(y or n) -> ")
        if response == "y":
            response1 = input(
                "Great! Do you want to add it? (y or n) -> ")
            if response1 == "y":
                add_element(answer)
            else:
                print("Thank you anyway")
        else:
            print("Use -d to check if it is already in our database, " +
                  "maybe there is a spelling error in the input. " +
                  "Then try again, thank you for your patiance!")
