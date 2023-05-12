from importlib_resources import files
import pandas as pd
import numpy as np
from pytracking_cdm import __version__
from pytracking_cdm.sequencer import sequence, gen_code_dct, sequencer
from pytracking_cdm.distance_matrix import distance_matrix
from pytracking_cdm.cost_matrix import cost_matrix
from pytracking_cdm import SeqAnaObj
from weighted_levenshtein import lev


def test_sequence():
    df_1 = pd.DataFrame({"aoi": pd.Series([1, 2, 2, 2, 5, 6, 8, 8, 9], dtype="str")})
    seq = sequence(df_1, "aoi")
    assert seq == "122256889"
    seq = sequence(df_1, "aoi", merge=True)
    assert seq == "125689"


def test_gen_code_dct():
    # empty code dict
    df_1 = pd.DataFrame({"aoi": pd.Series([1, 2, 2, 2, 5, 6, 8, 8, 9], dtype="str")})
    code_dct = gen_code_dct(df_1, "aoi")
    assert code_dct == {"1": "!", "2": '"', "5": "#", "6": "$", "8": "%", "9": "&"}
    # filled code dict
    df_2 = pd.DataFrame({"aoi": pd.Series([8, 8, 0, 0, 10, 11, 13, 1, 2], dtype="str")})
    code_dct = gen_code_dct(df_2, "aoi", code_dct)
    assert code_dct == {
        "1": "!",
        "2": '"',
        "5": "#",
        "6": "$",
        "8": "%",
        "9": "&",
        "0": "'",
        "10": "(",
        "11": ")",
        "13": "*",
    }


def test_sequencer():
    df = pd.DataFrame(
        {
            "id": pd.Series(["1_1", "1_2", "1_3", "2_1", "2_2", "2_3"], dtype="str"),
            "seq": pd.Series(['!""', '"#$', "%&&", "''(", "()!", '!""'], dtype="str"),
            "len": pd.Series([3, 3, 3, 3, 3, 3], dtype="int"),
        }
    )
    seq = sequencer(
        files("tests.data.simple.trial_sep")._paths[0],
        id_col="subj",
        sep_col="trial",
        aoi_col="aoi",
    )[0]
    pd.testing.assert_frame_equal(df, seq)


def test_cost_matrix():
    costs = cost_matrix(1, {'"': 2})
    dist = lev("abc", 'ab"c', insert_costs=costs)
    assert dist == 2
    costs = cost_matrix(1, {'"': 2})
    dist = lev('abc"', "abc", delete_costs=costs)
    assert dist == 2
    costs = cost_matrix(2, {'"': {"a": 1.25}})
    dist = lev('"bc', "abc", substitute_costs=costs)
    assert dist == 1.25


def test_cost_matrix_coded():
    code_dct = {"1": '"', "2": "a"}
    costs = cost_matrix(1, {"1": 2}, code_dct)
    dist = lev("abc", 'ab"c', insert_costs=costs)
    assert dist == 2
    costs = cost_matrix(2, {"1": {"2": 1.25}}, code_dct)
    dist = lev('"bc', "abc", substitute_costs=costs)
    assert dist == 1.25


def test_distance_matrix():
    arr = [
        [0, 1, 2, 1],
        [1, 0, 2, 2],
        [2, 2, 0, 3],
        [1, 2, 3, 0],
    ]
    arr = np.array([np.array(xi) for xi in arr])

    df = pd.DataFrame(
        {
            "id": pd.Series(["1_1", "1_2", "1_3", "1_4"], dtype="str"),
            "seq": pd.Series(["abc", 'ab"c', 'abc""', '"bc'], dtype="str"),
            "len": pd.Series([3, 3, 3, 3], dtype="int"),
        }
    )
    dm = distance_matrix(df)

    np.testing.assert_array_equal(arr, dm)


def test_SeqAnaObj():
    df = pd.DataFrame(
        {
            "id": pd.Series(["1", "2", "3", "4"], dtype="str"),
            "seq": pd.Series(['!!!"', '"!"#!', "!$%%&", '!!!"$'], dtype="str"),
            "len": pd.Series([4, 5, 5, 5], dtype="int"),
        }
    )
    code_dct = {
        "label_one": "!",
        "label_two": '"',
        "label_four": "#",
        "label_six": "$",
        "label_seven": "%",
        "label_nine": "&",
    }

    arr = [
        [0, 4, 4, 1],
        [4, 0, 5, 4],
        [4, 5, 0, 4],
        [1, 4, 4, 0],
    ]
    arr = np.array([np.array(xi) for xi in arr])

    obj = SeqAnaObj(
        files("tests.data.simple.ind")._paths[0],
        id_col="subj",
        aoi_col="aoi",
    )

    pd.testing.assert_frame_equal(df, obj.seq_df)
    assert code_dct == obj.code_dct
    np.testing.assert_array_equal(obj.distance_matrix, arr)
