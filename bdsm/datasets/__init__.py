"""
datasets
==================================
Datasets for Data Science
"""

from .abalones import abalones
from .bodyfat import bodyfat
from .iris import iris
from .mall import mall
from .penguins import penguins
from .students import students
from .titanic import titanic
from .wine import wine

from .processes import wn, ma, ar, arma

l_datasets = ['abalones', 'bodyfat', 'iris', 'mall', 'penguins', 'students', 'titanic', 'wine']
l_processes = ['wn', 'ma', 'ar', 'arma']

__all__ = l_datasets + l_processes
