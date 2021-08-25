# -*- coding: utf-8 -*-

import itertools
import numpy as np

DNAelements = 'ACGT'
RNAelements = 'ACGU'
proteinElements = 'ACDEFGHIKLMNPQRSTVWY'

def sequenceType(seqType):
    if seqType == 'DNA':
        elements = DNAelements
    else:
        if seqType == 'RNA':
            elements = RNAelements
        else:
            if seqType == 'PROTEIN' or seqType == 'PROT':
                elements = proteinElements
            else:
                elements = None

    return elements


trackingFeatures = []

def gF(args, X, Y):

    elements = sequenceType(args.sequenceType.upper())

    m3 = list(itertools.product(elements, repeat=3))


    T = []  # All instance ...

    def kmers(seq, k):
        v = []
        for i in range(len(seq) - k + 1):
            v.append(seq[i:i + k])
        return v     
    
    ### --- ###

    def monoDiKGap(x, g):  # 1___2

        m = m3
        for i in range(1, g + 1, 1):
            V = kmers(x, i + 3)
            # seqLength = len(x) - (i+2) + 1
            # print(V)
            for gGap in m:
                # print(gGap[0], end='')
                # print('-' * i, end='')
                # print(gGap[1], end='')
                # print(gGap[2], end=' ')
                # trackingFeatures.append(gGap[0] + '-' * i + gGap[1] + gGap[2])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[-2] == gGap[1] and v[-1] == gGap[2]:
                        C += 1
                # print(C, end=',')
                t.append(C)

     
        ### --- ###

    def generateFeatures(kGap, kTuple, x, y):

        if args.monoDi == 1:
            monoDiKGap(x, kGap)        #4*k*(4^2) = 960
            
        ##############################################################

        t.append(y)
        #######################


    for x, y in zip(X, Y):
        t = []
        generateFeatures(args.kGap, args.kTuple, x, y)
        T.append(t)
        ### --- ###

    ############################

    return np.array(T)


