"""
datasets
==================================
Datasets for Data Science
"""

from .abalones import abalones
from .bodyfat import bodyfat
from .boston import boston
from .iris import iris
from .mall import mall
from .penguins import penguins
from .shopping import shopping
from .students import students
from .sunshine import sunshine
from .titanic import titanic
from .wine import wine

from .processes import wn, ma, ar, arma

l_datasets = ['abalones', 'bodyfat', 'boston', 'iris', 'mall', 'penguins', 'shopping', 'students', 'sunshine','titanic', 'wine']
l_processes = ['wn', 'ma', 'ar', 'arma']

__all__ = l_datasets + l_processes
