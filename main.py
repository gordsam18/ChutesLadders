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
# ui in progress 
import tkinter as tk
import random


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.game = True
        
        self.row = 10
        self.col = 10
        self.boardEnd = self.row * self.col
        self.chute = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladder = {1: 38,4: 14,9: 31,21: 42,28: 84,36: 44,51: 67,71: 91,80: 100}
        self.roll = 0

        self.players = {1: "Player 1", 2: "Player 2"}
        self.playerPosition = {1: 1, 2: 1}

        self.currentPlayer = 1

        self.board = self.createBoard()
        self.drawBoard(self.root)

        
        

    def createBoard(self):
        """
        10x10 matrix board
        snakes every 10 spots from 1-100 
        """
        rows = 10
        cols = 10
        counter = 100
        board = []
        


        for i in range(rows): 
            row = []
            for col in range(cols):
                row.append(counter)
                counter -= 1
            
            if i % 2 == 1:
                row.reverse()
                
            board.append(row)

        return board

    def drawBoard(self, root):
        """"
        Draws the board on the Tkinter window using Labels in a grid.
        """
        


        legend = {
            "Chute Start": "salmon",
            "Ladder Start": "lightblue",
            "Chute/Ladder End": "khaki",
            "Player Tile": "lightgreen"
        }

        for i, (name, color) in enumerate(legend.items()):
            tk.Label(root, text=name, bg=color, width=15).grid(row=11+i, column=0, columnspan=2, sticky="w", padx=5, pady=2)

        self.turnLabel = tk.Label(
        root,
        text=f"{self.players[self.currentPlayer]}'s turn. Please Roll\n")
        self.turnLabel.grid()

        self.resultLabel = tk.Label(
            root,
            text=f"{self.players[self.currentPlayer]}'s turn. Please Roll",
            font=("Arial", 12, "bold"),
            fg="darkblue",
            bg="#e0f7fa",
            pady=10
        )
        self.resultLabel.grid()

        self.diceButton = tk.Button(
            root,
            text="Roll",
            command=self.diceRoll,
            bg="#00796b",
            fg="white",
            activebackground="#004d40",
            font=("Arial", 14, "bold"),
            width=10,
            height=2,
            bd=3,
            relief="raised"
        )
        self.diceButton.grid(pady=10)
        self.rollLabel = tk.Label(
            self.root,
            text=f"Please Roll")
        self.rollLabel.grid()

        for widget in root.winfo_children():
            widget.grid_forget()

        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                cell_text = str(value)
                # Add player positions if they're on this cell
                players_here = [player for player, pos in self.playerPosition.items() if pos == value]

                if players_here:
                    cell_text += f"\n{', '.join(map(str, players_here))}"

                cellBackground = "lightgreen"

                if value in self.chute:
                    cellBackground = "salmon"
                elif value in self.ladder:
                    cellBackground = "lightblue"
                elif value in self.chute.values() or value in self.ladder.values():
                    cellBackground = "khaki"

                label = tk.Label(
                root,
                text=cell_text,
                width=6,
                height=3,
                borderwidth=2,
                relief="ridge",
                font=("Helvetica", 10, "bold"),
                bg=cellBackground,
                fg="black"
                )
                label.grid(row=i + 3, column=j, padx=1, pady=1)

        self.turnLabel.grid(row=0, column=0, columnspan=10)
        self.diceButton.grid(row=1, column=0, columnspan=10, pady=5)
        self.rollLabel.grid(row=2, column=0, columnspan=10)

        

        
    def diceRoll(self):
        """
        Rolls a 6 sided dice
        """
        self.roll = random.randint(1,6)
        self.rollLabel.config(text=f"You rolled a {self.roll}")
        print(self.roll)
        self.updateTurn(self.roll)
        self.roll
    
    def updateTurn(self, roll):
        player = self.currentPlayer
        
        newPosition = self.movePlayer(player, roll)
        self.playerPosition[player] = newPosition

        if newPosition == self.boardEnd:
            self.turnLabel.config(text=f"{self.players[player]} wins!")
            self.diceButton.config(state="disabled")

        if self.currentPlayer == 2:
                self.currentPlayer = 1
                self.currentPlayer
        else: 
            self.currentPlayer = 2
        
        self.drawBoard(self.root)


    def movePlayer(self, player, dice):
        """
        Takes in current player and dice roll
        Moves the player the number of spaces from the dice roll 
        Checks to see if the new spot is a chute or ladder
        Returns the new player position after roll and ladder/chute check
        """
        currentPosition = self.playerPosition[player]
        newPosition = currentPosition + dice

        if newPosition > 100:
            return currentPosition
        
        if newPosition in self.chute:
            self.resultLabel.config(text=f"{self.players[player]} went down a chute to {newPosition}")
            print("Went down a chute")
            newPosition = self.chute[newPosition]

        elif newPosition in self.ladder:
            self.resultLabel.config(text=f"{self.players[player]} went up a ladder to {newPosition}")
            print("Went up a ladder")
            newPosition = self.ladder[newPosition]

        self.resultLabel.config(text=f"{self.players[player]} moved to {newPosition}")
        print(f"{self.players[player]} moved to {newPosition}")

        return newPosition

    

    def play(self):
        """
        Runs the game loop
        while the game is active print who's turn it is
        Roll the dice and print what was rolled
        Call the move player player method and pass in current player location and dice roll 
        Moes the player to the new spot given by the movePlayer Method and then Switches player
        Continues cycle until player has reached the 100th spot
        """
        # Initialize the GUI
        
        self.root.title("Snakes Board")
        
        print("in the loop")
        self.drawBoard(self.root)
        self.root.mainloop()

          



# game loop 
if __name__ == "__main__":
    game = Game()
    game.play()