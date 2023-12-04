import pandas as pd
import numpy as np
from pytracking_cdm.sequencer import sequence, gen_code_dct, sequencer
from pytracking_cdm.distance_matrix import distance_matrix
from pytracking_cdm.cost_matrix import cost_matrix
from pytracking_cdm import SeqAnaObj
from weighted_levenshtein import lev

def test_g_SeqAnaObj(path_real_data):
    obj = SeqAnaObj(
        path_real_data,
        id_col="participant_id",
        aoi_col="row_label",
        off_aoi_str="nan"
    )

