

class PlayerActionService:
    """
    The playerActionService manages our main game logic, enabling players to play their symbols as well as check for conditions to end the game.
    
    Attributes:
        rootService (RootService): The connection to the rootService helps to access and manipulate the game state.
    """

    def __init__(self, rootService):
        self.rootService = rootService





    def playSymbol(self, x: int, y: int):
        """
        The playSymbol allows the current player to play their symbol on the board. Since we take care in the GUI to play valid moves, we only need to check our game Logic.
        For orientation see the activity diagram in the documentation 'assets/diagrams/activity_diagram_playturn.svg'.
        
        Args:
            x (int): The x coordinate of the field where the player wants to play their symbol.
            y (int): The y coordinate of the field where the player wants to play their symbol.
        """

        # due to the safty of our GUI, we know that our move is valid. We now can add the move to our board.
        self.rootService.board.field[y][x] = self.rootService.board.getCurrentPlayer().symbol #because we have list of lists, we first need to insert the y coordinate

        # after playing our move, we need to check for the lose condition. We do this by calling our helper function checkField.
        if self.checkField():
            # if we have a hit, we set the game state to 0, which means the game is over and we can end the game.
            self.rootService.board.gameState = 0
        else:
            # if there is no hit, we first need to check if the field is full, which also ends the game.
            if self.checkIfFull():
                self.rootService.board.gameState = 2
            else:
                # if there is no hit and the field is not full, we can go on to the next player and let them play.
                self.rootService.board.nextPlayer()






    def checkField(self):
        """
        This is our essential algorithm to check for lose conditions. It works the following:

        1) We collect all Coordinates placed by the current active player in the field.
        2) We filter the list by looking for valid start positions, by intersecting both sets.
        3) If the intersection is empty, we know there is start position we need to check and we can go on to check if the field is full.
        4) If there are valid start positions, we need to check the neighbours for a placed symbol matching the current player. (for this we have the helper functions to check them.)
        5) If analysis of our helper functions are 'False', we can go further to check if the field is full.
        6) If analysis of our helper functions are 'true', we give this information further, changing our game state to 0 and ending the game.

        Returns:
            bool: True if the current player has lost, False otherwise.
        """

        # 1) Collect all coordinates of the symbols placed by the current player.
        playerCoordinates = set()
        for y in range(len(self.rootService.board.field)):
            for x in range(len(self.rootService.board.field)):
                if self.rootService.board.field[y][x] == self.rootService.board.getCurrentPlayer().symbol:
                    playerCoordinates.add((x,y))

        # 2) Now we filter the list by intersecting the coordinates with the valid start positions.
        playerCoordinates = playerCoordinates.intersection(self.rootService.gameService.validStartPositions)

        # 3) We first check if there are valid start positions hit by the player, by checking if the intersection is empty.
        if len(playerCoordinates) == 0:
            # if there are no positions, we return false and let the upper function (play Symbol) check if the field is full.
            return False
        else:
            # 4) Now that there are valid start positions, we need to check their neightbours for a hit.
            if self.checkHorizontal(playerCoordinates) or self.checkVertical(playerCoordinates) or self.checkDiagonalRightDown(playerCoordinates) or self.checkDiagonalLeftDown(playerCoordinates):
                # 6) If there is a hit (triple), we return true, which will be used in the playSymbol function to end the game.
                return True
            else:
                # 5) If there is no hit, we return false and let the upper function (play Symbol) check if the field is full.
                return False






    #This part defines our helper functions to check for the neighbours to find a triple. According to their name, they check the corresponding direction & return a boolean value.

    def checkHorizontal(self, playerCoordinates):
        for coordinate in playerCoordinates:
            #out of bounds safety
            if coordinate[0] + 2 >= len(self.rootService.board.field):
                continue

            # now we check the + 2 neighbours in x-direction for a hit.
            if self.rootService.board.field[coordinate[1]][coordinate[0] + 1] == self.rootService.board.getCurrentPlayer().symbol and self.rootService.board.field[coordinate[1]][coordinate[0] + 2] == self.rootService.board.getCurrentPlayer().symbol:
                return True
            
        # if there is no horizontal triple, we end the check.
        return False

    def checkVertical(self, playerCoordinates):
        for coordinate in playerCoordinates:
            #out of bounds safety
            if coordinate[1] + 2 >= len(self.rootService.board.field):
                continue

            # now we check the + 2 neighbours in y-direction for a hit.
            if self.rootService.board.field[coordinate[1] + 1][coordinate[0]] == self.rootService.board.getCurrentPlayer().symbol and self.rootService.board.field[coordinate[1] + 2][coordinate[0]] == self.rootService.board.getCurrentPlayer().symbol:
                return True
            
        # if there is no vertical triple, we end the check.
        return False

    def checkDiagonalRightDown(self, playerCoordinates):

        # for the diagonal cases, we need to watch out, since they can end up in a outOfBounds error, which is why we need to check the coordinates.
        for coordinate in playerCoordinates:
            if coordinate[0] + 2 < len(self.rootService.board.field) and coordinate[1] + 2 < len(self.rootService.board.field):
            # now that we made sure the vsp won't end in an outOfBounds error, we check the diagonal right down neighbours for a hit.
                if self.rootService.board.field[coordinate[1] + 1][coordinate[0] + 1] == self.rootService.board.getCurrentPlayer().symbol and self.rootService.board.field[coordinate[1] + 2][coordinate[0] + 2] == self.rootService.board.getCurrentPlayer().symbol:
                    return True
            
        # if there is no diagonal right down triple, we end the check.
        return False
        

                
    def checkDiagonalLeftDown(self, playerCoordinates):

        # same case for the diagonal left down, we need to watch out for outOfBounds errors, which is why we check the coordinates first.
        for coordinate in playerCoordinates:
            if coordinate[0] - 2 >= 0 and coordinate[1] + 2 < len(self.rootService.board.field):
            # now that we made sure the vsp won't end in an outOfBounds error, we check the diagonal left down neighbours for a hit.
                if self.rootService.board.field[coordinate[1] + 1][coordinate[0] - 1] == self.rootService.board.getCurrentPlayer().symbol and self.rootService.board.field[coordinate[1] + 2][coordinate[0] - 2] == self.rootService.board.getCurrentPlayer().symbol:
                    return True
                
        # if there is no diagonal left down triple, we end the check.
        return False






    def checkIfFull(self):
        """
        This helper function allows us to check if our field is full, ending the game if so.
        
        Returns:
            bool: True if the field is full, False otherwise.
        """
        for y in range(len(self.rootService.board.field)):
            for x in range(len(self.rootService.board.field)):
                if self.rootService.board.field[y][x] == 0:
                    return False

        # now our field is full.
        return True
