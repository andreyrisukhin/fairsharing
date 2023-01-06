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
> (0,3,3): [[0,1,1],[0,0,0],[0,0,0]]  # Case when an underpayer needs to repay 2+ people
> (0,0,1,7): [[0,0,0,2],[0,0,0,2],[0,0,0,1],[0,0,0,0]] # Case when an underpayer already paid an amount
> () # Case when max payer is at front

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

    needs_to_pay = g - a # Positive: needs to pay that much, negative: overpayed by that much 

    print(f'DB a: {a}')
    print(f'DB g: {g}')
    print(f'DB diff: {needs_to_pay}')

    in_flux = a.copy()
    for ri, row in enumerate(result):
        if a[ri] < fairshare: # Only friends that underpaid need to realloc
            running_total_payout = 0 # Tracks 
            for ci, col_elem in enumerate(row): # compare with full row in case overpay was before
                diff = a[ri] - a[ci]

    """
    Logic
    For each    
    """

    # Return as 2d array? elements are how much each 
    pass 


in1 = [0,0,0,100]

unifSplit(np.ndarray(in1))