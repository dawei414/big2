#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:32:05 2017

@author: dawei414
"""
from Cards import *

def str_to_b2hand(h_string):
    to_play = h_string.split()
    tp = [Card(card) for card in to_play]
    return Big2Hand(tp)
         
class Hand(object):

    def __init__(self, c_list):
        self.hand = c_list

    def __iter__(self):
        return iter(self.hand)

    def __len__(self):
        return len(self.hand)
    
    def __getitem__(self, i):
        return self.hand[i]

    def show(self):
        for card in self.hand:
            print("[" + card.show(), end = "]")
        print()

    def size(self):
        return len(self.hand)

    def sort(self):
        for i in range(len(self.hand) - 1):
            j = i + 1
            while j < len(self.hand):
                if self.hand[i] < self.hand[j]:
                    self.hand[i], self.hand[j] = self.hand[j], self.hand[i]
                j += 1

    def reverse(self):
        self.hand = self.hand[::-1]

    def min_card(self):
        if self.size() > 0:
            temp = self.hand[:]
            temp.sort()
            return temp[0]
        else:
            return None

    def max_card(self):
        if self.size() > 0:
            temp = self.hand[:]
            temp.sort()
            return temp[-1]
        else:
            return None
    
    def copy(self):
        return Hand(self.hand)

class Big2Hand(Hand):

    def __init__(self, h_list):
        super().__init__(h_list)
        self.hand_type = self.set_hand_type()
        
    def set_hand_type(self):
        if self.size() == 1:
            return "single"
        elif self.size() == 2:
            return "pair" if self.is_pair() else "none"
        elif self.size() == 3:
            return "triple" if self.is_triple() else "none"
        else:
            five = {1: "straight", 2: "flush", 3: "full house", 4: "four of a kind", 5: "straight flush"}
            return five.get(self.type_of_five(), "none")

    def get_type(self):
        return self.hand_type

    def insert(self, card):
        if not card.is_in(self.hand):
            self.hand.append(card)
            self.hand_type = self.set_hand_type()
        else:
            raise ValueError("Err(05): Card already in hand")

    def discard(self, card):
        if card in self.hand:
            self.hand.remove(card)
            self.hand_type = self.set_hand_type()
        else:
            raise ValueError("Err(06): Card not in hand")

    def is_valid_hand(self, to_play):
        if to_play.size() > self.size():
            return False
        if all(e.is_in(self) for e in to_play):
            None
        else:
            return False
        return False if to_play.get_type() == "none" else True

    def update_hand(self, to_play):
        """ to_play is a Big2Hand Object
            returns itself with Cards in to_play removed """
        for card in to_play:
            self.discard(card)
        self.hand_type = self.set_hand_type()
        return self

    def get_hand_score(self):
        if self.get_type() == "none":
            return 0
        elif self.get_type() == "single":
            return self.hand[0].get_score()
        elif self.get_type() == "pair":
            ps = self.hand[0].get_score() + self.hand[1].get_score()
            return "{:.1f}".format(ps)
        elif self.get_type() == "triple":
            ts = self.hand[0].get_score() + self.hand[1].get_score() + self.hand[2].get_score()
            return "{:.1f}".format(ts)
        elif self.size() == 5:
            five = self.type_of_five()
            temp = self.hand[:]
            temp = sorted(temp)
            if self.get_type() == "full house" or self.get_type == "four of a kind":
                return temp[2].get_score() + (five * 100)
            else:
                return self.max_card().get_score() + (five * 100)
        
    def is_pair(self):
        if self.size() == 2:
            return self.hand[0].get_val() == self.hand[1].get_val()
        else:
            return False

    def is_triple(self):
        if self.size() == 3:
            return self.hand[0].get_val() == self.hand[1].get_val() and self.hand[0].get_val() == self.hand[2].get_val()
        else:
            return False

    def is_straight(self):
        if self.size() == 5:
            temp = self.hand[:]
            temp.sort()
            res = 0
            for i in range(4):
                if abs(temp[i].get_val() - temp[i + 1].get_val()) == 1:
                    res += 1
            return res == 4
        else:
            return False

    def is_flush(self):
        if self.size() == 5:
            res = 0
            for i in range(4):
                if self.hand[0].get_suit() == self.hand[i + 1].get_suit():
                    res += 1
            return res == 4
        else:
            return False

    def is_fullhouse(self):
        if self.size() == 5:
            temp = self.hand[:]
            temp.sort()
            temp_vals = [card.get_val() for card in temp]
            if temp_vals.count(temp_vals[0]) == 2 and temp_vals.count(temp_vals[4]) == 3:
                return True
            elif temp_vals.count(temp_vals[0]) == 3 and temp_vals.count(temp_vals[4]) == 2:
                return True
            else:
                return False
        else:
            return False

    def is_four_kind(self):
        if self.size() == 5:
            temp = self.hand[:]
            temp.sort()
            temp_vals = [card.get_val() for card in temp]
            if temp_vals.count(temp_vals[0]) == 1 and temp_vals.count(temp_vals[4]) == 4:
                return True
            elif temp_vals.count(temp_vals[0]) == 4 and temp_vals.count(temp_vals[4]) == 1:
                return True
            else:
                return False
        else:
            return False

    def type_of_five(self):
        if self.is_flush():
            return 5 if self.is_straight() else 2
        elif self.is_straight():
            return 1
        elif self.is_four_kind():
            return 4
        elif self.is_fullhouse():
            return 3
        else:
            return 0