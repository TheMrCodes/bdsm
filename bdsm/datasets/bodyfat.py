import numpy as np
import pandas as pd
from .dataframe import BdsmDataFrame

class Bodyfat(BdsmDataFrame):
    """
        Bodyfat dataset as pandas dataframe
    """
    def __init__(self):
        data_file = self._load_file('bodyfat.csv')
        df = pd.read_csv(data_file)
        
        super().__init__(df)
    
    def clean(self, unit = 'imperial'):
        df = self
        
        # check unit argument for valid options
        unit = unit if unit in ('imperial', 'metric') else 'imperial'
        
        # drop Density
        df = df.drop(['Density'], axis = 1)
        
        # convert Weight and Height to metric
        if unit == 'metric':
            df['Weight'] = df['Weight'] * 0.45359237
            df['Height'] = df['Height'] / 0.39370
        
        return df
