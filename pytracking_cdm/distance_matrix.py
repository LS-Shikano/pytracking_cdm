from itertools import combinations
import pandas as pd
from scipy.spatial.distance import squareform
from weighted_levenshtein import lev
from pytracking_cdm.cost_matrix import gen_costs
import numpy as np


def distance_matrix(
    df: pd.DataFrame,
    insert_costs_dct: dict = None,
    delete_costs_dct: dict = None,
    substitute_costs_dct: dict = None,
    code_dct: dict = None,
    normalize: bool = False,
) -> np.ndarray:
    """distance_matrix: generates a matrix of levenshtein distances between all sequences pairs from a pandas dataframe
    of one sequence per row
    Params:
    ------
    df: pandas dataframe containing one sequence per row
    insert_costs_dct: Optionally, a dictionary like this: {'"': 2}. A string as key and a insertion cost as value
    delete_costs_dct: Optionally, a dictionary like this: {'"': 2}. A string as key and a deletion cost as value
    substitute_costs_dct: Optionally, a dictionary like this: {'"': {"a": 1.25}}. A string as key and a dictionary as
    value.
    This dictionary should contain all other characters as keys and the cost of substituting the key of the parent
    dictionary with the key of the nested dictionary as values
    code_dct: If your sequences are encoded, but your cost dictionaries are not, also specify a code dictionary.
    normalize: Optionally normalize the levenshtein distance by dividing the distance between two strings by the length
    of the longer string

    Returns:
    ------
    A numpy ndarray (matrix) of levenshtein distances.

    Usage:
    ------
    >>> from pytracking_cdm.distance_matrix import distance_matrix
    >>> sequencer("path/to/folder", id_col="subj", sep_col="trial", aoi_col="aoi")
    """

    lst = df.seq.values.tolist()

    insert_costs = gen_costs(1, insert_costs_dct, code_dct)
    delete_costs = gen_costs(1, delete_costs_dct, code_dct)
    substitute_costs = gen_costs(2, substitute_costs_dct, code_dct)

    if normalize:
        distances = [
            lev(i, j, insert_costs=insert_costs, delete_costs=delete_costs, substitute_costs=substitute_costs)
            / max(len(i), len(j))
            for (i, j) in combinations(lst, 2)
        ]
    else:
        distances = [
            lev(i, j, insert_costs=insert_costs, delete_costs=delete_costs, substitute_costs=substitute_costs)
            for (i, j) in combinations(lst, 2)
        ]

    distance_matrix = squareform(distances)
    return distance_matrix
