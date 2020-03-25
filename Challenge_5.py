"""
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].
"""

from fractions import Fraction
from math import gcd
from functools import reduce

def solution(m):
    def p_of_state(m, s):
        """
        Returns probability of reaching state s
        """
        # TODO modify to accomodate looping states
        if s == 0:
            return Fraction(1,1)

        # find all states that lead to state i
        paths = []
        for i in range(len(m)):
            if m[i][s] != 0:
                paths.append(i)
        # for each one, multiply that probability by p_of_state(m, parent)
        # add different paths together

        print(paths)

        p = 0

        for path in paths:
            p += Fraction(m[path][s],sum(m[path])) * p_of_state(m, path)
        
        return p
    
    def lcm(denominators):
        """
        Returns lowest common denominator from a list of ints
        """
        return reduce(lambda a,b: a*b // gcd(a,b), denominators)
    
    # TODO check that matrix is a square

    # find terminal states in m
    terminal_states = []
    for i in range(len(m)):
        terminal = True
        # checking if all probabilities in a state are 0 except the 
        # probability corresponding to the state itself
        # (a state that only goes to itself is still terminal)
        for j in range(len(m)):
            if m[i][j] != 0 and i!=j:
                terminal = False

        if terminal == True:
            terminal_states.append(i)

    f_solution = []
    denominators = []

    for state in terminal_states:
        f_solution.append(p_of_state(m, state))
        denominators.append(f_solution[-1].denominator)
    
    denominator = lcm(denominators)

    solution = []

    for f in f_solution:
        solution.append(int(f.numerator*denominator/f.denominator))
    
    solution.append(denominator)
    
    return solution