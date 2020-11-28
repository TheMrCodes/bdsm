"""
Base IO code for all datasets
"""

import pandas as pd

class Dataset():
    def __init__(self, file, sep = ','):
        self.file = file
        self.sep = sep
        self.load_file()
    
    def load_file(self):
        self.df = pd.read_csv(self.file, sep = self.sep)
    
    def get_df(self):
        return self.df
