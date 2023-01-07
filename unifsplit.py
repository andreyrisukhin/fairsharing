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

"""
Takes actual array (n) and corrections (n,n)
Output resulting array
"""
def applyPayments(actual:np.ndarray, correction:np.ndarray):
    n = np.shape(actual)[0]
    assert np.shape(correction) == (n,n), 'Mismatch correction instructions with actual payments.'
    # TODO


def unifSplit(a):
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



    in_flux = needs_to_pay.copy()
    
    # Can fill underpayer's payment into first available overpayment hole, because this action always brings us closer to solution (converge)

    for ri, row in enumerate(result):
        if in_flux[ri] > 0: # Only friends that underpaid need to realloc
            for ci, col_elem in enumerate(row): # compare with full row in case overpay was before
                if in_flux[ci] < 0: # If needs to be paid
                    diff = in_flux[ci] + in_flux[ri]
                    # TODO add a control to ensure that if i owes more than j needs, i pays only what j needs
                    # TODO add a corollary control to ensure that if i owes less than j needs, i pays all to j

    # At this point, all differences should be equalized, no more differences between goal and payments + actual

    # for ri, row in enumerate(result):
    #     if a[ri] < fairshare: # Only friends that underpaid need to realloc
    #         running_total_payout = 0 # Tracks 
    #         for ci, col_elem in enumerate(row): # compare with full row in case overpay was before
    #             diff = a[ri] - a[ci]

    """
    Logic
    For each    
    """

    # Return as 2d array? elements are how much each 
    pass 


in1 = [0,0,0,100]

unifSplit(in1)