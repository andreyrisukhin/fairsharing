"""
Thue-Morse Sequence for two people (ABBA BAAB ...)
Thunk-style, generates next n tokens in the sequence upon prompt, at each prompt 
    can also exit.
"""

# Binary string, take complement and append, move pointer forward 1 by 1

''' Takes s containing 'A', 'B' and reverses them. '''
def complement(s:str):
    r = ''
    for c in s:
        if c == 'A':
            r += 'B'
        else: r += 'A'
    return r

def twoThueMorse(n:int=1):
    stillSelecting = True
    s = 'ABBA'
    i = 0
    j = n
    seq = ''
    while(stillSelecting):
        seq += s[i]
        i += 1
        j -= 1
        # Expand if needed
        if i >= len(s):
            s = s + complement(s)
        # Prompt if needed
        if j <= 0:
            print(seq)
            seq = ''
            response = input(f'Generate {n} more tokens? (y/n)\n')
            if response == 'y':
                j = n
            else: stillSelecting = False

twoThueMorse(4)        



