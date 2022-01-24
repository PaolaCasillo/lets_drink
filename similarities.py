import pandas as pd


def similarities(column, parameter):
    """
    This function returns similarities between the
    Drinks given as an input and
    the other Cocktails stored in our database.
    The code is structured in order to
    individuate similarities according to columns
    "Category" and "Alc-type".
    The user should select the column she/he
    is interested in.
    """
    db = pd.DataFrame(pd.read_csv('cocktails_data.csv'))

    column = str(column)
    parameter = str(parameter)
    result = db.loc[db[column] == parameter][["Drink"]]
    if column == ("Alcohol_type"):
        if len(result) > 1:
            print("The cocktails made with {} are: {} ".format(
                    parameter, result))
        else:
            print("Sorry, there are no cocktails with {} ".format(parameter))
    else:
        if len(result) > 1:
            print("In our Dataset we have the following {} : \n {}".format(
                    parameter, result))
        else:
            print("Sorry, there are not {} our Dataset ".format(parameter))
        
