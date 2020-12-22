"""
Base IO code for all datasets
"""

import os
import numpy as np
import pandas as pd

class BdsmSeries(pd.Series):
    @property
    def _constructor(self):
        return BdsmSeries
    
    @property
    def _constructor_expanddim(self):
        return BdsmDataFrame
    

class BdsmDataFrame(pd.DataFrame):    
    @property
    def _constructor(self):
        return BdsmDataFrame
    
    @property
    def _constructor_sliced(self):
        return BdsmSeries
    
    def _load_file(self, file) -> os.path:
        module_path = os.path.dirname(__file__)
        data_path = os.path.join(module_path, 'data')
        
        return os.path.join(data_path, file)
    
    def clean(self):
        return self
    
    def to_numeric(self):
        df = self.clean()
        
        cat = df.select_dtypes(['category']).columns
        cat_codes = [x + '_cat' for x in cat]
        
        df[cat_codes] = df[cat].apply(lambda x: x.cat.codes)
        
        df = df.select_dtypes(include = ['number'])
        
        return df
