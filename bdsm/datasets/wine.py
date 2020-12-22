import numpy as np
import pandas as pd
from .dataframe import BdsmDataFrame

class Wine(BdsmDataFrame):
    """
        Wine dataset as pandas dataframe
    """
    def __init__(self):
        data_file = self._load_file('wine.csv')
        df = pd.read_csv(data_file, sep = ';')
        
        super().__init__(df)
    
    def clean(self):
        df = self
        
        # column types
        df['color'] = df['color'].astype('category')
        
        return df
