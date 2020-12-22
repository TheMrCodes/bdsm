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
