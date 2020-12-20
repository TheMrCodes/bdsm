"""
Base IO code for all datasets
"""

import os
import pandas as pd

class BdsmDataFrame(pd.DataFrame):    
    def __init__(self, df) -> pd.core.api.DataFrame:        
        super(BdsmDataFrame, self).__init__(df)
    
    def _load_file(self, file) -> os.path:
        module_path = os.path.dirname(__file__)
        data_path = os.path.join(module_path, 'data')
        
        return os.path.join(data_path, file)
    
    def to_numeric(self) -> pd.core.api.DataFrame:
        df = self.clean()
        
        cat = df.select_dtypes(['category']).columns
        cat_codes = [x + '_cat' for x in cat]
        
        df[cat_codes] = df[cat].apply(lambda x: x.cat.codes)
        
        df = df.select_dtypes(include = ['number'])
        
        return df
