import numpy as np
import matplotlib.pyplot as plt

def faster_lattice_american_put(r, sigma, S, T, K, n):
    dt = T/n
    R = np.exp(r*dt)
    u = np.exp(sigma*np.sqrt(dt))
    d = 1/u
    pu = (R - d)/(u - d)
    pd = 1 - pu
    
    stock_values = np.zeros(2*n + 1)
    
    stock_values[0] = S*d**n
    for i in range(1, 2*n + 1):
        stock_values[i] = stock_values[i - 1]*u
        
    option_values = np.maximum(0, K - stock_values)
    
    for j in reversed(range(n)):
        for i in range(n - j, j + n + 1, 2):
            continuation_value = (pu*option_values[i + 1] + pd*option_values[i - 1])/R
            early_exercise = K - stock_values[i]
            option_values[i] = max(early_exercise, continuation_value)
            
    return option_values[n]


if __name__ == "__main__":
    # underlying and market parameters
    r = 0.08
    sigma = 0.3
    S = 60
    # option parameters
    T = 0.5
    K = 60
    n = 500
    print(faster_lattice_american_put(r, sigma, S, T, K, n))
    
    size = 100
    binomial_lattice = np.zeros(size)
    richardson_extrapolation = np.zeros(size)
    for i in range(size):
        n = 10*(i + 1)
        binomial_lattice[i] = faster_lattice_american_put(r, sigma, S, T, K, n)
        n = 5*(i + 1)
        price = faster_lattice_american_put(r, sigma, S, T, K, n)
        richardson_extrapolation[i] = 2*binomial_lattice[i] - price
  
    steps = np.arange(6, size*6 + 1, 6)
    plt.plot(steps, binomial_lattice,
             steps, richardson_extrapolation)
#    
#    print("Put price by lattice using {} divisions: {:4f}".format(n, c))    
#    print("-"*50)
