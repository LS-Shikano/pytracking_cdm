import pandas as pd
import numpy as np
from pytracking_cdm.sequencer import sequence, gen_code_dct, sequencer
from pytracking_cdm.distance_matrix import distance_matrix
from pytracking_cdm.cost_matrix import cost_matrix
from pytracking_cdm import SeqAnaObj
from weighted_levenshtein import lev


def test_a_sequence(df_a, seq_a):
    seq = sequence(df_a, "aoi")
    assert seq == seq_a
    seq = sequence(df_a, "aoi", merge=True)
    assert seq == "125689"


def test_b_gen_code_dct(df_b, df_b_2, dct_b, dct_b_2):
    # empty code dict
    code_dct = gen_code_dct(df_b, "aoi")
    assert code_dct == dct_b
    # filled code dict
    code_dct = gen_code_dct(df_b_2, "aoi", code_dct)
    assert code_dct == dct_b_2

def test_c_sequencer(df_c, path_c):
    seq = sequencer(
        path_c,
        id_col="subj",
        sep_col="trial",
        aoi_col="aoi",
    )[0]
    pd.testing.assert_frame_equal(df_c, seq)


def test_d_cost_matrix():
    costs = cost_matrix(1, {'"': 2})
    dist = lev("abc", 'ab"c', insert_costs=costs)
    assert dist == 2
    costs = cost_matrix(1, {'"': 2})
    dist = lev('abc"', "abc", delete_costs=costs)
    assert dist == 2
    costs = cost_matrix(2, {'"': {"a": 1.25}})
    dist = lev('"bc', "abc", substitute_costs=costs)
    assert dist == 1.25


def test_e_cost_matrix_coded():
    code_dct = {"1": '"', "2": "a"}
    costs = cost_matrix(1, {"1": 2}, code_dct)
    dist = lev("abc", 'ab"c', insert_costs=costs)
    assert dist == 2
    costs = cost_matrix(2, {"1": {"2": 1.25}}, code_dct)
    dist = lev('"bc', "abc", substitute_costs=costs)
    assert dist == 1.25


def test_f_distance_matrix(arr_f, df_f):
    dm = distance_matrix(df_f)
    np.testing.assert_array_equal(arr_f, dm)


def test_g_SeqAnaObj(df_g, dct_g, arr_g, path_g):
    
    obj = SeqAnaObj(
        path_g,
        id_col="subj",
        aoi_col="aoi",
    )

    pd.testing.assert_frame_equal(df_g, obj.seq_df)
    assert dct_g == obj.code_dct
    np.testing.assert_array_equal(obj.distance_matrix, arr_g)
