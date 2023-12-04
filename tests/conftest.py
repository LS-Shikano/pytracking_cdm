import pytest
import pandas as pd
import numpy as np
from importlib_resources import files


@pytest.fixture
def df_a():
    df_a = pd.DataFrame({"aoi": pd.Series([1, 2, 2, 2, 5, 6, 8, 8, 9], dtype="str")})
    return df_a

@pytest.fixture
def seq_a():
    return "122256889"


@pytest.fixture
def df_b():
    df_b = pd.DataFrame({"aoi": pd.Series([1, 2, 2, 2, 5, 6, 8, 8, 9], dtype="str")})
    return df_b


@pytest.fixture
def dct_b():
    return {"1": "!", "2": '"', "5": "#", "6": "$", "8": "%", "9": "&"}


@pytest.fixture
def df_b_2():
    df_b_2 = pd.DataFrame({"aoi": pd.Series([8, 8, 0, 0, 10, 11, 13, 1, 2], dtype="str")})
    return df_b_2


@pytest.fixture
def dct_b_2():
    return {
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


@pytest.fixture
def df_c():
    df_c = pd.DataFrame(
        {
            "id": pd.Series(["1_1", "1_2", "1_3", "2_1", "2_2", "2_3"], dtype="str"),
            "seq": pd.Series(['!""', '"#$', "%&&", "''(", "()!", '!""'], dtype="str"),
            "len": pd.Series([3, 3, 3, 3, 3, 3], dtype="int"),
        }
    )
    return df_c

@pytest.fixture
def path_c():
    return files("tests.data.simple.trial_sep")._paths[0]

@pytest.fixture
def arr_f():
    arr = [
        [0, 1, 2, 1],
        [1, 0, 2, 2],
        [2, 2, 0, 3],
        [1, 2, 3, 0],
    ]
    arr_f = np.array([np.array(xi) for xi in arr])
    return arr_f

@pytest.fixture
def df_f():
    df_f = pd.DataFrame(
        {
            "id": pd.Series(["1_1", "1_2", "1_3", "1_4"], dtype="str"),
            "seq": pd.Series(["abc", 'ab"c', 'abc""', '"bc'], dtype="str"),
            "len": pd.Series([3, 3, 3, 3], dtype="int"),
        }
    )
    return df_f
@pytest.fixture
def df_g():
    df_g = pd.DataFrame(
        {
            "id": pd.Series(["1", "2", "3", "4"], dtype="str"),
            "seq": pd.Series(['!!!"', '"!"#!', "!$%%&", '!!!"$'], dtype="str"),
            "len": pd.Series([4, 5, 5, 5], dtype="int"),
        }
    )
    return df_g

@pytest.fixture
def dct_g():
    dct_g = {
        "label_one": "!",
        "label_two": '"',
        "label_four": "#",
        "label_six": "$",
        "label_seven": "%",
        "label_nine": "&",
    }
    return dct_g

@pytest.fixture
def arr_g():
    arr = [
        [0, 4, 4, 1],
        [4, 0, 5, 4],
        [4, 5, 0, 4],
        [1, 4, 4, 0],
    ]
    arr_g = np.array([np.array(xi) for xi in arr])
    return arr_g

@pytest.fixture
def path_g():
    return files("tests.data.simple.ind")._paths[0]