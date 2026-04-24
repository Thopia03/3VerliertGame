import unittest
from src.entity.board import Board

class testBoard(unittest.TestCase):

    """This class tests the Board class, checking if the initial initialization of the board is correct, if the nextPlayer function correctly switches the current player, and if the getCurrentPlayer function returns the correct player object."""

    def testInitialisation(self):
        """Tests if the board is initialized correctly with an empty field (all 0), two player objects inside the players list, the current player set to 0, and the game state set to 1 for running."""
        board = Board()

        # check if field is consisting of all 0s
        self.assertEqual(board.field, [[0 for i in range(4)] for j in range(4)])

        #  check if there are two players
        self.assertEqual(len(board.players), 2)

        #check if the current player is set to 0
        self.assertEqual(board.currentPlayer, 0)

        # check if the game state is set to 1 for running
        self.assertEqual(board.gameState, 1)

        print("\nGrid looks like: ")
        for row in board.field:
            print(row)


    def testNextPlayer(self):
        """Tests if the nextPlayer function correctly switches the current player between 0 and 1. Is tested for 4 iterations."""
        board = Board()

        # since we already know the initial current player is 0, we can directly test the next cases.
        for i in range(4):
            currentPlayerBefore = board.currentPlayer
            # we safe the currentPlayer before, to check if the then currentPlayer is unequal to the previous one
            board.nextPlayer()
            self.assertNotEqual(board.currentPlayer, currentPlayerBefore)



    def testGetCurrentPlayer(self):
        """This Method now finally tests, if the getCurrentPlayer function returns the correct player object. We check if the Symbol of the returned player is correct, as well as the Player object itself."""
        board = Board()
        
        # We use the same 4 times to check the viability of the getCurrentPlayer function.
        for i in range(4):
            currentPlayer = board.getCurrentPlayer()

            # we check if the symbol of the current player is correct, as well as the player object itself.
            self.assertEqual(currentPlayer.symbol, board.currentPlayer + 1)
            self.assertEqual(currentPlayer, board.players[board.currentPlayer])
            board.nextPlayer()

    

    if __name__ == '__main__':
        unittest.main()