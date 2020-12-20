import pandas as pd
from .dataframe import BdsmDataFrame

class Abalones(BdsmDataFrame):
    """
        Abalones dataset as pandas dataframe
    """
    def __init__(self):
        data_file = self._load_file('abalones.csv')
        df = pd.read_csv(data_file)
        
        super(Abalones, self).__init__(df)
    
    def prepare(self):
        self['Sex'] = self['Sex'].astype('category')
        
        return self
