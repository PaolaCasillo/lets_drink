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
                   help="show similar artits by nat/mov/nop")
group.add_argument("-chr", "--characteristics", action="store_true",
                   help="entire characteristcs of a cocktail")
args = parser.parse_args()
answer = args.drink

check = Check()
