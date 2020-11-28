"""
Loader for all datasets
"""

import os
from .dataset import Dataset

module_path = os.path.dirname(__file__)
data_path = os.path.join(module_path, 'data')

def load_abalones():
    data_file = os.path.join(data_path, 'abalones.csv')
    
    data = Dataset(file = data_file)    
    df = data.get_df()
    
    return df
