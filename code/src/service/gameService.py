from src.entity.board import Board

class GameService:
    """
    The game Service is connected to the RootService and is responsible for setting up and managing our game.
    
    Attributes:
        rootService (RootService): The connection to the rootService helps to access and manipulate the game state.
        validStartPositions (set): This set contains tuples (x,y) of all valid start positions for a triple in the field, which is essential for our lose condition.
    """

    def __init__(self, rootService):
        self.rootService = rootService
        self.validStartPositions = self.calculateValidStartPositions()

    def restartGame(self):
        """The function restarts the game by reinitializing the board & calculating the valid start positions needed for the lose condition."""

        self.rootService.board = Board()

    def calculateValidStartPositions(self):
        """
        This function calculates all valid start positions for a triple in the field.

        Returns:
            set: A set of all valid start positions for a triple in the field.

        """
        # we need the sizes of our field. Per convention it could be NxN so we need only one length to get the width and height.
        N = len(self.rootService.board.field)

        validStartPositions = set()

        # horizontal
        for x in range(N):
            for y in range(N):
                if x + 2 < N:
                    validStartPositions.add((x,y))
    
        # vertical
        for x in range(N):
            for y in range(N):
                if y + 2 < N:
                    validStartPositions.add((x,y))

        # diagonal right down
        for x in range(N):
            for y in range(N):
                if x + 2 < N and y + 2 < N:
                    validStartPositions.add((x,y))

        # diagonal left down
        for x in range(N):
            for y in range(N):
                if x - 2 >= 0 and y + 2 < N:
                    validStartPositions.add((x,y))

        return validStartPositions