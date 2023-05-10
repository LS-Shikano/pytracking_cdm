from pytracking_cdm.sequencer import sequencer
from pytracking_cdm.distance_matrix import distance_matrix
import pandas as pd
import numpy as np


class SeqAnaObj:
    """
    Attributes
    ------

    seq_df: A pandas dataframe of one sequence per row per individual or trial, depending on params
    code_dct: Dictionary with the aoi labels as keys and their encoded sequence chars as values.
    distance_matrix: A numpy ndarray (matrix) of levenshtein distances.

    """

    def __init__(
        self,
        folder: str,
        id_col: str,
        aoi_col: str,
        off_aoi_str: str = None,
        sep_col: str = None,
        merge: bool = False,
        normalize: bool = False,
        insert_costs_dct: dict = None,
        delete_costs_dct: dict = None,
        substitute_costs_dct: dict = None,
    ):
        """
        init: transforms a folder of csv files containing row wise fixations to a dataframe of sequences and then
        generates a matrix of levenshtein distances from these sequences.

        Params:
        ------
        folder: Input folder containing one file of eyetracking data as csv per individual or trial.
        id_col: Name of the column containing the unique id of the individual or trial.
        aoi_col: Name of the column containing the label of the area of interest.
        off_aoi_str: Optional, exclude the AOIs with this label when generating the sequences. This is usually the
        label for a fixation that's not on an area of interest.
        sep_col: Optional, a column that contains some category (for example trials) that should be treated as separate
        sequences.
        insert_costs_dct: Optionally, a dictionary like this: {'"': 2}. A string as key and a insertion cost as value
        delete_costs_dct: Optionally, a dictionary like this: {'"': 2}. A string as key and a deletion cost as value
        substitute_costs_dct: Optionally, a dictionary like this: {'"': {"a": 1.25}}. A string as key and a dictionary
        as value.

        Usage:
        ------
        >>> from pytracking_cdm import SeqAnaObj
        >>> obj = SeqAnaObj("folder/path", id_col='id', aoi_col='aoi', sep_col='trial')
        """
        temp = sequencer(
            folder=folder, id_col=id_col, aoi_col=aoi_col, off_aoi_str=off_aoi_str, sep_col=sep_col, merge=merge
        )
        self.seq_df: pd.DataFrame = temp[0]
        self.code_dct: dict = temp[1]
        self.distance_matrix: np.ndarray = distance_matrix(
            self.seq_df,
            insert_costs_dct=insert_costs_dct,
            delete_costs_dct=delete_costs_dct,
            substitute_costs_dct=substitute_costs_dct,
            code_dct=self.code_dct,
            normalize=normalize,
        )
