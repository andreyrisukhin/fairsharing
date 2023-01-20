"""
Given array length n, each element representing the amount person i paid for trip.
Return the directions for who transfers how much money to whom, as if all paid equally for trip.
"""

import numpy as np

# Test format: list of (in, corrections). Assume uniform splits!
tests = [
    ([0,0,100,0], [[0,0,25,0],[0,0,25,0],[0,0,0,0],[0,0,25,0]]),
    ([0,10,0,30], [[0,0,0,10],[0,0,0,0],[0,0,0,10],[0,0,0,0]]),
    ([0,2], [[0,1],[0,0]]),
    ([1,2,3], [[0,0,1],[0,0,0],[0,0,0]]),
    ([0,3,3], [[0,1,1],[0,0,0],[0,0,0]]),
    ([0,0,1,7], [[0,0,0,2],[0,0,0,2],[0,0,0,1],[0,0,0,0]]),
    ([2,0], [[0,0],[1,0]])
]

"""
Examples:
> (0,0,100,0): [[0,0,25,0],[0,0,25,0],[0,0,0,0],[0,0,25,0]]
> (0,10,0,30): [[0,0,0,10],[0,0,0,0],[0,0,0,10],[0,0,0,0]]
> (0,2): [[0,1],[0,0]]
> (1,2,3): [[0,0,1],[0,0,0],[0,0,0]]
> (0,3,3): [[0,1,1],[0,0,0],[0,0,0]]  # Case when an underpayer needs to repay 2+ people
> (0,0,1,7): [[0,0,0,2],[0,0,0,2],[0,0,0,1],[0,0,0,0]] # Case when an underpayer already paid an amount
> (2,0): [[0,0],[1,0]] # Case when max payer is at front

Observations:
- Diagonal is zero
- later, maybe optimize to triangular matrix
- As if adding negatives to max payer to equalize payment
- Output should pass the assert that input + actions = output, and output has equal value elements
"""

"""
Takes actual array (n) and corrections (n,n)
    Interpret corrections c_ij as "friend i must pay friend j c_ij for fairness"
    Expect corrections to be positive.
Output resulting array.
=========
Used to validate solutions, actual + correction -> result, where uniform split result = all entries equal
"""
def applyPayments(actual:np.ndarray, correction:np.ndarray):
    n = np.shape(actual)[0]
    assert np.shape(correction) == (n,n), 'Mismatch correction instructions with actual payments.'
    result = actual.copy()
    for i, row in enumerate(correction):
        for j, c_ij in enumerate(row):
            if c_ij > 0:
                result[i] += c_ij
                result[j] -= c_ij
    # result is fair at this point; generally, result = actual + corrections    
    return result

'''
Uniformly splits the spending from actual to result, outputs corrections needed.
'''
def unifSplit(actual):
    # Prepare variables
    n = len(actual)
    correction = np.zeros((n,n))

    total_spent = sum(actual)
    fairshare = total_spent / n 
    goal = [fairshare for i in range(n)]
    g = np.array(goal)

    diff = g - actual # Positive: needs to pay that much, negative: overpayed by that much 

    print(f'DB a: {actual}')
    print(f'DB g: {g}')
    print(f'DB diff: {diff}')

    # Modifies diff
    for i, d_i in enumerate(diff):
        # while(d_i > 0): # Loop through needs to pay i
            # print(f'  DB i to be paid: {i}')
            # print(f'  DB diff: {diff}')
        if d_i > 0:
            for j, d_j in enumerate(diff): # TODO this should be entire array, in case need to pay is last
                if d_j < 0: # j is a hole to be filled
                    # Logic to see how much to fill vs how much is left
                    if abs(d_i) < abs(d_j): # Pit (dj) greater than amount (di)
                        diff[j] += d_i
                        correction[i][j] = d_i
                        diff[i] = 0
                    else: # Amount (di) fills pit (dj), maybe with leftover
                        pit_size = d_j
                        diff[i] -= -1*pit_size
                        correction[i][j] = -1*pit_size
                        diff[j] = 0

    print(f'DB diff: {diff}')
    print(f'DB corr: {correction}')

    return correction

    # # TODO ADD while to loop through needs to pay
    # for i, d_i in enumerate(diff):
    #     if d_i > 0: 
    #         to_realloc = d_i
    #         while(to_realloc > 0): # Loop through needs to be paid
    #             for j, d_j in enumerate(diff): # TODO this should be entire array, in case need to pay is last
    #                 if d_j < 0: # j is a hole to be filled
    #                     curr_pit = d_j
    #                     # Logic to see how much to fill vs how much is left
    #                     if to_realloc < curr_pit:
    #                         curr_pit += to_realloc
    #                         to_realloc = 0

            # Find where it should be reallocated



            # for j in range(i, n):
            #     if diff[j] < 0: # This is a spot that needs filling




    # Can fill underpayer's payment into first available overpayment hole, because this action always brings us closer to solution (converge)

    # for ri, row in enumerate(correction):
    #     if in_flux[ri] > 0: # Only friends that underpaid need to realloc
    #         for ci, col_elem in enumerate(row): # compare with full row in case overpay was before
    #             if in_flux[ci] < 0: # If needs to be paid
    #                 diff = in_flux[ci] + in_flux[ri]
    #                 # TODO add a control to ensure that if i owes more than j needs, i pays only what j needs
    #                 # TODO add a corollary control to ensure that if i owes less than j needs, i pays all to j

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

# Testing!
for in_i, corr_i in tests:
    pass 



# in1 = [0,0,0,100]

# corr1 = unifSplit(in1)
# out1 = applyPayments(in1, corr1)

# print(f'Out 1: {out1}')

# a_in = np.array([0,0,100,0])
# a_c = np.array([[0,0,25,0],[0,0,25,0],[0,0,0,0],[0,0,25,0]])
# a_out = applyPayments(actual=a_in, correction=a_c)
# print(f'initial payments: {a_in}, fair payments: {a_out}')
