"""
tools
==================================
Several tools for Data Science
"""

from .dataprep import quality
from .dataprep import standardized_split
from .getpath import getpath
from .vif import vif

__all__ = [
    'quality',
    'standardized_split',
    'getpath',
    'vif'
]
