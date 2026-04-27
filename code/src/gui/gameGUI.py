import tkinter as tk

class GameGUI:

    """This class gives us a grafical interface to play our game with. It handles only giving correct moves as well as showing the current player."""

    def __init__(self, root, rootService):
        # we first define the root as well as the connection to our rootService we later access.
        self.root = root
        self.rootService = rootService

        #now we add some configuration to the overall Window
        self.root.title("Three loses!")
        self.root.configure(background = "#1E1E1E")


        # here we define our top-Area, displaying the players as well as the currently active one
        topFrame = tk.Frame(root, background = "#1E1E1E")
        topFrame.pack(pady = 20, padx = 10)

        self.player1Label = tk.Label(topFrame, text = "Player X", foreground = "#9B5DE5", background = "#1E1E1E", font = ("JetBrains Mono", 20))
        self.player1Label.grid(row = 0, column = 0, padx = 30)

        self.playerActiveLabel = tk.Label(topFrame, text = "Active: X Your turn!", foreground = "#9B5DE5", background = "#1E1E1E", font = ("JetBrains Mono", 20, "bold"))
        self.playerActiveLabel.grid(row = 0, column = 1, padx = 30)

        self.player2Label = tk.Label(topFrame, text = "Player O", foreground = "#9B5DE5", background = "#1E1E1E", font = ("JetBrains Mono", 20))
        self.player2Label.grid(row = 0, column = 2, padx = 30)



        # now we define our middle-Area, displaying the game field itself
        boardFrame = tk.Frame(root, background = "#1E1E1E")
        boardFrame.pack(pady = 20, padx = 10)

        self.buttonMap = []

        for y in range(4):
            row = []
            for x in range(4):
                button = tk.Button(boardFrame, text = "", width = 8, height = 8, font = ("JetBrains Mono", 14, "bold"), background = "#1E1E1E", foreground = "#C77DFF", command = lambda x = x, y = y: self.onCellClicked(x, y)) # we use a lambda so that the button knows its own variables
                button.grid(row = y, column = x, padx = 2, pady = 2)
                row.append(button)
            self.buttonMap.append(row)



        # here we define the bottom-Area, displaying the reset button as well as the game State
        bottomFrame = tk.Frame(root, background = "#1E1E1E")
        bottomFrame.pack(pady = 20, padx = 10)

        self.resultLabel = tk.Label(bottomFrame, text = "Game running...", foreground = "#9B5DE5", background = "#1E1E1E", font = ("JetBrains Mono", 20, "bold"))
        self.resultLabel.pack(pady = 5)

        self.resetButton = tk.Button(bottomFrame, text = "Reset Game", background = "#1E1E1E", foreground = "#C77DFF", font = ("JetBrains Mono", 18, "bold"), command = self.onResetClicked)
        self.resetButton.pack()




    # GUI refresh methods


    def updateCell(self, x, y, symbol):
        button = self.buttonMap[y][x]

        if symbol == 1:
            button["text"] = "X"
        else:
            button["text"] = "O"
        

    def setActivePlayer(self):
        symbol = self.rootService.board.getCurrentPlayer().symbol
        if  symbol == 1:
            self.playerActiveLabel["text"] = "Active: X Your turn!"
        else:
            self.playerActiveLabel["text"] = "Active: O Your turn!"

    def showWinner(self, text):
        self.resultLabel["text"] = "Player" + str(text) + " lost!"

    def resetBoard(self):
        for row in self.buttonMap:
            for button in row:
                button["text"] = ""
            
        self.setActivePlayer()
        self.resultLabel["text"] = "Game running..."






    # this part defines the Event-handling for the buttons

    def onCellClicked(self, x, y):
        # check if field is already 
        if self.buttonMap[y][x]["text"] != "" or self.rootService.board.gameState != 1:
            return
            
        # before we play our move, we need to safe the symbol of the active player before the game changes them.
        symbol = self.rootService.board.getCurrentPlayer().symbol
        self.rootService.playerActionService.playSymbol(x, y)

        # update GUI
        self.setActivePlayer()
        self.updateCell(x, y, symbol) 
        self.setActivePlayer()

        # now we need to check if there is a winner or not; if yes, we need to set them!
        if self.rootService.board.gameState == 0:
            self.showWinner(self.rootService.board.getCurrentPlayer().symbol)
        elif self.rootService.board.gameState == 2:
            self.resultLabel["text"] = "Draw!"

            
            

    def onResetClicked(self):
        self.rootService.gameService.restartGame()
        self.resetBoard()