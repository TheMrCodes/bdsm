"""
The :mod:`bdsm.metrics._classification` module includes classes and
functions to calculate and display classification metrics.
"""

# Author: Alexander Adrowitzer <alexander.adrowitzer@fhstp.ac.at>

import pandas as pd

def confusion_matrix(y_pred, y_true):
    """Displays the confusion matrix in BDS standard format.
    
    Parameters:
    -----------
    y_true: Actual classes (e.g. from testset) 
    y_pred: Predicted classes
    """
    return pd.crosstab(y_pred, y_true, rownames=['Predicted'], colnames=['Actual'])