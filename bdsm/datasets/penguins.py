import numpy as np
import pandas as pd
from .dataframe import BdsmDataFrame

class Penguins(BdsmDataFrame):
    """
        Penguins dataset as pandas dataframe
    """
    def __init__(self):
        data_file = self._load_file('penguins.csv')
        df = pd.read_csv(data_file)
        
        super().__init__(df)
    
    def clean(self):
        df = self
        
        # drop headers in data
        df = df[df['Comments'] != 'Comments']
        
        # NA: mean by species as float
        for col in ['CulmenLength', 'CulmenDepth', 'FlipperLength', 'BodyMass']:
            df[col] = df[col].astype('float')
            df[col] = df[col].fillna(df.groupby('Species')[col].transform('mean'))
        
        # NA: unknown
        df['Sex'] = np.where(df['Sex'].isna(), 'Unknown', df['Sex'].str.title())
        
        # unneeded columns
        df = df.drop(df.columns[[0, 1, 3, 5, 6, 7, 8, 14, 15, 16]], axis = 1)
        
        # column types
        df['Species'] = df['Species'].astype('category')
        df['Island'] = df['Island'].astype('category')
        df['Sex'] = df['Sex'].astype('category')
        
        return df
