#!/usr/bin/env python
"""module to conduct log of binomial coefficients"""

import argparse
import math
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="number of total individual")
parser.add_argument("-k", type=int, help="number of individual being chosen")
parser.add_argument("-l", "--log", action="store_true", help="to get the log of the binomial coefficient")
parser.add_argument("--test", action="store_true", help="tests the functions")
args = parser.parse_args()

if not args.test and __name__ == '__main__':
    if args.k<0:
        raise Exception("log(1)=0 if k>n, it’s a sum of 0 terms")

def logfactorial(n=args.n, k=args.k): 
    '''
    The function is used to calculate the log values of given n, k, and n-k.
    Examples:

    >>> logfactorial(5, 3)
    (4.787491742782046, 1.791759469228055)

    >>> logfactorial(5, 5)
    (4.787491742782046, 4.787491742782046)

    >>> logfactorial(5, 6)
    (4.787491742782046, 6.579251212010101)
    '''
    assert n >= 0.0, 'n should be equal or larger than zero'        
    assert k >= 0.0, 'k should be equal or larger than zero'

    norder = list(range(1, n+1))
    sumlogi = 0
    for i in norder:
        logi = math.log(i)
        sumlogi = sumlogi+logi
    
    korder = list(range(1, k+1))
    sumlogj = 0
    for j in korder:
        logj = math.log(j)
        sumlogj = sumlogj+logj

    return sumlogi, sumlogj

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)


def choose(n=args.n, k=args.k): 
    '''
    The function is used to calculate the log of binomial coefficients
    (log(choose(n, k))),the log value of finding all combinations to do n choose k.
    Examples:

    >>> choose(5, 3)
    10

    >>> choose(5, 5)
    1
    '''
    assert n >= 0.0, 'n should be equal or larger than zero'        
    assert k >= 0.0, 'k should be equal or larger than zero'
    assert n-k >= 0.0, 'log(1)=0 if k>n, it’s a sum of 0 terms'
    norder = list(range(1, n+1))
    sumlogi = 0
    for i in norder:
        logi = math.log(i)
        sumlogi = sumlogi+logi
    
    korder = list(range(1, k+1))
    sumlogj = 0
    for j in korder:
        logj = math.log(j)
        sumlogj = sumlogj+logj

    nminuskorder = list(range(1, n-k+1))
    sumlogm = 0
    for m in nminuskorder:
        logm = math.log(m)
        sumlogm = sumlogm+logm
    bicolog = sumlogi-sumlogj-sumlogm
    bico = int(round(math.exp(bicolog)))
    return bico

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)