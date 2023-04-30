from pytracking_cdm.sequencer import sequencer
from pytracking_cdm.distance_matrix import distance_matrix

def process(level,merge=False,off_ballot=True,position=True,raw=False,metric="distance",div_len=False):
    """process: generates a sequence from eyetracking data and returns a distance matrix
    Params:
    ------
    level: the level of the sequence, 0 is the level of the first sequence, 1 is the level of the second sequence, etc.
    merge: if True, the result will be a list of lists, where each sublist is a sequence of beads that have been merged.
    off_ballot: if True, the first bead will be the off-ballot bead, and the second will be the on-ballot bead.
    position: if True, the first bead will be the position of the off-ballot bead, and the second will be the position of the on
    ballot.
    raw: if True, the result will be a list of lists, where each sublist is a sequence of beads.
    metric: the distance metric to use.
    div_len: if True, the result will be a list of lists of lists, where each sublist of lists is a sequence of beads with
    different bead lengths.
    
    Usage:
    ------
    >>> from pytracking_cdm import process
    >>> process(0,merge=True)
    """
    if level == 2:
        fix="AOI"
    else:
        fix="Row"
    df = sequencer(
        level=level,
        folder=f"../Data/Labelled_Data/Individual_Ballots/Double{'' if raw else f'/Fixations/{fix}_Fixations/30ms'}",
        merge=merge,
        off_ballot=off_ballot,
        position=position)

    return  distance_matrix(df=df,metric=metric,div_len=div_len)