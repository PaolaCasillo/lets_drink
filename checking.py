"""
This module focuses on checking if the input
given by the user is present in our database (csv file)
that contains information of cocktails.
It contains a functions where the user inputs the name of
the drink to know whether they are already
present in the "cocktails_data.csv file" respectively.
"""

import pandas as pd


class Check:

    def check_artist(self, artist):
        
        artist = artist.lower()
        db = pd.DataFrame(pd.read_csv('cocktails_data.csv'))
        artists = db["Drink"].str.lower()
        if artist in artists.values:
            return True
        return False
