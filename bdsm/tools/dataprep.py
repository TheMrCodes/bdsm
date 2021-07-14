"""
The :mod:`bdsm.tools._dataprep` module includes classes and
functions to inspect and prepare a dataset.
"""

# Author: Alexander Adrowitzer <alexander.adrowitzer@fhstp.ac.at>

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

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

def standardized_split(X, y, test_size=None, train_size=None, random_state=None, shuffle=True, stratify=None):
    """Applies sklearn ``StandardScaler`` to output of 
    sklearn ``train_test_split``.
    """
    sc = StandardScaler()

    xtr, xte, ytr, yte = train_test_split(X, 
        y, 
        test_size=test_size, 
        train_size=train_size, 
        random_state=random_state, 
        shuffle=shuffle, 
        stratify=stratify)
    xtr, xte, ytr, yte = train_test_split(X,y)
    xtrain = sc.fit_transform(xtr)
    xtest = sc.fit_transform(xte)
    return xtrain, xtest, ytr, yte