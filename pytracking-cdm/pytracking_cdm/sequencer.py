import pandas as pd
import numpy as np
import os
import re
from string import ascii_lowercase as alc
from collections.abc import Callable


##### Dictionaries for Encoding the Sequences ######
complete_inst = chr(33)
off_ballot= chr(34)
# Row level
dct_rows = {
    "complete-instructions":complete_inst,
    "off_ballot": off_ballot,
    "row_fv_1":"B",
    "row_fv_2":"C",
    "row_fv_3":"D",
    "row_fv_4":"E",
    "row_fv_5":"F",
    "row_fv_6":"G",
    "row_sv_1":"H",
    "row_sv_2":"I",
    "row_sv_3":"J",
    "row_sv_4":"K",
    "row_sv_5":"L",
    "row_sv_6":"M"
}

# AOI
## AOI with position
dct_aoi= {'complete-instructions': complete_inst, 'off_ballot': off_ballot, 'cand_name_fv_1': '#',
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

def sequence_csv(file:str, aoi_col:str, merge:bool=False, off_aoi:bool=True, off_aoi_str:str=None):
    """sequencer: converts a csv containing row wise fixations to a sequence
    Params:
    ------
    file: path to csv file
    merge: Merge contiguous identical strings 
    off_aoi: Include off AOI rows in sequence
    
    Usage:
    ------
    >>> from pytracking_cdm.sequence_csv import sequence_csv
    >>> sequence_csv("data/individual/inv_1.csv", "et_rois")
    """

    # Read the labelled gaze file
    df = pd.read_csv(file)

    if off_ballot == False & off_aoi != None:
        df = df[df[aoi_col] != off_aoi_str]

    seq = df[aoi_col].astype(str).str.cat(sep='')

    if merge:
        lst = [*seq]
        temp = []
        # merging sub sequences of identical strings to one string
        for count,i in enumerate(lst):
            if count != len(lst)-1:
                if lst[count+1] != i:
                    temp.append(i)
            else:
                temp.append(i)
        seq = "".join(temp)
    
    return seq


def sequencer(folder:str, seq_method:str="sequence_csv", *args):
    """sequencer: converts a dataframe containing row wise fixations to a sequence
    Params:
    ------
    folder: Input folder containing one file of eyetracking data as csv per ballot.
    seq_method: Sequence method to be used. 
        - 'sequence_csv': converts a csv to a sequence
    Usage:
    ------
    >>> from pytracking_cdm.sequencer import sequencer
    >>> sequencer("data/individual/sequence_csv")
    """
    seq_lst = []
    id_lst = []
    length_lst=[]

    # List the files in the folder
    folder_lst = os.listdir(folder)

    for file in folder_lst:

        # Store the individual file name for later use
        filename = file[:-4]

        filepath = os.path.join(folder, file)

        # Check if file is a file and not a directory
        if os.path.isfile(filepath):
            # Read the labelled gaze file
            df = pd.read_csv(filepath)

            # Adding colum that contains the assigned letter
            if level == 1:
                if position==False:
                    raise NotImplementedError("Position can only be disregarded when doing analysis on level 2")
                # Replace nan with string
                df["row_label"] = df["row_label"].fillna(np.nan).replace([np.nan], ["off_ballot"])
                if off_ballot == False:
                    df = df[df["row_label"] != "off_ballot"]
                df["seq_event"] = df["row_label"].apply(lambda x : dct_rows[x])

            elif level == 2:
                df["class_label"] = df["class_label"].fillna(np.nan).replace([np.nan], ["off_ballot"])
                if off_ballot == False:
                    df = df[df["class_label"] != "off_ballot"]
                if position:
                    df["seq_event"] = df["class_label"].apply(lambda x : dct_aoi[x] if not pd.isnull(x) else "")
                else:
                    df["seq_event"] = df["class_label"].apply(lambda x : dct_aoi_wo_pos[re.sub("_\d","",x)])

            # generating sequence
            seq = df["seq_event"].str.cat(sep='')

            if merge:
                lst = [*seq]
                temp = []
                # merging sub sequences of identical strings to one string
                for count,i in enumerate(lst):
                    if count != len(lst)-1:
                        if lst[count+1] != i:
                            temp.append(i)
                    else:
                        temp.append(i)
                seq = "".join(temp)

            length_lst.append(len(seq))
            seq_lst.append(seq)
            id_lst.append(filename)

    df = pd.DataFrame({"id": id_lst, "seq": seq_lst, "len":length_lst})

    return df


# sequencer(level=1,
#           folder=f"Data/Labelled_Data/Individual_Ballots/Double/Fixations/AOI_Fixations/30ms")