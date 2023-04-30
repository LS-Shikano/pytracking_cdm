import os
import pandas as pd
import numpy as np
from itertools import combinations
from scipy.spatial.distance import pdist, squareform
from datetime import datetime
from pytracking_cdm.sequencer import sequencer
from Levenshtein import distance,jaro,jaro_winkler



# https://stackoverflow.com/questions/46452724/string-distance-matrix-in-python-using-pdist
# arr = np.array(lst).reshape(-1,1)
# Y = pdist(arr, lambda x,y: nltk.edit_distance(x[0],y[0])) WAY SLOWER

# https://maxbachmann.github.io/Levenshtein/levenshtein.html#distance

def distance_matrix(df,metric="distance", div_len=False):
    '''

    @param df:
    dataframe containing one sequence per row
    @param metric:
    one of "distance","jaro" or "jaro_winkler"
    @param div_len:
    if True, divide distance by length of longer sequence
    @return:
    '''
    lst = df.seq.values.tolist()
    # print("avg len of sequences:", df['len'].mean())
    t1 = datetime.now()
    # print("starting distance matrix calculation", t1.strftime("%H:%M:%S"))
    # will divide by length of longer sequence
    # print(f"{metric}(i, j)")
    if div_len:
        distances = [eval(f"{metric}(i, j)")/max(len(i),len(j)) for (i, j) in combinations(lst, 2)]
    else:
        distances = [eval(f"{metric}(i, j)") for (i, j) in combinations(lst, 2)]
    t2 = datetime.now()
    delta = t2-t1
    # print("done", t2.strftime("%H:%M:%S"), f"\n took {delta.total_seconds()} seconds ")
    distance_matrix = squareform(distances)
    return distance_matrix


# seqs = sequencer(level=2,
#           folder=f"Data/Labelled_Data/Individual_Ballots/Double/Fixations/AOI_Fixations/30ms")
#
# calc_dist_matr(seqs)

