from itertools import combinations
from scipy.spatial.distance import squareform
from weighted_levenshtein import lev
from pytracking_cdm.cost_matrix import gen_costs


def distance_matrix(
    df,
    insert_costs_dct: dict = None,
    delete_costs_dct: dict = None,
    substitute_costs_dct: dict = None,
    code_dct: dict = None,
    div_len: bool = False,
):
    """

    @param df:
    dataframe containing one sequence per row
    @param metric:
    one of "distance","jaro" or "jaro_winkler"
    @param div_len:
    if True, divide distance by length of longer sequence
    @return:
    """

    lst = df.seq.values.tolist()

    insert_costs = gen_costs(1, insert_costs_dct, code_dct)
    delete_costs = gen_costs(1, delete_costs_dct, code_dct)
    substitute_costs = gen_costs(2, substitute_costs_dct, code_dct)

    if div_len:
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
