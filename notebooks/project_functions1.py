#Sam's .py file
import pandas as pd
import numpy as np

def clean_df(rawFile):
    df = pd.read_csv(rawFile)
    data_clean = (df.copy()
                  .drop(['atmo_opacity','wind_speed', 'id', 'terrestrial_date'], axis=1)
                  .dropna(axis=0)
                  .rename(columns={'ls':'solar_longitude'})
                 )
    mNames = [(f"Month {x}") for x in range(1,13)]
    data_clean['month'].replace(mNames, list(range(1,13)), inplace=True)
    
    return data_clean