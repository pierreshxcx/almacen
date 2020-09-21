import numpy as np

# Recursion with memoization

# Helper function
def memoize(f):
    memo = {}
    def helper(*args):
        if args not in memo:            
            memo[args] = f(*args)
        return memo[args]
    return helper

# Option pricing function
def recursive_call_with_memo(n):
    # binomial tree parameters
    N = n          # number of divisions or steps    
    R = np.exp(r*T/N)
    u = np.exp(sigma*np.sqrt(T/N))
    p = (R - 1/u)/(u - 1/u)
    # recursive pricing    
    @memoize
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
    n = 650 
    print(recursive_call_with_memo(n))
