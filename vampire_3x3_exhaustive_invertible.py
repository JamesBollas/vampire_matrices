# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:43:25 2020

@author: James
"""

import numpy as np

def ver(A):
    try:
        B = np.linalg.inv((np.eye(3) - np.linalg.inv(A))/10)
        return np.equal(np.mod(B, 1), 0).all() and (B<10).all() and (B>0).all()
    except:
        return False
i = 0
for a1 in range(1,10):
    for a2 in range(1,10):
        for a3 in range(1,10):
            for a4 in range(1,10):
                for a5 in range(1,10):
                    for a6 in range(1,10):
                        for a7 in range(1,10):
                            for a8 in range(1,10):
                                for a9 in range(1,10):
                                    i+=1
                                    if i % 100000 == 0:
                                        print(i)
                                    A = np.array([[a1,a2,a3],[a4,a5,a6],[a7,a8,a9]])
                                    if ver(A):
                                        print(A)
                                        print(np.linalg.inv((np.eye(3) - np.linalg.inv(A))/10))
                                        print(A.dot(np.linalg.inv((np.eye(3) - np.linalg.inv(A))/10)))
