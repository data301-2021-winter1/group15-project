import pandas as pd
import numpy as np

def unprocessed(csv_file):
    df = pd.read_csv('../data/raw/mars-weather.csv')
    return df

def load_and_process(csv_file):
    df = pd.read_csv('../data/raw/mars-weather.csv')
    df1=(df.copy().drop(['atmo_opacity','wind_speed','id'], axis=1)
        .rename(columns={"terrestrial_date":"earth_date"})
        .dropna(axis=0))   
    conditions = [
        (df1['ls'] >= 0)&(df1['ls'] < 90),
        (df1['ls'] >= 90) & (df1['ls'] < 180),
        (df1['ls'] >= 180) & (df1['ls'] < 270),
        (df1['ls'] >= 270) & (df1['ls'] <=360)
        ]
    vals= ['Autumn','Winter','Spring','Summer']

    df1['Season'] = np.select(conditions, vals)
    return df1

