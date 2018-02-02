#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 10:44:44 2017

@author: dawei414
"""
from Big2Hand import *

#def cpuPlay(turn, curr_htype, curr_score, curr_hand, player_hand):
#    ## show current board state
#    showState(turn, curr_htype, curr_score, curr_hand, player_hand)
#    ## play hand
#    play = True
#    state = "next"
#    print("Player " + str(turn + 1) + ": Play a hand, 'p' for pass: ")

def play_best(dic):
    h_type = ["straight flush", "four of a kind", "full house", "flush", "straight",
              "triple", "pair", "single"]
    for nxt_type in h_type:
        if len(dic.get(nxt_type)) != 0:
            the_type = dic.get(nxt_type)
            break
    if len(the_type) == 1:
        return the_type[0][0]
    else:
        score = [float(e[1]) for e in the_type]
        return the_type[score.index(max(score))]

def find_pairs(b2h):
    """ in a given hand 'b2h', find all the pairs, with the score """
    if len(b2h) <= 1:
        return []
    else:
        b2h.sort()
        pair = []
        for i in range(len(b2h)-1):
            j = i + 1
            while j < len(b2h):
                if b2h[i].get_faceval() == b2h[j].get_faceval():
                    pair.append(b2h[i].show() + ' ' + b2h[j].show())
                j += 1
#    return [(hand, str_to_b2hand(hand).get_hand_score()) for hand in pair]
    return pair

def find_triple(b2h):
    if len(b2h) <= 2:
        return []
    else:
        b2h.sort()
        triple = []
        for i in range(len(b2h)-2):
            if (b2h[i].get_faceval() + b2h[i+1].get_faceval() + b2h[i+2].get_faceval()) / 3 == b2h[i].get_faceval():
                triple.append(b2h[i].show() + ' ' + b2h[i+1].show() + ' ' + b2h[i+2].show())
    return triple

def find_straight(b2h):
    b2h.sort()
    b2h.reverse()
    st = [b2h[0]]
    for i in range(len(b2h)):
        if abs(st[-1].get_val() - b2h[i].get_val()) == 1:
            st.append(b2h[i])
    stra = []
    for e in st:
        stra.append(e.show())
            
    if len(stra) < 5:
        return []
    elif len(stra) == 5:
        return [' '.join(stra)]
    else:
        if len(stra) > 5:
            res = []
            for i in range(len(stra)-4):
                res.append(stra[i:i+5])
        return [' '.join(e) for e in res]

def find_flush(b2h):
    if len(b2h) < 5:
        return []
    else:
        strip_suit = []
        for card in b2h:
            strip_suit.append(card.get_suit())
    suits = []
    for char in strip_suit:
        if strip_suit.count(char) >= 5:
            suits.append(char) if char not in suits else None
    if len(suits) == 0:
        return []
    res = []
    for char in suits:
        flush = []
        for card in b2h:
            if card.get_suit() == char:
                flush.append(card.show())
        if len(flush) > 5:
            flush = expand(flush)
            for elt in flush:
                res.append(' '.join(elt))
        else:
            res.append(' '.join(flush))
    return res

def find_four(b2h):
    if len(b2h) <= 3:
        return []
    else:
        b2h.sort()
        four = []
        for i in range(len(b2h)-3):
            if (b2h[i].get_faceval() + b2h[i+1].get_faceval() + b2h[i+2].get_faceval() + b2h[i+3].get_faceval()) / 4 == b2h[i].get_faceval():
                four.append(b2h[i].show() + ' ' + b2h[i+1].show() + ' ' + b2h[i+2].show() + ' ' + b2h[i+3].show())
    return four

def find_fullhouse(b2h):
    pair = find_pairs(b2h)
    trips = find_triple(b2h)
    full = []
    for three in trips:
        for two in pair:
            if three[0] != two[0]:
                full.append(three + ' ' + two)
    return full

def find_strflsh(b2h):
    fl = find_flush(b2h)
    sf = []
    if len(fl) == 0:
        return sf
    else:
        for i in range(len(fl)):
            nums = sorted([int(e[:-1]) for e in fl[i].split()])
            if (nums[-1] + nums[-2]) - (nums[0] + nums[1]) == 6:
                sf.append(fl[i])
        return sf
    
def expand(f_list):
    res = []
    for i in range(len(f_list) - 4):
        res.append(f_list[i:i+5])
    return res


def all_hands(p_hand):
    all_dic = {}
    
    pair_d = find_pairs(p_hand)
    all_dic["pair"] = [(hand, str_to_b2hand(hand).get_hand_score()) for hand in pair_d]
    
    trips_d = find_triple(p_hand)
    all_dic["triple"] = [(hand, str_to_b2hand(hand).get_hand_score()) for hand in trips_d]
    
    str_d = find_straight(p_hand)
    all_dic["straight"] = [(hand, str_to_b2hand(hand).get_hand_score()) for hand in str_d]
    
    flu_d = find_flush(p_hand)
    all_dic["flush"] = [(hand, str_to_b2hand(hand).get_hand_score()) for hand in flu_d]
    
    full_d = find_fullhouse(p_hand)
    all_dic["full house"] = [(hand, str_to_b2hand(hand).get_hand_score()) for hand in full_d]
    
    stfl_d = find_strflsh(p_hand)
    all_dic["straight flush"] = [(hand, str_to_b2hand(hand).get_hand_score()) for hand in stfl_d]

    four = find_four(p_hand)
        
    a = set([card.show() for card in p_hand])
    b = set(' '.join(pair_d + trips_d + str_d + flu_d + full_d + four + stfl_d).split())
    c = list(a-b)
    print(c)
    
    four_d = []
    if len(four) > 0:
        for f in four:
            for e in c:
                print(1)
                four_d.append(f + " " + e)
        
            
    all_dic["four of a kind"] = [(hand, str_to_b2hand(hand).get_hand_score()) for hand in four_d]
    
    all_dic["single"] = [(hand, str_to_b2hand(hand).get_hand_score()) for hand in c]
    
    return all_dic
                