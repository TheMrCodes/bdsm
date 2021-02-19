import numpy as np
import pandas as pd
from ._helper import _load_file

class WineSeries(pd.Series):
    @property
    def _constructor(self):
        return WineSeries
    
    @property
    def _constructor_expanddim(self):
        return WineDataFrame
    

class WineDataFrame(pd.DataFrame):    
    @property
    def _constructor(self):
        return WineDataFrame
    
    @property
    def _constructor_sliced(self):
        return WineSeries
    
    def clean(self, unit = 'imperial'):
        df = self
        
        # column types
        df['color'] = df['color'].astype('category')
        
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


def wine():
    data_file = _load_file('wine.csv')
    
    df = WineDataFrame(pd.read_csv(data_file, delimiter = ';'))
    df.attrs['cleaned'] = False
    
    return df
