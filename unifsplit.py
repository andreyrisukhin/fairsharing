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
    ([2,0], [[0,0],[1,0]]),
    ([1,2,3,4], [[0,0,0.5,1],[0,0,0,0.5],[0,0,0,0],[0,0,0,0]]),
    ([301.9,0,181.8,0], [[0,0,0,0],[120.925,0,0,0,],[0,0,0,0],[60.05,0,60.875,0]])
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
            # print(f'  {c_ij}')
            if c_ij > 0:
                result[i] += c_ij
                result[j] -= c_ij
    # result is fair at this point; generally, result = actual + corrections    
    return result

'''
Uniformly splits the spending from actual to result, outputs corrections needed.
'''
def unifSplit(actual:np.ndarray):
    # Prepare variables
    actual = np.array(actual, dtype=np.float64)
    n = np.size(actual) # len(actual)
    correction = np.zeros((n,n))
    total_spent = sum(actual)
    fairshare = total_spent / n 
    goal = [fairshare for i in range(n)]
    goal = np.array(goal)
    diff = goal - actual # Positive: needs to pay that much, negative: overpayed by that much 
    # Solving (Modifies diff)
    for i in range(len(diff)):
        # d_i = diff[i]
        if diff[i] > 0:
            for j in range(len(diff)): # TODO this should be entire array, in case need to pay is last
                if diff[j] < 0: # j is a hole to be filled
                    # Logic to see how much to fill vs how much is left
                    if abs(diff[i]) < abs(diff[j]): # Pit (dj) greater than amount (di)
                        diff[j] += diff[i]
                        correction[i][j] = diff[i]
                        diff[i] = 0
                    else: # Amount (di) fills pit (dj), maybe with leftover
                        pit_size = abs(diff[j])
                        diff[i] -= pit_size
                        correction[i][j] = pit_size
                        diff[j] = 0
                    # print(f'  {diff}')
    # TODO an assert to ensure it's fair distribution? remove future d_i vs diff[i], var vs ref issue?
    # Check that the correction results in the correct answer
    corr_out = applyPayments(actual=actual, correction=correction)
    assert np.allclose(goal, corr_out), f'Error: The calculated output {corr_out} did not result in the goal {goal}.'
    

    return correction

# Testing!
for in_true, corr_true in tests:
    in_true_np = np.array(in_true)
    corr_calc = unifSplit(in_true_np)
    assert np.allclose(corr_calc,corr_true), f"Test failed: expected corrections: {corr_true}, calculated: {corr_calc}"

# TODO take in an itemized list of transactions, and support deletion/removal of an item for a person?
# > For example, if a friend did not eat at all at a restaurant, the uniform split assumption is unfair

# Keep thinking; what is the fairest adjusted calculation of 1 of n friends doesn't participate in an activity?
