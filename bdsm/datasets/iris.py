import pandas as pd
from .dataframe import BdsmDataFrame

class Iris(BdsmDataFrame):
    """
        Abalones dataset as pandas dataframe
    """
    def __init__(self) -> pd.core.api.DataFrame:
        data_file = self._load_file('iris.csv')
        df = pd.read_csv(data_file)
        
        super(Iris, self).__init__(df)
    
    def clean(self) -> pd.core.api.DataFrame:
        df = self
        df['Class'] = df['Class'].astype('category')
        
        return df
