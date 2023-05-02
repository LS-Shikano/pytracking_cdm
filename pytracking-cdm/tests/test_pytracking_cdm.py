from importlib_resources import files, path
import pandas as pd
from pytracking_cdm import __version__
from pytracking_cdm.sequencer import sequence, gen_code_dct, sequencer


def test_version():
    assert __version__ == '0.1.0'


def test_sequence():
    csv = files('tests.data.single_test').joinpath('test1.csv')
    df = pd.read_csv(csv)
    seq = sequence(df, "aoi")
    assert seq == "122256889"
    seq = sequence(df, "aoi", merge=True)
    assert seq == "125689"
    seq = sequence(df, "aoi", off_aoi_str="2")
    assert seq == "156889"

def test_gen_code_dct():
    csv1 = files('tests.data.single_test').joinpath('test1.csv')
    df = pd.read_csv(csv1)
    code_dct = gen_code_dct(df, "aoi", {})
    assert code_dct == {1:"#",2:"$",5:"%",6:"&",8:"'",9:"("}
    csv2 = files('tests.data.single_test').joinpath('test2.csv')
    df = pd.read_csv(csv2)
    code_dct = gen_code_dct(df, "aoi", code_dct)
    assert code_dct == {1:"#",2:"$",5:"%",6:"&",8:"'",9:"(", 0: ')', 10: '*', 11: '+', 13: ','}

def test_sequencer_csv():    
    res = sequencer(files('tests.data.jenke_et_al')._paths[0], id_col="subjid", sep_col="trialnums", aoi_col="et_rois")
    print(res)
