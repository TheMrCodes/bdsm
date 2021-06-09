"""
The :mod:`bdsm.tools._dataprep` module includes classes and
functions to inspect and prepare a dataset.
"""

# Author: Alexander Adrowitzer <alexander.adrowitzer@fhstp.ac.at>

import pandas as pd

def quality(df):
    """Quality inspection of a DataFrame

        Returns
        -------
        result : DataFrame
            Returns:
                number of rows and columns (formatted)
                datatype of columns
                number of missing values per column (absolute and relative)
                number of unique values per column
        """   
    result = pd.DataFrame(df.dtypes,columns=['type'])
    result['unique'] = pd.DataFrame(df.nunique())
    result['missing_abs'] = pd.DataFrame(df.isna().sum())
    result['missing_rel'] = pd.DataFrame(round(100*df.isna().sum()/len(df),2))
    numrows = df.shape[0]
    print("Dataframe has " + f'{numrows:,}' + " rows and " + str(df.shape[1]) + " columns.\n")
    print(str(result[result['missing_abs'] != 0].shape[0]) + " columns have missing values.")
    
    return result