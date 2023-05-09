from importlib_resources import files
import pandas as pd
import numpy as np
from pytracking_cdm import __version__
from pytracking_cdm.sequencer import sequence, gen_code_dct, sequencer
from pytracking_cdm.distance_matrix import distance_matrix
from pytracking_cdm.cost_matrix import gen_costs
from weighted_levenshtein import lev


def test_version():
    assert __version__ == "0.1.0"


def test_sequence():
    test_df1 = pd.DataFrame({"aoi": pd.Series([1, 2, 2, 2, 5, 6, 8, 8, 9], dtype="str")})
    seq = sequence(test_df1, "aoi")
    assert seq == "122256889"
    seq = sequence(test_df1, "aoi", merge=True)
    assert seq == "125689"


def test_gen_code_dct():
    # empty code dict
    test_df1 = pd.DataFrame({"aoi": pd.Series([1, 2, 2, 2, 5, 6, 8, 8, 9], dtype="str")})
    code_dct = gen_code_dct(test_df1, "aoi")
    assert code_dct == {"1": "!", "2": '"', "5": "#", "6": "$", "8": "%", "9": "&"}
    # filled code dict
    test_df2 = pd.DataFrame({"aoi": pd.Series([8, 8, 0, 0, 10, 11, 13, 1, 2], dtype="str")})
    code_dct = gen_code_dct(test_df2, "aoi", code_dct)
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
    test_df_1 = pd.DataFrame(
        {
            "id": pd.Series(["1_1", "1_2", "1_3", "2_1", "2_2", "2_3"], dtype="str"),
            "seq": pd.Series(['!""', '"#$', "%&&", "''(", "()!", '!""'], dtype="str"),
            "len": pd.Series([3, 3, 3, 3, 3, 3], dtype="int"),
        }
    )
    seq = sequencer(
        files("tests.data.simple.same_length")._paths[0],
        id_col="subj",
        sep_col="trial",
        aoi_col="aoi",
    )
    pd.testing.assert_frame_equal(test_df_1, seq)


def test_gen_costs():
    costs = gen_costs(1, {'"': 2})
    dist = lev("abc", 'ab"c', insert_costs=costs)
    assert dist == 2
    costs = gen_costs(1, {'"': 2})
    dist = lev('abc"', "abc", delete_costs=costs)
    assert dist == 2
    costs = gen_costs(2, {'"': {"a": 1.25}})
    dist = lev('"bc', "abc", substitute_costs=costs)
    assert dist == 1.25


def test_gen_costs_coded():
    code_dct = {"1": '"', "2": "a"}
    costs = gen_costs(1, {"1": 2}, code_dct)
    dist = lev("abc", 'ab"c', insert_costs=costs)
    assert dist == 2
    costs = gen_costs(2, {"1": {"2": 1.25}}, code_dct)
    dist = lev('"bc', "abc", substitute_costs=costs)
    assert dist == 1.25


def test_distance_matrix():
    arr = [
        [
            0,
            1,
            2,
            1,
        ],
        [
            1,
            0,
            2,
            2,
        ],
        [
            2,
            2,
            0,
            3,
        ],
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
