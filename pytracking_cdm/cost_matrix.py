import numpy as np


def gen_costs(dim: int, dct: dict, code_dct: dict = None):
    if dim == 1:
        costs = np.ones(128, dtype=np.float64)
        if dct is None:
            return costs
        for key, value in dct.items():
            if code_dct is None:
                costs[ord(key)] = value
            else:
                costs[ord(code_dct[key])] = value
        return costs
    elif dim == 2:
        costs = np.ones((128, 128), dtype=np.float64)
        if dct is None:
            return costs
        for key, value in dct.items():
            for key2, value2 in value.items():
                if code_dct is None:
                    costs[ord(key), ord(key2)] = value2
                else:
                    costs[ord(code_dct[key]), ord(code_dct[key2])] = value2
    return costs
