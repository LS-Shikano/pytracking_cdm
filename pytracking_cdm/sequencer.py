import pandas as pd
import os
from typing import TypeVar

PandasDataFrame = TypeVar("pandas.core.frame.DataFrame")


def sequence(df: pd.DataFrame, aoi_col: str, merge: bool = False):
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
    # TODO: error handling if aoi col is not string

    df[aoi_col] = df[aoi_col].astype(str)

    seq = df[aoi_col].str.cat(sep="")

    if merge:
        lst = [*seq]
        temp = []
        # merging sub sequences of identical strings to be one string
        for count, i in enumerate(lst):
            if count != len(lst) - 1:
                if lst[count + 1] != i:
                    temp.append(i)
            else:
                temp.append(i)
        seq = "".join(temp)

    return seq


def ascii_to_char(code):
    # Excluding control characters
    if code < 33 or code > 126:
        raise ValueError("Code must be between 33 and 126")
    return chr(code)


def gen_code_dct(df: pd.DataFrame, aoi_col: str, code_dct: dict):
    uni_start = 33
    new_unique_aoi = [x for x in df[aoi_col].unique().tolist() if x not in code_dct.keys()]
    lock = len(code_dct.keys())
    if len(new_unique_aoi) != 0:
        for lst_count, i in enumerate(new_unique_aoi):
            code_dct[i] = ascii_to_char(uni_start + lock + lst_count)
    return code_dct


def sequencer(
    folder: str,
    id_col: str,
    aoi_col: str,
    off_aoi_str: str = None,
    sep_col: str = None,
    **kwargs,
):
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
    code_dct = dict()

    with os.scandir(folder) as it:
        for entry in it:
            df = pd.read_csv(entry.path)

            if off_aoi_str is not None:
                df = df[df[aoi_col] != off_aoi_str]

            code_dct = gen_code_dct(df, aoi_col, code_dct)

            df[aoi_col] = df[aoi_col].apply(lambda x: code_dct[x])

            if sep_col is not None:
                df_lst = [y for x, y in df.groupby(sep_col)]
                for df in df_lst:
                    seq = sequence(df, aoi_col=aoi_col, **kwargs)
                    seq_lst.append(seq)
                    length_lst.append(len(seq))
                    id_lst.append(f"{df[id_col].iloc[0]}_{df[sep_col].iloc[0]}")

            else:
                seq = sequence(df, aoi_col=aoi_col, **kwargs)
                length_lst.append(len(seq))
                seq_lst.append(seq)
                id_lst.append(f"{id_col[id_col].iloc[0]}")

    df = pd.DataFrame({"id": id_lst, "seq": seq_lst, "len": length_lst})

    return df
