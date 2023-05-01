from importlib_resources import files, path
import pandas as pd
from pytracking_cdm import __version__
from pytracking_cdm.sequencer import sequence, sequencer


def test_version():
    assert __version__ == '0.1.0'


def test_sequence_csv():
    csv = files('tests.data.jenke_et_al').joinpath('ind_9.csv')
    df = pd.read_csv(csv)
    seq = sequence(df, "et_rois")
    # print(seq)


def test_sequencer_csv():
    print(files('tests.data.jenke_et_al'))
    
    # res = sequencer(package_path, mult_seq=True, aoi_col="et_rois")
    # print(seq)
