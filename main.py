#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:04:34 2017

@author: dawei414
"""
from Big2Hand import *
from cpuplay import *


LINE = "=" * 30


def title(message):
    print(LINE)
    print(message)
    print(LINE)
    print()

def showState(turn, curr_htype, curr_score, curr_hand, player_hand):
    print(LINE)
    print("On the table: " + curr_htype)
    print("Played hand score: " + str(curr_score))
    print("Played hand: ", end = "")
    curr_hand.sort()
    curr_hand.show()
    print(LINE)
    print("Player " + str(turn + 1) + "'s hand: ", end = "")
    player_hand.sort()
    player_hand.show()
    
def playHand(turn, curr_htype, curr_score, curr_hand, player_hand):
    ## show current board state
    showState(turn, curr_htype, curr_score, curr_hand, player_hand)
    ## play hand
    play = True
    state = "next"
    while play:
        ## Check for valid input first
        valid_input = False
        while not valid_input:
            hand_str = input("Player " + str(turn + 1) + ": Play a hand, 'p' for pass or 'q' for quit: ")
            if len(hand_str) == 1:
                if hand_str == 'p':
                    if curr_htype != "none":
                        print()
                        print("Skiping to next player...")
                        turn += 1
                        remHand = player_hand
                        played = curr_hand
                        state = "pass"
                        return [turn, state, curr_htype, curr_score, played, remHand]
                    elif curr_htype == "none":
                        print()
                        print("Cannot pass when the table is empty!")
                if hand_str == 'q':
                    ans = ''
                    while ans not in ['y', 'n']:
                        ans = input("Are you sure? (y/n): ").lower()
                    if ans == 'y':
                        remHand = player_hand
                        played = curr_hand
                        state = "quit"
                        return [turn, state, curr_htype, curr_score, played, remHand]
                    else:
                        continue
                else:
                    print()
                    print("Err(07): Not a valid input!")
            else:
                try:
                    played = str_to_b2hand(hand_str)
                except ValueError:
                    print()
                    print("Err(15): Invalid input!")
                    continue
                if player_hand.is_valid_hand(played):
                    if played.get_type() != curr_htype and curr_htype != "none":
                        print()
                        print("Err(14): Need to Play a {0}.".format(curr_htype))
                        continue
                    if played.get_hand_score() < curr_score:
                        print()
                        print("Err(07): Cannot beat current played Hand!")
                        continue
                    else:
                        valid_input = True
                else:
                    print()
                    print("Err(20): Not valid!")
        ## Update variables and return played hand              
        turn += 1
        remHand = player_hand.update_hand(played)
        curr_htype = played.get_type()
        curr_score = played.get_hand_score()
        if remHand.size() == 0:
            state = "won"
            print("Congrats! Player " + str(turn) + " WINS!")
        play = False
    return [turn, state, curr_htype, curr_score, played, remHand]
                           
def playGame():
    title("Welcome to Big 2!")
    user_input = ''
    while user_input != 'x':
        user_input = input("Press 's' to start a new game, 'c' for CPU, 'x' to quit: ").lower()
        if user_input == 's':
            # Initiate new deck and shuffle cards
            the_deck = Deck()
            the_deck.shuffle()
            # deal 4 hands
            the_hands = []
            p1 = Big2Hand(the_deck.deal(13))
            p2 = Big2Hand(the_deck.deal(13))
            p3 = Big2Hand(the_deck.deal(13))
            p4 = Big2Hand(the_deck.deal(13))
            the_hands = [p1, p2, p3, p4]
            turn, passed, curr_score = 0, 0, 0
            curr_hand = Big2Hand([])
            curr_htype = "none"
            state = "start"
            while state not in ["won", "quit"]:
                if turn > 3:
                    print("Turn reset to 0")
                    turn = 0
                if state == "next":
                    print("reset pass counter")
                    passed = 0
                if state == "pass":
                    passed += 1
                if passed == 3:
                    passed = 0
                    curr_score = 0
                    curr_hand = Big2Hand([])
                    curr_htype = "none"
                now_hand = the_hands[turn]
                [turn, state, curr_htype, curr_score, curr_hand, remHand] = playHand(turn, curr_htype, curr_score, curr_hand, now_hand)
                the_hands[turn - 1] = remHand
        
#        elif user_input == 'c':
#            the_deck = Deck()
#            the_deck.shuffle()
#            the_hands = []
#            p1 = Big2Hand(the_deck.deal(13))
#            P2 = Big2Hand(the_deck.deal(13))
#            p3 = Big2Hand(the_deck.deal(13))
#            p4 = Big2Hand(the_deck.deal(13))
#            the_hands = [p1, p2, p3, p4]
#            turn, passed, curr_score = 0, 0, 0
#            curr_hand = Big2Hand([])
#            curr_htype = "none"
#            state = "start"
#            while state != "won":
#                if turn > 3:
#                    turn = 0
#                if state == "next":
#                    passed = 0
#                if state == "pass":
#                    passed += 1
#                if passed == 3:
#                    passed = 0
#                    curr_score = 0
#                    curr_hand = Big2Hand([])
#                    curr_htype = "none"
#                now_hand = the_hands[turn]
#                [turn, state, curr_htype, curr_score, curr_hand, remHand] = cpuPlay(turn, curr_htype, curr_score, curr_hand, now_hand)
#                the_hands[turn - 1] = remHand

        elif user_input == 'x':
            ans = ''
            while ans not in ['y', 'n']:
                ans = input("Are you sure? (y/n): ").lower()
            if ans == 'y':
                break
            else:
                user_input = ''
        else:
            print("Invalid Command")
            print()
                
playGame()
