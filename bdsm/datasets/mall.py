import numpy as np
import pandas as pd
from .dataframe import BdsmDataFrame

class Mall(BdsmDataFrame):
    """
        Mall dataset as pandas dataframe
    """
    def __init__(self):
        data_file = self._load_file('mall.csv')
        df = pd.read_csv(data_file)
        
        super().__init__(df)
    
    def clean(self):
        df = self
        
        # column types
        df['Gender'] = df['Gender'].astype('category')
        
        return df
