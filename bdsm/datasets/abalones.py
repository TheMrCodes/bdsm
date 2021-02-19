import numpy as np
import pandas as pd
from ._helper import _load_file

class AbalonesSeries(pd.Series):
    @property
    def _constructor(self):
        return AbalonesSeries
    
    @property
    def _constructor_expanddim(self):
        return AbalonesDataFrame
    

class AbalonesDataFrame(pd.DataFrame):    
    @property
    def _constructor(self):
        return AbalonesDataFrame
    
    @property
    def _constructor_sliced(self):
        return AbalonesSeries
    
    def clean(self, unit = 'imperial'):
        df = self
        
        # column types
        df['Sex'] = df['Sex'].astype('category')
        
        # set clean state
        df.attrs['cleaned'] = True
        
        return df
    
    def to_numeric(self):
        # clean df if not cleaned
        if not self.attrs['cleaned']:
            df = self.clean()
        else:
            df = self
        
        cat = df.select_dtypes(['category']).columns
        cat_codes = [x + '_cat' for x in cat]
        
        df[cat_codes] = df[cat].apply(lambda x: x.cat.codes)
        
        df = df.select_dtypes(include = ['number'])
        
        return df


def abalones():
    data_file = _load_file('abalones.csv')
    
    df = AbalonesDataFrame(pd.read_csv(data_file))
    df.attrs['cleaned'] = False
    
    return df
