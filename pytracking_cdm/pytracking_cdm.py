from pytracking_cdm.sequencer import sequencer
from pytracking_cdm.distance_matrix import distance_matrix


def process(**kwargs):
    """process: generates a sequence from eyetracking data and returns a
    distance matrix
    Params:
    ------
    level: the level of the sequence, 0 is the level of the first sequence, 1 is the level of the second sequence, etc.
    merge: if True, the result will be a list of lists, where each sublist is
    a sequence of beads that have been merged.
    off_ballot: if True, the first bead will be the off-ballot bead, and the
    second will be the on-ballot bead.
    position: if True, the first bead will be the position of the off-ballot
    bead, and the second will be the position of the on
    ballot.
    raw: if True, the result will be a list of lists, where each sublist is a
    sequence of beads.
    metric: the distance metric to use.
    div_len: if True, the result will be a list of lists of lists, where each
    sublist of lists is a sequence of beads with
    different bead lengths.

    Usage:
    ------
    >>> from pytracking_cdm import process
    >>> process(0,merge=True)
    """
    return lambda x: distance_matrix(sequencer(x))
