import pandas as pd
import numpy as np

def unprocessed (csvfile):
    data= pd.read_csv("../data/raw/mars-weather.csv")
    return data
def load_and_processed (f):
    cleaned_rmd= (   
    pd.read_csv(f)
    .copy().drop(['wind_speed','id','atmo_opacity','month'], axis=1)
    .rename(columns={"terrestrial_date":"date"})
    .reindex(["date", "min_temp", "max_temp", "pressure", "ls", "sol"],axis=1))
        
    

    return cleaned_rmd
