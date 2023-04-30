from importlib_resources import files
from pytracking_cdm import __version__
from pytracking_cdm.sequencer import sequence_csv,sequencer

def test_version():
    assert __version__ == '0.1.0'

def test_sequence_csv():
    csv = files('tests.data.jenke_et_al').joinpath('ind_9.csv')
    seq = sequence_csv(files('tests.data.jenke_et_al').joinpath('ind_9.csv'), "et_rois")
    print(seq)