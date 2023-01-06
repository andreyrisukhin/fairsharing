"""
Given array length n, each element representing the amount person i paid for trip.
Return the directions for who transfers how much money to whom, as if all paid equally for trip.
"""

import numpy as np

"""
Examples:
> (0,0,100,0): [[0,0,25,0],[0,0,25,0],[0,0,0,0],[0,0,25,0]]
> (0,10,0,30): [[0,0,0,10],[0,0,0,0],[0,0,0,10],[0,0,0,0]]
> (0,2): [[0,1],[0,0]]
> (1,2,3): [[0,0,1],[0,0,0],[0,0,0]]

Observations:
- Diagonal is zero
- later, maybe optimize to triangular matrix
- As if adding negatives to max payer to equalize payment
- Output should pass the assert that input + actions = output, and output has equal value elements
"""
def unifSplit(a:np.ndarray):
    # Prepare variables
    n = len(a)
    result = np.zeros((n,n))
    total_spent = sum(a)
    fairshare = total_spent / n 
    goal = [fairshare for i in range(n)]
    g = np.array(goal)

    for ri, row in enumerate(result):
        if a[ri] < fairshare: # Only for friends that underpaid need to realloc
            for ci, col_elem in enumerate(row):
                pass # TODO

    """
    Logic
    For each    
    """

    # Return as 2d array? elements are how much each 
    pass 