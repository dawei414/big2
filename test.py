#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:12:02 2017

@author: dawei414
"""
from Big2Hand import *
from cpuplay import *

## Create new deck, shuffle, and deal 4 hands of 13 cards
d1 = Deck()
d1.shuffle()
h1 = Big2Hand(d1.deal(13))
h2 = Big2Hand(d1.deal(13))
h3 = Big2Hand(d1.deal(13))
h4 = Big2Hand(d1.deal(13))

## display the 4 hands
h1.sort()
h2.sort()
h3.sort()
h4.sort()

print("Hand 1: ", end = '')
h1.show()
print("Hand 2: ", end = '')
h2.show()
print("Hand 3: ", end = '')
h3.show()
print("Hand 4: ", end = '')
h4.show()


# test pairs
p1 = find_pairs(h1)
p2 = find_pairs(h2)
p3 = find_pairs(h3)
p4 = find_pairs(h4)

print(p1)
print(p2)
print(p3)
print(p4)

# test triple
t1 = find_triple(h1)
t2 = find_triple(h2)
t3 = find_triple(h3)
t4 = find_triple(h4)

# test flush
f1 = find_flush(h1)
f2 = find_flush(h2)
f3 = find_flush(h3)
f4 = find_flush(h4)
        
#test straight
st1 = find_straight(h1)
st2 = find_straight(h2)
st3 = find_straight(h3)
st4 = find_straight(h4)

# test four of kind
    
fo1 = find_four(h1)
fo2 = find_four(h2)
fo3 = find_four(h3)
fo4 = find_four(h4)
#print('yo',fo1)
#print()
#print('yo1',fo2)
#print()
#print('yo2',fo3)
#print()
#print('yo3',fo4)

# test full house
fh1 = find_fullhouse(h1)
fh2 = find_fullhouse(h2)
fh3 = find_fullhouse(h3)
fh4 = find_fullhouse(h4)

# test all hands 
#all1 = all_hands(h1)
#all2 = all_hands(h2)
#all3 = all_hands(h3)
#all4 = all_hands(h4)

#print(all1)
#print()
#print(all2)
#print()
#print(all3)
#print()
#print(all4)
