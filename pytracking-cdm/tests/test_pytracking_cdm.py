from importlib_resources import files, path
import pandas as pd
from pytracking_cdm import __version__
from pytracking_cdm.sequencer import sequence, sequencer


def test_version():
    assert __version__ == '0.1.0'


def test_sequence():
    csv = files('tests.data.single_test').joinpath('test.csv')
    df = pd.read_csv(csv)
    seq = sequence(df, "aoi")
    assert seq == "123456789"


def test_sequencer_csv():    
    res = sequencer(files('tests.data.jenke_et_al')._paths[0], id_col="subjid", sep_col="trialnums", aoi_col="et_rois")
    print(res)
