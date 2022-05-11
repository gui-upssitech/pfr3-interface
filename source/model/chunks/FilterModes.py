from enum import Enum

"""
Classe FilterModes qui stocke tous les filtres de chunk disponibles
"""
class FilterModes(Enum):
    AVERAGE = 0
    NO_ZERO_AVERAGE = 1
    MEDIAN = 2
    CONST = 3
