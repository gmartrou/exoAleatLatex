#!/usr/bin/python
# -*- coding: utf-8 -*-


def PGCD(N):
    A = N[:]
    if len(A) == 2:
        while A[0] % A[1] != 0:
            A[0], A[1] = A[1], (A[0] % A[1])
    else:
        a = A[0]
        del A[0]
        b = PGCD(A)
        return PGCD([a, b])
    return int(A[1])

def PPCM(N):
    A = N[:]
    if len(A) == 2:
        return int((A[0]*A[1])/PGCD(A))
    else:
        a = A[0]
        del A[0]
        b = PPCM(A)
        return int(PPCM([a, b]))
