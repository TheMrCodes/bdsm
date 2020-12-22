import numpy as np
import pandas as pd
from .dataframe import BdsmDataFrame

class Iris(BdsmDataFrame):
    """
        Iris dataset as pandas dataframe
    """
    def __init__(self):
        data_file = self._load_file('iris.csv')
        df = pd.read_csv(data_file)
        
        super().__init__(df)
    
    def clean(self):
        df = self
        
        # column types
        df['Class'] = df['Class'].astype('category')
        
        return df
