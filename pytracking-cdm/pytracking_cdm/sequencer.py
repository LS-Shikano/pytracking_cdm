import pandas as pd
import numpy as np
import os
import re
from string import ascii_lowercase as alc
from collections.abc import Callable
from typing import TypeVar
PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')


##### Dictionaries for Encoding the Sequences ######
complete_inst = chr(33)
off_ballot = chr(34)
# Row level
dct_rows = {
    "complete-instructions": complete_inst,
    "off_ballot": off_ballot,
    "row_fv_1": "B",
    "row_fv_2": "C",
    "row_fv_3": "D",
    "row_fv_4": "E",
    "row_fv_5": "F",
    "row_fv_6": "G",
    "row_sv_1": "H",
    "row_sv_2": "I",
    "row_sv_3": "J",
    "row_sv_4": "K",
    "row_sv_5": "L",
    "row_sv_6": "M"
}

# AOI
# AOI with position
dct_aoi = {'complete-instructions': complete_inst, 'off_ballot': off_ballot, 'cand_name_fv_1': '#',
           'cand_name_fv_2': '$', 'cand_name_fv_3': '%', 'cand_name_fv_4': '&',
           'cand_name_fv_5': "'", 'cand_name_fv_6': '(', 'party_abbr_fv_1': ')',
           'party_abbr_fv_2': '*', 'party_abbr_fv_3': '+', 'party_abbr_fv_4': ',',
           'party_abbr_fv_5': '-', 'party_abbr_fv_6': '.', 'party_full_fv_1': '/',
           'party_full_fv_2': '0', 'party_full_fv_3': '1', 'party_full_fv_4': '2',
           'party_full_fv_5': '3', 'party_full_fv_6': '4', 'cand_info_fv_1': '5',
           'cand_info_fv_2': '6', 'cand_info_fv_3': '7', 'cand_info_fv_4': '8',
           'cand_info_fv_5': '9', 'cand_info_fv_6': ':', 'party_full_sv_1': ';',
           'party_full_sv_2': '<', 'party_full_sv_3': '=', 'party_full_sv_4': '>',
           'party_full_sv_5': '?', 'party_full_sv_6': '@', 'party_leaders_sv_1': 'A',
           'party_leaders_sv_2': 'B', 'party_leaders_sv_3': 'C', 'party_leaders_sv_4': 'D',
           'party_leaders_sv_5': 'E', 'party_leaders_sv_6': 'F', 'party_abbr_sv_1': 'G',
           'party_abbr_sv_2': 'H', 'party_abbr_sv_3': 'I', 'party_abbr_sv_4': 'J',
           'party_abbr_sv_5': 'K', 'party_abbr_sv_6': 'L'}

# Code that generated this dict:

# dct_aoi = {
#     "complete-instructions":chr(33), # -> !
#     "off_ballot": chr(34) # -> "
# }
#
#
# lst = ["cand_name_fv", "party_abbr_fv", "party_full_fv", "cand_info_fv", "party_full_sv", "party_leaders_sv", "party_abbr_sv"]
# temp = 0
# for count,i in enumerate(lst):
#     for y in range(1,7):
#         dct_aoi[f"{i}_{y}"] = chr(temp+35)
#         temp+=1


# AOI without position

dct_aoi_wo_pos = {'complete-instructions': complete_inst, 'off_ballot': off_ballot,
                  'cand_name_fv': 'a', 'party_abbr_fv': 'b', 'party_full_fv': 'c',
                  'cand_info_fv': 'd', 'party_full_sv': 'e', 'party_leaders_sv': 'f',
                  'party_abbr_sv': 'g'}

# Code that generated this dict:

# dct_aoi_wo_pos = {
#     "complete-instructions":'!',
#     "off_ballot": '"'
# }
# for count,i in enumerate(lst):
#     dct_aoi_wo_pos[i] = alc[count]

################


def sequence(df: pd.DataFrame,  aoi_col: str, merge: bool = False, off_aoi: bool = True, off_aoi_str: str = None):
    """sequencer: converts a csv containing row wise fixations to a sequence
    Params:
    ------
    df: pandas dataframe
    merge: Merge contiguous identical strings 
    off_aoi: Include off AOI rows in sequence

    Usage:
    ------
    >>> from pytracking_cdm.sequence_csv import sequence_csv
    >>> sequence_csv("data/individual/inv_1.csv", "et_rois")
    """

    if off_ballot == False & off_aoi != None:
        df = df[df[aoi_col] != off_aoi_str]

    seq = df[aoi_col].astype(str).str.cat(sep='')

    if merge:
        lst = [*seq]
        temp = []
        # merging sub sequences of identical strings to be one string
        for count, i in enumerate(lst):
            if count != len(lst)-1:
                if lst[count+1] != i:
                    temp.append(i)
            else:
                temp.append(i)
        seq = "".join(temp)

    return seq


def sequencer(folder: str, mult_seq: bool = False, group_by_col: str = None, **kwargs):
    """sequencer: converts a dataframe containing row wise fixations to a sequence
    Params:
    ------
    folder: Input folder containing one file of eyetracking data as csv per ballot.
    Usage:
    ------
    >>> from pytracking_cdm.sequencer import sequencer
    >>> sequencer("data/individual/")
    """
    seq_lst = []
    id_lst = []
    length_lst = []

    # List the files in the folder
    folder_lst = os.listdir(folder)

    # TODO: Add subject id,

    for fl in folder_lst:
        df = pd.read_csv(fl)
        if mult_seq:
            df_lst = [y for x, y in df.groupby(group_by_col)]
            print(df_lst)
            for df in df_lst:
                seq = sequence_csv(df, **kwargs)
                seq_lst.append(seq)
                length_lst.append(len(seq))
                id_lst.append(fl)
        else:
            df = pd.read_csv(csv)
            seq = sequence_csv(df, **kwargs)
            length_lst.append(len(seq))
            seq_lst.append(seq)
            id_lst.append(fl)

    df = pd.DataFrame({"id": id_lst, "seq": seq_lst, "len": length_lst})

    return df
