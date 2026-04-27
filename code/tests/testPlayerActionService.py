import unittest
from src.service.rootService import RootService

class testPlayerActionService(unittest.TestCase):

    """This class tests the playerActionService, checking if the Service functions correctly."""


    # before checking the main Functions, we need to make sure, that our helper functions for the condition check work correctly.

    def testCheckIfFull(self):
        """Tests if the checkIfFull function correctly checks for a full field and returns the right boolean."""

        rootService = RootService()

        # we first insert some symbols inside our field.
        rootService.board.field[0][0] = 1
        rootService.board.field[1][0] = 1
        rootService.board.field[2][0] = 2
        rootService.board.field[3][0] = 1
        rootService.board.field[0][1] = 2
        rootService.board.field[0][2] = 1
        rootService.board.field[0][3] = 2
        rootService.board.field[1][1] = 2
        rootService.board.field[1][2] = 1
        rootService.board.field[1][3] = 2
        rootService.board.field[2][1] = 1
        rootService.board.field[3][1] = 2

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        # 12 fields are filled. Now we check if the check if full function returns false.
        self.assertFalse(rootService.playerActionService.checkIfFull())

        # now we fill the rest of the board, then check if it returns true.
        rootService.board.field[2][2] = 2
        rootService.board.field[3][3] = 2
        rootService.board.field[2][3] = 1
        rootService.board.field[3][2] = 1

        self.assertTrue(rootService.playerActionService.checkIfFull())
        



    def testCheckHorizontal(self):
        """Tests if the checkHorizontal function correctly checks for a horizontal triple for the current player."""

        rootService = RootService()

        print("\n Horizontal check:")

        # we first insert some symbols. This should result in the checkHorizontal to return false.
        rootService.board.field[0][0] = 1
        rootService.board.field[0][1] = 1

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        # now we check with the method if there is a horizontal triple, which should return false.
        self.assertFalse(rootService.playerActionService.checkHorizontal([(0,0),(1,0)]))

        # We insert a third symbol to get a horizontal triple, which should result in the checkHorizontal to return true.
        rootService.board.field[0][2] = 1

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        # now we check with the method if there is a horizontal triple, which should return true.
        self.assertTrue(rootService.playerActionService.checkHorizontal([(0,0),(1,0),(2,0)]))

        # to fully check, we insert the other players symbol in the end, which should result in the checkHorizontal to return false.
        rootService.board.field[0][2] = 2

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        self.assertFalse(rootService.playerActionService.checkHorizontal([(0,0),(1,0),(2,0)]))

        # we now lastly check if the outOfBounds handling functions correctly, by calling the method with non existing coordinates in our field.
        rootService.playerActionService.checkHorizontal([(0,0), (1,0), (2,0), (3,0), (4,0)])



    def testCheckVertical(self):
        """Tests if the checkVertical function correctly checks for a vertical triple for the current player."""

        rootService = RootService()

        print("\n Vertical check:")

        # we first insert some symbols. This should result in the checkVertical to return false.
        rootService.board.field[0][0] = 1
        rootService.board.field[1][0] = 1

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        # now we check with the method if there is a vertical triple, which should return false.
        self.assertFalse(rootService.playerActionService.checkVertical([(0,0),(0,1)]))
        
        # We insert a third symbol to get a vertical triple, which should result in the checkVertical to return true.
        rootService.board.field[2][0] = 1

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        # now we check with the method if there is a vertical triple, which should return true.
        self.assertTrue(rootService.playerActionService.checkVertical([(0,0),(0,1),(0,2)]))

        # to fully check, we insert the other players symbol in the end, which should result in the checkVertical to return false.
        rootService.board.field[2][0] = 2

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        self.assertFalse(rootService.playerActionService.checkVertical([(0,0),(0,1),(0,2)]))

        # we now lastly check if the outOfBounds handling functions correctly, by calling the method with non existing coordinates in our field.
        rootService.playerActionService.checkVertical([(0,0), (0,1), (0,2), (0,3), (0,4)])



    def testCheckDiagonalRightDown(self):
        """Tests if the checkDiagonalRightDown function correctly checks for a diagonal right down triple for the current player."""

        rootService = RootService()

        print("\n Diagonal right down check:")

        # just like the other tests, we insert symbols just so the algorithm returns false.
        rootService.board.field[0][0] = 1
        rootService.board.field[1][1] = 1

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        # now we check if there is a diagonal right down triple which should return false.
        self.assertFalse(rootService.playerActionService.checkDiagonalRightDown([(0,0), (1,1)]))

        # we insert a third symbol to get a triple, checking if the function returns true.
        rootService.board.field[2][2] = 1

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        self.assertTrue(rootService.playerActionService.checkDiagonalRightDown([(0,0), (1,1), (2,2)]))

        # like the other tests, we change the field to return false
        rootService.board.field[2][2] = 2

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        self.assertFalse(rootService.playerActionService.checkDiagonalRightDown([(0,0), (1,1), (2,2)]))

        # we now lastly check if the outOfBounds handling functions correctly, by calling the method with non existing coordinates in our field.
        rootService.playerActionService.checkDiagonalRightDown([(0,0), (1,1), (2,2), (3,3), (4,4)])

        # to make sure the algorithm doesn't check for vsps in our out of bounds area, we insert vsps that would result in a outOfBounds if checked, to see if this will not be checked. For this i added debbing for the method.
        rootService.board.field[2][0] = 1
        self.assertFalse(rootService.playerActionService.checkDiagonalRightDown([(0,0),(1,1),(2,2), [2,0]]))
    


    def testCheckDiagonalLeftDown(self):
        """Tests if the checkDiagonalLeftDown function correctly checks for a diagonal left down triple for the current player."""

        rootService = RootService()

        print("\n Diagonal left down check:")

        # just like the other tests, we insert symbols just so the algorithm returns false.
        rootService.board.field[0][3] = 1
        rootService.board.field[1][2] = 1

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        # now we check if there is a diagonal right down triple which should return false.
        self.assertFalse(rootService.playerActionService.checkDiagonalLeftDown([(3,0), (2,1)]))

        # we insert a third symbol to get a triple, checking if the function returns true.
        rootService.board.field[2][1] = 1

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        self.assertTrue(rootService.playerActionService.checkDiagonalLeftDown([(3,0), (2,1), (1,2)]))

        # like the other tests, we change the field to return false
        rootService.board.field[2][1] = 2

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        self.assertFalse(rootService.playerActionService.checkDiagonalLeftDown([(3,0), (2,1), (1,2)]))

        # we now lastly check if the outOfBounds handling functions correctly, by calling the method with non existing coordinates in our field.
        rootService.playerActionService.checkDiagonalLeftDown([(3,0), (2,1), (1,2), (0,3), (-1,4)])

        # to make sure the algorithm doesn't check for vsps in our out of bounds area, we insert vsps that would result in a outOfBounds if checked, to see if this will not be checked. For this i added debbing for the method.
        rootService.board.field[0][0] = 1
        self.assertFalse(rootService.playerActionService.checkDiagonalLeftDown([(0,0)]))





    # after checking our helper functions, we now test our main functions

    def testCheckField(self):
        """Tests if the checkField method correctly handles all cases."""

        rootService = RootService()

        print("\n CheckField check:")

        # we first check if the empty intersection rightfully returns false.
        rootService.board.field[3][3] = 1

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        self.assertFalse(rootService.playerActionService.checkField())

        # we now add cases, where the game needs to check with the helper functions. First we want false to appear.

        rootService.board.field[3][1] = 1

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        self.assertFalse(rootService.playerActionService.checkField())

        # we add another case, which should let the function return true for a found triple.
        rootService.board.field[3][2] = 1

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        self.assertTrue(rootService.playerActionService.checkField())



    def testPlaySymbol(self):
        """This method checks if a symbol gets placed correctly, and if the other cases, like finding a triple and locking the game as well as checking the full field and setting the next player function correctly."""

        rootService = RootService()

        #we define a testBoard to manually check our progress
        testBoard = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        print("\n playSymbol check:")

        #we first see, if the method places an item correctly, as well as the player is set to the next one.
        rootService.playerActionService.playSymbol(0,0)

        testBoard = [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.assertEqual(rootService.board.field, testBoard)
        self.assertEqual(rootService.board.currentPlayer, 1)

        # after the first check, we now play a few moves, so the checkField methods turns positive.

        rootService.playerActionService.playSymbol(0,1)
        rootService.playerActionService.playSymbol(1,0)
        rootService.playerActionService.playSymbol(0,2)

        testBoard = [
            [1, 1, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        # now our method should find the triple and set the game state to 0 (stopped)
        rootService.playerActionService.playSymbol(2,0)
        self.assertEqual(rootService.board.gameState, 0)

        # we reset our game and play until the board is full, to check if the method then also sets the game state to 0
        rootService.gameService.restartGame()

        rootService.playerActionService.playSymbol(0,0)
        rootService.playerActionService.playSymbol(1,0)
        rootService.playerActionService.playSymbol(2,0)
        rootService.playerActionService.playSymbol(3,0)
        rootService.playerActionService.playSymbol(1,1)
        rootService.playerActionService.playSymbol(0,1)
        rootService.playerActionService.playSymbol(3,1)
        rootService.playerActionService.playSymbol(2,1)
        rootService.playerActionService.playSymbol(1,2)
        rootService.playerActionService.playSymbol(0,2)
        rootService.playerActionService.playSymbol(3,2)
        rootService.playerActionService.playSymbol(2,2)
        rootService.playerActionService.playSymbol(0,3)
        rootService.playerActionService.playSymbol(1,3)
        rootService.playerActionService.playSymbol(2,3)
        rootService.playerActionService.playSymbol(3,3)
        

        print("\nModified grid looks like: ")
        for row in rootService.board.field:
            print(row)

        print("Game state:" + str(rootService.board.gameState))
        self.assertEqual(rootService.board.gameState, 0)


        



if __name__ == '__main__':
    unittest.main()