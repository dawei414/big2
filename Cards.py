#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:29:01 2017

@author: dawei414
"""
import random

ACE_VAL = 14
DUCE_VAL = 15
SUIT = 'shcd'

class Card(object):

    def __init__(self, card):
        value, suit = int(card[:-1]), card[-1].lower()

        if suit not in SUIT:
            raise ValueError("Err(01): Not valid suit, --> ('s', 'h', 'c', 'd')")
        else:
            self.suit = suit

        if value == 1:
            self.val = ACE_VAL
        elif value == 2:
            self.val = DUCE_VAL
        else:
            self.val = value

        s_choice = {"s": 0.5, "h": 0.3, "c": 0.2, "d": 0.1}
        adder = s_choice.get(self.suit)
        self.score = self.val + adder

        self.faceval = value

    def __lt__(self, other):
        return self.get_score() < other.get_score()

    def __eq__(self, other):
        return self.get_score() == other.get_score()

    def __str__(self):
        num_name = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        val = num_name.get(self.get_faceval(), "other")
        if val == "other":
            val = self.get_faceval()
        s_name = {"s": "Spades", "h": "Hearts", "c": "Clubs", "d": "Diamonds"}
        suit = s_name.get(self.get_suit())
        return "[{0} of {1}]".format(val, suit)

    def get_val(self):
        return self.val

    def get_faceval(self):
        return self.faceval

    def get_suit(self):
        return self.suit

    def get_score(self):
        return self.score

    def is_in(self, hand):
        for card in hand:
            if card == self:
                return True
        return False
        
    def show(self):
        return "{0}{1}".format(self.faceval, self.suit)

class Deck(object):

    def __init__(self):
        self.deck = []
        for suit in SUIT:
            for val in range(1, 14):
                self.deck.append(Card(str(val) + suit))

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        dlist = []
        for card in self.deck:
            dlist.append(card.show())
        return str(dlist)

    def insert(self, card):
        if not card.is_in(self.deck):
            self.deck.append(card)
        else:
            raise ValueError("Err(02): Already in deck")

    def discard(self, card):
        try:
            self.deck.remove(card)
        except:
            raise ValueError("Err(03): " + str(card) + " not found")
        
    def get(self, pos):
        if pos > len(self) or pos == 0:
            raise IndexError("Err(04): Out of Range")
        else:
            return self.deck[pos - 1]

    def shuffle(self):
        s_deck = []
        while len(self.deck) > 1:
            rand = random.randint(1, len(self.deck))
            card = self.get(rand)
            s_deck.append(card)
            self.discard(card)
        s_deck.append(self.get(1))
        self.deck = s_deck[:]

    def deal(self, num):
        hand = []
        for _ in range(num):
            try:
                card = self.get(1)
                hand.append(card)
                self.discard(card)
            except IndexError:
                print("Cannot deal more cards than in the deck.")
        return hand