'''helper mathematical functions'''

import fractions
import functools

import numpy as np


def gcd(a, b):
    '''Return greatest common divisor.'''
    # pylint: disable=deprecated-method
    return fractions.gcd(a, b)


def lcm(a, b):
    '''Return lowest common multiple.'''
    return a * b // gcd(a, b)


# TODO consider making this a np ufunc
def lcmm(args):
    '''Return lcm of args.'''
    return functools.reduce(lcm, args)


def minimum_aabb(mask):
    '''calculate the minimum axis-aligned bounding box for a volume mask

    Returns:
        A tuple containing the minimum x,y,z and maximum x,y,z
    '''
    idx = np.nonzero(mask)
    return np.min(idx, axis=1), np.max(idx, axis=1)


def positions_minimum_aabb(positions):
    '''calculate the minimum axis-aligned bounding box for a list of positions

    Returns:
        A tuple containing the minimum x,y,z and maximum x,y,z
    '''
    return np.min(positions, axis=0), np.max(positions, axis=0)


def clip(mask, aabb):
    '''take a numpy array and clip it to an axis-aligned bounding box

    Args:
        mask: numpy array
        aabb: tuple of two sets of coordinates indicating, respectively,
            the lowest and highest values for each dimension

    Returns:
        A new numpy array containing the same values as mask for the space defined by aabb
    '''
    idx = [slice(s, e + 1) for s, e in zip(*aabb)]
    return mask[idx].copy()


def is_diagonal(matrix):
    """ Check if the matrix is diagonal. """
    return np.all(matrix == np.diag(matrix.diagonal()))
