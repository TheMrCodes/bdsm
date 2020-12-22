import numpy as np
import pandas as pd
from .dataframe import BdsmDataFrame

class Abalones(BdsmDataFrame):
    """
        Abalones dataset as pandas dataframe
    """
    def __init__(self):
        data_file = self._load_file('abalones.csv')
        df = pd.read_csv(data_file)
        
        super().__init__(df)
    
    def clean(self):
        df = self
        
        # column types
        df['Sex'] = df['Sex'].astype('category')
        
        return df
