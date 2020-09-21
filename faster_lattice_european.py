#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:46:27 2018

@author: jesus
"""

import numpy as np
import matplotlib.pyplot as plt

def faster_lattice_european_call(r, sigma, S, T, K, n):
    dt = T/n
    R = np.exp(r*dt)
    u = np.exp(sigma*np.sqrt(dt))
    d = 1/u
    p = (R - d)/(u - d)
    
    S_values = np.zeros(2*n + 1)
    
    S_values[0] = S*d**n
    for i in range(1, 2*n + 1):
        S_values[i] = S_values[i - 1]*u
        
    V_values = np.maximum(0, S_values - K)
        
    for j in range(n):
        for i in range(j + 1, 2*n + 1 - j, 2):
            V_values[i] = (p*V_values[i + 1] + (1 - p)*V_values[i - 1])/R
            
    return V_values[n]


if __name__ == "__main__":
    # underlying and market parameters
    r = 0.08
    sigma = 0.3
    S = 60
    # option parameters
    T = 0.5
    K = 50
    
    ns = list(range(25, 2501, 25))
    prices = []
    for n in ns:
        c = faster_lattice_european_call(r, sigma, S, T, K, n)
        prices.append(c)
   
    plt.plot(ns, prices)
    
    print("Call price by lattice using {} divisions: {:4f}".format(n, c))    
    print("-"*50)