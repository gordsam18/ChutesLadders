"""
Chutes and ladders game

Game board is 10x10 matrix snaking from 1 to 100

Ladders go up 
Chutes go down 

2 players roll a dice (1-6) to progress on the board.
When a player lands on a ladder they progress to the top of the ladder
When a player lands on a chute they regress to the begining of chute 
First player to the end (spot 100) wins 

Game asks if they want to restart 
"""
import tkinter as tk
import random


class Game:
    def __init__(self):
        self.board = self.createBoard()
        self.players = {1: "Player 1", 2: "Player 2"
            }
        
        self.playerPosition = {1: 0, 2: 0
            }
        
        self.chute = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladder = {1: 38,4: 14,9: 31,21: 42,28: 84,36: 44,51: 67,71: 91,80: 100}
    
        self.currentPlayer = 1
        self.row = 10
        self.col = 10
        self.boardEnd = self.row * self.col

    def createBoard(self):
        """
        10x10 matrix board
        snakes 1-100
        """
        row = 10
        col = 10 

        board = []
        count = 1
        switch = 0 
        for i in range(row):
            l = []
            for j in range(col):
                l.append(count)
                count += 1

        if switch % 2 == 0:
            l = l[::-1]
        
        switch += 1 
        
        board.append(l)
        return board

    def printBoard(self):
        """
        Printing and formatting the board for better readability
        """
        for row in self.board:
            print(''.join(f'{x:2}'for x in row))

    
        
    def diceRoll(self):
        """
        Rolls a 6 sided dice
        """
        return random.randint(1,6)

    def movePlayer(self, player, dice):
        """
        
        """
        currentPosition = self.playerPosition[player]
        newPosition = currentPosition + dice

        if newPosition > 100:
            return currentPosition
        
        if newPosition in self.chute:
            print("Went down a chute")
            newPosition = self.chute[newPosition]

        elif newPosition in self.ladder:
            print("Went up a ladder")
            newPosition = self.ladder[newPosition]

        return newPosition

    

    def play(self):
        while True:
            print(f"{self.players[self.currentPlayer]}'s turn. Please Roll\n")
            diceRoll = self.diceRoll()
            print(f"{self.players[self.currentPlayer]} rolled a {diceRoll}\n")
            newPosition = self.movePlayer(self.currentPlayer, diceRoll)
            self.playerPosition[self.currentPlayer] = newPosition
            print(f"{self.players[self.currentPlayer]} moved to {newPosition}\n")
            
            if newPosition == self.boardEnd:
                print(f"{self.players[self.currentPlayer]} wins!")
                return False
            
            
            if self.currentPlayer == 2:
                self.currentPlayer = 1
            else: 
                self.currentPlayer = 2  
    
if __name__ == "__main__":
    game = Game()
    game.play()