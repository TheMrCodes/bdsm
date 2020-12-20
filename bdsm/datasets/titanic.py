import numpy as np
import pandas as pd
from .dataframe import BdsmDataFrame

class Titanic(BdsmDataFrame):
    """
        Abalones dataset as pandas dataframe
    """
    def __init__(self) -> pd.core.api.DataFrame:
        data_file = self._load_file('titanic.csv')
        df = pd.read_csv(data_file, sep = ';')
        
        super(Titanic, self).__init__(df)
    
    def clean(self) -> pd.core.api.DataFrame:
        df = self
        
        df['Age'] = np.where(df['Age'].isna(), df['Age'].mean(), df['Age'])
        df['Cabin'] = np.where(df['Cabin'].isna(), 'Unknown', df['Cabin'])
        df['Embarked'] = np.where(df['Embarked'].isna(), 'Unknown', df['Embarked'])
        
        df['Survived'] = df['Survived'].astype('category')
        df['Sex'] = df['Sex'].astype('category')
        df['Embarked'] = df['Embarked'].astype('category')
        
        return df
