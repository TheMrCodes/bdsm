import numpy as np
import pandas as pd
from .dataframe import BdsmDataFrame

class Titanic(BdsmDataFrame):
    """
        Titanic dataset as pandas dataframe
    """
    def __init__(self):
        data_file = self._load_file('titanic.csv')
        df = pd.read_csv(data_file, sep = ';')
        
        super().__init__(df)
    
    def clean(self):
        df = self
        
        # NA: unknown
        for col in ['Cabin', 'Embarked']:
            df[col] = np.where(df[col].isna(), 'Unknown', df[col])
        
        # NA: mean
        df['Age'] = np.where(df['Age'].isna(), df['Age'].mean(), df['Age'])
        
        # column types
        df['Survived'] = df['Survived'].astype('category')
        df['Sex'] = df['Sex'].astype('category')
        df['Embarked'] = df['Embarked'].astype('category')
        
        return df
