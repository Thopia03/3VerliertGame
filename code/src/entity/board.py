from src.entity.player import Player

class Board:

    """
    Board class represents the game field. It also functions as a structure to manage the (active) player and the game state.

    Attributes:
        field (list): A 4x4 list representing the game field.
        players (list): A list of Player objects representing the two players in the game.
        currentPlayer (int): An integer representing the index of the current player in the players list
        gameState (int): An integer representing the current state of the game. 0 for ongoing, 1 for player 1 wins, 2 for player 2 wins, and -1 for a draw.
    """

    def __init__(self):
        self.field = [[0 for i in range(4)] for j in range(4)]
        self.players = [Player(1), Player(2)]
        self.currentPlayer = 0
        self.gameState = 1 # game state 0 for stopped, game state 1 for running

    def nextPlayer(self):
        """Switches the current player to the next. As we use an integer to represent the current player index, we use modulo to switch between 0 and 1."""
        self.currentPlayer = (self.currentPlayer + 1) % 2

    def getCurrentPlayer(self):
        """
        We need the current player object for the game logic, to check for lose conditions and updating the game state accordingly.
    
        Returns:
            Player: The current player object.
        """
        return self.players[self.currentPlayer]
    