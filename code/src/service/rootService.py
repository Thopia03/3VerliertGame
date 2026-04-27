from src.entity.board import Board
from src.service.gameService import GameService
from src.service.playerActionService import PlayerActionService

class RootService:
    """
    The RootService class serves as our central point of access. It cuts the main logic into one accessible point for our GUI.
    
    Attributes:
        board (Board): This is the instance running our active game.
        playerActionService (PlayerActionService): The playerActionService serves as the main part of our game logic, enabling playing moves and checking for lose conditions.
        gameService (GameService): The gameService is responsible for restarting the game.
    """

    def __init__(self):
        self.board = Board()
        self.gameService = GameService(self)
        self.playerActionService = PlayerActionService(self)