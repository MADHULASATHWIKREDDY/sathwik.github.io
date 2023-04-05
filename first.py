"""
Python module for solving the Convex Cover problem
"""

import numpy as np

def find_convex_cover(pvertices: np.ndarray, clist: list) -> list:
    """
    Computes the minimum sum of circles given their centres and the vertices
    of a polygon.

    Parameters
    ----------
    pvertices: np.ndarray
        The vertices of the polygon
    clist: list
        The list of centres of the circle
    """
    assert isinstance(pvertices, np.ndarray) and isinstance(clist, list)
    assert pvertices.shape[1] == 2 and all([len(v) == 2 for v in clist])

    carray: np.ndarray = np.array(clist)
    x_dist: np.ndarray = pvertices[:,0,None] - carray[:,0].T
    y_dist: np.ndarray = pvertices[:,1,None] - carray[:,1].T
    dist: np.ndarray = np.sqrt(np.square(x_dist) + np.square(y_dist))

    j: np.ndarray = np.argmin(dist, axis=1)
    i: np.ndarray = np.array(range(len(j)))
    ans: np.ndarray = np.zeros(dist.shape)
    ans[i, j] = dist[i, j]
    result: list = np.max(ans, axis=0).tolist()
    return result
