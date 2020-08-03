# -*- dcoding: utf-8 -*-
"""
Created on Sat Feb  1 10:42:20 2020

@author: cursobcrp
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Asian Option

# Put Option
s = 100
n = 180
m = 100
T = 0.5
r = 0.02
sigma = 0.5
K = 100
dt = T/n
S = np.zeros((n, m))
S[0]= s
np.random.seed(123)
z = np.random.randn(n, m)
for i in range(n-1):
    S[i + 1] = S[i]*np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z[i])
plt.plot(S)
A = np.mean(S, axis=0)
payoff = np.maximum(K - A, 0)
payoff
price = np.mean(np.exp(-r*T)*payoff)
price
se= np.sqrt(np.var(np.exp(-r*T)*payoff, ddof=1)/m)
se
print('price:{:.4f}, se:{:.4f}'.format(price, se))


# Call Option
s = 100
n = 180
m = 100
T = 0.5
r = 0.02
sigma = 0.5
K = 100
dt = T/n
S = np.zeros((n, m))
S[0]= s
np.random.seed(123)
z = np.random.randn(n, m)
for i in range(n-1):
    S[i + 1] = S[i]*np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z[i])
plt.plot(S)
A = np.mean(S, axis=0)
payoff = np.maximum(A - K, 0)
payoff
price = np.mean(np.exp(-r*T)*payoff)
price
se= np.sqrt(np.var(np.exp(-r*T)*payoff, ddof=1)/m)
se
print('price:{:.4f}, se:{:.4f}'.format(price, se))

