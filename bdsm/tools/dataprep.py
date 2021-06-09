"""
The :mod:`bdsm.tools._dataprep` module includes classes and
functions to inspect and prepare a dataset.
"""

# Author: Alexander Adrowitzer <alexander.adrowitzer@fhstp.ac.at>

import locale
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
    locale.setlocale(locale.LC_ALL, 'en_US')
    result = pd.DataFrame(df.dtypes,columns=['type'])
    result['unique'] = pd.DataFrame(df.nunique())
    result['missing_abs'] = pd.DataFrame(df.isna().sum())
    result['missing_rel'] = pd.DataFrame(round(100*df.isna().sum()/len(df),2))
    print("Dataframe has " + locale.format_string("%d", df.shape[0], grouping=True) + " rows and " + str(df.shape[1]) + " columns.\n")
    print(str(result[result['missing_abs'] != 0].shape[0]) + " columns have missing values.")
    
    return result