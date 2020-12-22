import numpy as np
import pandas as pd
from .dataframe import BdsmDataFrame

class Students(BdsmDataFrame):
    """
        Students dataset as pandas dataframe
    """
    def __init__(self):
        data_file = self._load_file('students.csv')
        df = pd.read_csv(data_file, sep = ';')
        
        super().__init__(df)
    
    def clean(self):
        df = self
        
        # NA: unknown
        for col in ['Gender', 'Eyes', 'Hair', 'Smoker', 'EduMother', 'EduFather', 'SmokeMother', 'SmokeFather', 'ZodiacSign']:
            df[col] = np.where(df[col].isna(), 'Unknown', df[col].str.title())
        
        # NA: mean by gender
        for col in ['Weight', 'Size', 'Shoesize']:
            df[col] = df[col].fillna(df.groupby('Gender')[col].transform('mean'))
        
        # NA: median
        for col in ['Mathgrade', 'Germangrade', 'Englishgrade']:
            df[col] = np.where(df[col].isna(), df[col].median(), df[col])
        
        # NA: mean
        df['SizeMother'] = np.where(df['SizeMother'].isna(), df['SizeMother'].mean(), df['SizeMother'])
        df['SizeFather'] = np.where(df['SizeFather'].isna(), df['SizeFather'].mean(), df['SizeFather'])
        
        # column types
        df['Gender'] = df['Gender'].astype('category')
        df['Eyes'] = df['Eyes'].astype('category')
        df['Hair'] = df['Hair'].astype('category')
        df['Smoker'] = df['Smoker'].astype('category')
        df['EduMother'] = df['EduMother'].astype('category')
        df['SmokeMother'] = df['SmokeMother'].astype('category')
        df['EduFather'] = df['EduFather'].astype('category')
        df['SmokeFather'] = df['SmokeFather'].astype('category')
        df['ZodiacSign'] = df['ZodiacSign'].astype('category')
        
        return df
