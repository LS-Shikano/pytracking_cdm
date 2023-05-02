from importlib_resources import files
import pandas as pd
from pytracking_cdm import __version__
from pytracking_cdm.sequencer import sequence, gen_code_dct, sequencer


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
    code_dct = gen_code_dct(test_df1, "aoi", {})
    assert code_dct == {"1": "#", "2": "$", "5": "%", "6": "&", "8": "'", "9": "("}
    # filled code dict
    test_df2 = pd.DataFrame({"aoi": pd.Series([8, 8, 0, 0, 10, 11, 13, 1, 2], dtype="str")})
    code_dct = gen_code_dct(test_df2, "aoi", code_dct)
    assert code_dct == {
        "1": "#",
        "2": "$",
        "5": "%",
        "6": "&",
        "8": "'",
        "9": "(",
        "0": ")",
        "10": "*",
        "11": "+",
        "13": ",",
    }


def test_sequencer_csv():
    test_df_1 = pd.DataFrame(
        {
            "id": pd.Series(["1_1", "1_2", "1_3", "2_1", "2_2", "2_3"], dtype="str"),
            "seq": pd.Series(["#$$", "$%&", "'((", "))*", "*+#", "#$$"], dtype="str"),
            "len": pd.Series([3, 3, 3, 3, 3, 3], dtype="int"),
        }
    )
    res = sequencer(
        files("tests.data.simple")._paths[0],
        id_col="subj",
        sep_col="trial",
        aoi_col="aoi",
    )
    pd.testing.assert_frame_equal(test_df_1, res)
