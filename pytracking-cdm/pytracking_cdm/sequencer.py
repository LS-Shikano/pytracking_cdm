import pandas as pd
import numpy as np
import os
import re
from collections.abc import Callable
from typing import TypeVar
PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')


def sequence(df: pd.DataFrame,  aoi_col: str, merge: bool = False, off_aoi_str: str = None):
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

    if off_aoi_str != None:
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


def sequencer(folder: str, id_col: str, aoi_col:str, off_aoi_str: str = None, sep_col: str = None, **kwargs):
    """sequencer: converts a dataframe containing row wise fixations to a sequence
    Params:
    ------
    folder: Input folder containing one file of eyetracking data as csv per ballot.
    Usage:
    ------
    >>> from pytracking_cdm.sequencer import sequencer
    >>> sequencer("data/individual/")
    """
    uni_start = 35

    seq_lst = []
    id_lst = []
    length_lst = []
    unique_aoi = []
    code_dct = dict()
    if off_aoi_str != None:
        code_dct[off_aoi_str]= chr(uni_start-1)
    
    with os.scandir(folder) as it:
        for entry in it:
            df = pd.read_csv(entry.path)
            
            new_unique_aoi = [x for x in df[aoi_col].unique().tolist() if x not in unique_aoi]
            if len(new_unique_aoi) != 0:
                for lst_count,i in enumerate(new_unique_aoi):
                    code_dct[i] = chr(uni_start+len(unique_aoi)+lst_count)

            unique_aoi = unique_aoi + new_unique_aoi

            df[aoi_col] = df[aoi_col].apply(lambda x : code_dct[x])
            
            if sep_col != None:
                df_lst = [y for x, y in df.groupby(sep_col)]
                for df in df_lst:
                    seq = sequence(df, aoi_col=aoi_col, off_aoi_str=off_aoi_str,**kwargs)
                    seq_lst.append(seq)
                    length_lst.append(len(seq))
                    id_lst.append(f"{df[id_col].iloc[0]}_{df[sep_col].iloc[0]}")
                
            else:
                df = pd.read_csv(csv)
                seq = sequence_csv(df, aoi_col=aoi_col, off_aoi_str=off_aoi_str, **kwargs)
                length_lst.append(len(seq))
                seq_lst.append(seq)
                id_lst.append(f"{id_col[id_col].iloc[0]}")

    df = pd.DataFrame({"id": id_lst, "seq": seq_lst, "len": length_lst})

    return df
