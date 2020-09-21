#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 10:07:20 2018

@author: jesus
"""

import numpy as np
import matplotlib.pyplot as plt

def lattice_european_call(r, sigma, S, T, K, n):
    dt = T/n
    R = np.exp(r*dt)
    u = np.exp(sigma*np.sqrt(dt))
    d = 1/u
    p = (R - d)/(u - d)
    
    lattice = np.zeros((n + 1, n + 1))
    
    for i in range(n + 1):
        lattice[i, n] = max(0, S*u**i*d**(n - i) - K)
        
    for j in reversed(range(n)):
        for i in range(j + 1):
            lattice[i, j] = (p*lattice[i + 1, j + 1] + (1 - p)*lattice[i, j + 1])/R
            
    return lattice[0, 0]

if __name__ == "__main__":
    # underlying and market parameters
    r = 0.08
    sigma = 0.3
    S = 60
    # option parameters
    T = 0.5
    K = 50
    
    ns = list(range(50, 5001, 50))
    prices = []
    for n in ns:
        c = lattice_european_call(r, sigma, S, T, K, n)
        prices.append(c)
   
    plt.plot(ns, prices)
    
    print("Call price by lattice using {} divisions: {:4f}".format(n, c))
    print("-"*50)

