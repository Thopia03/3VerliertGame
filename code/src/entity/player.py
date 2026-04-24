class Player:

    """
    Player class to represent a player entity in game.

    Attributes:
        symbol (int): The symbol of the player, either 1 or 2.
    """

    def __init__(self, symbol = int):
        """
        Initializes the Player object with a symbol and the name, given by their Symbol.

        Args:
            symbol (int): The symbol of the player, either 1 or 2. As given our convention, it repesents their mark on the Grid, either X or O.
        """

        self.symbol = symbol
        self.name = "Player " + str(symbol)