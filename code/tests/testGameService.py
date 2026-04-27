import unittest
from src.service.rootService import RootService
from src.entity.board import Board

class testGameService(unittest.TestCase):

    """This class tests the GameService class, checking if the restartGame function correctly resets the board and if the validStartPositions are calculated correctly"""

    def testRestartGame(self):
        """Tests if the restartGame function correctly resets the board, by giving a modified game state and then checking if it is in its inital state."""

        rootService = RootService()
        
        # we first modify our game state in every way.
        rootService.board.field[0][0] = 1
        rootService.board.field[1][1] = 2
        rootService.board.field[3][2] = 1
        rootService.board.currentPlayer = 1
        rootService.board.gameState = 0

        # to see the changes even inside our console, we print the modified board.
        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        # now we restart the game, which should be the inital state then.
        rootService.gameService.restartGame()

        # we check if the field is consisting of all 0s
        self.assertEqual(rootService.board.field, [[0 for i in range(4)] for j in range(4)])

        # we then check the rest of the board.
        self.assertEqual(rootService.board.currentPlayer, 0)
        self.assertEqual(rootService.board.gameState, 1)

        # just to check for debugging, we print the restarted board as well.
        print("\nRestarted grid looks like: ")
        for row in rootService.board.field:
            print(row)


    def testCalculateValidStartPositions(self):
        """Tests if the right start positions are calculated according to our mathmetical basis."""

        rootService = RootService()
        
        # we calculate the valid start positions after the inital state.
        validStartPositions = rootService.gameService.calculateValidStartPositions()

        # for debugging purposes, we print the valid start positions to see if they are correct.
        print("\nValid start positions are: ")
        for pos in validStartPositions:
            print(pos)


        # we now check if the valid start positions are correct, by comparing them to the inital one. This is to ensure the consistency of the method.
        self.assertEqual(validStartPositions, rootService.gameService.validStartPositions)


        # after making sure the vsp are correct, we now check if they are the same as our mathmetical basis for a 4 x 4 field.
        self.assertEqual(validStartPositions, {(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 0), (2, 1), (3, 0), (3, 1)})




if __name__ == '__main__':
    unittest.main()