#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round"""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


"""Create a player subclass that plays randomly"""


class Random_Player(Player):
    def move(self):
        return(random.choice(moves))


"""Create a subclass for a human player"""
"""Validate user input"""


class Human_Player(Player):
    def move(self):
        while True:
            Human_Input = input("Rock, Paper or Scissors? ")
            if Human_Input.lower() not in moves:
                print("Invalid input. Please choose Rock, Paper or Scissors")
            else:
                # print(f"You played {Human_Input}")
                return(Human_Input.lower())


"""Create player classes that remember"""


class ReflectPlayer(Player):
    def move(self, my_move, their_move):
        if their_move == "paper":
            return "paper"
        elif their_move == "scissors":
            return "scissors"
        else:
            return "rock"


class CyclePlayer(Player):
    def move(self, my_move, their_move):
        if my_move == "rock":
            return "paper"
        elif my_move == "paper":
            return "scissors"
        else:
            return "rock"


"""Create Game class and methods"""
"""Keep score"""
"""Number of rounds"""
"""Announce the winner"""


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # global p1s, p2s
        self.p1s = 0
        self.p2s = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You: {move1}  Computer: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2) is True:
                self.p1s += 1
                print("You won this round")
        elif beats(move2, move1) is True:
                self.p2s += 1
                print("Computer won this round")
        elif move1 == move2:
                print("Draw!")
        print(self.p1s, self.p2s)

    def play_game(self):
        print("Game start!")
        rounds = int(input("How many rounds you want to play? "))
        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()
        print(f"The score is {self.p1s} to {self.p2s}")
        if self.p1s > self.p2s:
            print("You won, Nice!")
        elif self.p1s < self.p2s:
            print("You lost!")
        else:
            print("It's a Tie!")


if __name__ == '__main__':
    game = Game(Human_Player(), Random_Player())
    game.play_game()
