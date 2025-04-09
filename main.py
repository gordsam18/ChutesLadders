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

import random


class Game:
    def __init__(self):
        self.board = self.CreateBoard()
        self.players = {1: "Player 1", 2: "Player 2"}
        self.playerStartPosition = {1: 0, 2: 0}
        self.currentPlayer = 1

    def CreateBoard(self):
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
        
        board.append()
        return board

    def PrintBoard(self):
        pass
        
    def DiceRoll(self):
        return random.randint(1,6)

    def MovePlayer(self):
        pass

    def Play(self):
        pass

    
if __name__ == "__main__":
    game = Game()
    game.Play