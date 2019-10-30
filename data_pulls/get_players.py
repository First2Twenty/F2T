"""
This script pulls a data dump from the Fantasy.PremierLeague.com site, extracts
the id and first and last name of each football player, and outputs the data to
a CSV file.
"""
import numpy as np
import pandas as pd
import requests


# Pull data from Fantasy.PremierLeague.com
URL = 'https://fantasy.premierleague.com/api/bootstrap-static/'
RESPONSE = requests.get(URL)
ELEMENTS = RESPONSE.json()['elements']

# Extract player id and first and last name to a DataFrame
DF = pd.DataFrame(np.empty((len(ELEMENTS), 3)))
DF[:] = np.nan
DF.columns = ['id', 'first_name', 'last_name']

for i, item in enumerate(ELEMENTS):
    DF.iloc[i, 0] = str(item['id'])
    DF.iloc[i, 1] = str(item['first_name'])
    DF.iloc[i, 2] = str(item['second_name'])

DF.to_csv('data/player_data.csv', encoding='utf-8', index=False)
