#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 09:43:21 2018

@author: jesus
"""

import numpy as np

# Simple recursion
def recursive_call(steps):
    # binomial tree parameters
    N = steps          # number of divisions or steps    
    R = np.exp(r*T/N)
    u = np.exp(sigma*np.sqrt(T/N))
    p = (R - 1/u)/(u - 1/u)
    # recursive pricing    
    def call(j, i):
        if j == N:
            return max(0, S*u**i - K)
        else:
            return ((p*call(j + 1, i + 1) + (1 - p)*call(j + 1, i - 1))/R)
        
    return call(0, 0)

if __name__ == "__main__":
    # underlying and market parameters
    r = 0.08
    sigma = 0.3
    S = 60
    # option parameters
    T = 0.5
    K = 50
    # tree parameters
    n = 30
    print(recursive_call(n))