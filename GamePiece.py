import MoveRules


class GamePiece:

    # constructor
    def __init__(self, piece_type, row, col, color, checkedW, checkedB):
        self.piece_type = piece_type
        self.row = row
        self.col = col
        self.color = color
        self.checkedW = checkedW
        self.checkedB = checkedB
        self.slain = False

    # movement
    def move(self, row, col, boardProper, boardBinary, turn):
        # select right color
        if turn == self.color:
            # capture
            if boardProper[row][col].piece_type != "null":
                boardProper[row][col].slain = True
                boardProper[row][col].row = -1
                boardProper[row][col].col = -1

            # move, return true
            self.row = row
            self.col = col
            return True
        # select wrong color
        elif turn == self.color * -1:
            print("wrong side.")
            return False
        # click on blank space
        else:
            return False

    def scan(self, boardProper, boardBinary):
        holdingSpace = 1
        # boardProper[self.row][self.col].checkedB = True
        # boardProper[self.row][self.col].checkedW = True


class Empty(GamePiece):
    def __init__(self, row, col):
        super().__init__("null", row, col, 0, False, False)


class Pawn(GamePiece):
    def __init__(self, piece_type, row, col, color):
        super().__init__(piece_type, row, col, color, False, False)
        # can be captured via en passant?
        self.passantable = False

    def move(self, row, col, boardProper, boardBinary, turn):
        if self.piece_type == "pawn":
            if MoveRules.pawnRules(self, int(row), int(col), boardProper, boardBinary, turn):
                return GamePiece.move(self, row, col, boardProper, boardBinary, turn)
            else:
                print("invalid move.")
                return False
        elif self.piece_type == "rook":
            if MoveRules.rookRules(self, int(row), int(col), boardBinary):
                return GamePiece.move(self, row, col, boardProper, boardBinary, turn)
            else:
                print("invalid move.")
                return False
        elif self.piece_type == "nite":
            if MoveRules.knightRules(self, row, col):
                return GamePiece.move(self, row, col, boardProper, boardBinary, turn)
            else:
                print("invalid move.")
                return False
        elif self.piece_type == "bish":
            if MoveRules.bishopRules(self, int(row), int(col), boardBinary):
                return GamePiece.move(self, row, col, boardProper, boardBinary, turn)
            else:
                print("invalid move.")
                return False
        elif self.piece_type == "quen":
            if MoveRules.bishopRules(self, int(row), int(col), boardBinary) or MoveRules.rookRules(self, int(row), int(col), boardBinary):
                return GamePiece.move(self, row, col, boardProper, boardBinary, turn)
            else:
                print("invalid move.")
                return False

    def scan(self, boardProper, boardBinary):
        if self.piece_type == "pawn":
            if self.color == -1:
                if self.row > 0:
                    if self.col < 7:
                        boardProper[self.row - 1][self.col + 1].checkedW = True
                    if self.col > 0:
                        boardProper[self.row - 1][self.col - 1].checkedW = True
            if self.color == 1:
                if self.row < 7:
                    if self.col < 7:
                        boardProper[self.row + 1][self.col + 1].checkedB = True
                    if self.col > 0:
                        boardProper[self.row + 1][self.col - 1].checkedB = True
        elif self.piece_type == "rook" or self.piece_type == "quen":
            n = self.row
            while True:
                # increment away from rook
                n += 1
                # loop exit condition
                if n > 7:
                    break
                # set spaces as checked
                if self.color == -1:
                    boardProper[n][self.col].checkedW = True
                if self.color == 1:
                    boardProper[n][self.col].checkedB = True
                if boardBinary[n][self.col] != 0:
                    break

            n = self.row
            while True:
                # decrement away from rook
                n -= 1
                # loop exit condition
                if n < 0:
                    break
                # set spaces as checked
                if self.color == -1:
                    boardProper[n][self.col].checkedW = True
                if self.color == 1:
                    boardProper[n][self.col].checkedB = True
                if boardBinary[n][self.col] != 0:
                    break

            n = self.col
            while True:
                # increment or decrement away from rook
                n += 1
                if n > 7:
                    break
                # set spaces as checked
                if self.color == -1:
                    boardProper[self.row][n].checkedW = True
                if self.color == 1:
                    boardProper[self.row][n].checkedB = True
                if boardBinary[self.row][n] != 0:
                    break

            n = self.col
            while True:
                # increment or decrement away from rook
                n -= 1
                # loop exit condition
                if n < 0:
                    break
                # set spaces as checked
                if self.color == -1:
                    boardProper[self.row][n].checkedW = True
                if self.color == 1:
                    boardProper[self.row][n].checkedB = True
                if boardBinary[self.row][n] != 0:
                    break
        elif self.piece_type == "nite":
            if self.color == -1:
                if self.row <= 6:
                    if self.col <= 5:
                        boardProper[self.row + 1][self.col + 2].checkedW = True
                    if self.col >= 2:
                        boardProper[self.row + 1][self.col - 2].checkedW = True
                    if self.row <= 5:
                        if self.col <= 6:
                            boardProper[self.row + 2][self.col + 1].checkedW = True
                        if self.col >= 1:
                            boardProper[self.row + 2][self.col - 1].checkedW = True
                if self.row >= 1:
                    if self.col <= 5:
                        boardProper[self.row - 1][self.col + 2].checkedW = True
                    if self.col >= 2:
                        boardProper[self.row - 1][self.col - 2].checkedW = True
                    if self.row >= 2:
                        if self.col <= 6:
                            boardProper[self.row - 2][self.col + 1].checkedW = True
                        if self.col >= 1:
                            boardProper[self.row - 2][self.col - 1].checkedW = True

            elif self.color == 1:
                if self.row <= 6:
                    if self.col <= 5:
                        boardProper[self.row + 1][self.col + 2].checkedB = True
                    if self.col >= 2:
                        boardProper[self.row + 1][self.col - 2].checkedB = True
                    if self.row <= 5:
                        if self.col <= 6:
                            boardProper[self.row + 2][self.col + 1].checkedB = True
                        if self.col >= 1:
                            boardProper[self.row + 2][self.col - 1].checkedB = True
                if self.row >= 1:
                    if self.col <= 5:
                        boardProper[self.row - 1][self.col + 2].checkedB = True
                    if self.col >= 2:
                        boardProper[self.row - 1][self.col - 2].checkedB = True
                    if self.row >= 2:
                        if self.col <= 6:
                            boardProper[self.row - 2][self.col + 1].checkedB = True
                        if self.col >= 1:
                            boardProper[self.row - 2][self.col - 1].checkedB = True
        elif self.piece_type == "bish" or self.piece_type == "quen":
            i = self.row
            j = self.col
            while True:
                i += 1
                j += 1
                if i > 7 or j > 7:
                    break
                if self.color == -1:
                    boardProper[i][j].checkedW = True
                if self.color == 1:
                    boardProper[i][j].checkedB = True
                if boardBinary[i][j] != 0:
                    break

            i = self.row
            j = self.col
            while True:
                i -= 1
                j += 1
                if i < 0 or j > 7:
                    break
                if self.color == -1:
                    boardProper[i][j].checkedW = True
                if self.color == 1:
                    boardProper[i][j].checkedB = True
                if boardBinary[i][j] != 0:
                    break

            i = self.row
            j = self.col
            while True:
                i += 1
                j -= 1
                if i > 7 or j < 0:
                    break
                if self.color == -1:
                    boardProper[i][j].checkedW = True
                if self.color == 1:
                    boardProper[i][j].checkedB = True
                if boardBinary[i][j] != 0:
                    break

            i = self.row
            j = self.col
            while True:
                i -= 1
                j -= 1
                if i < 0 or j < 0:
                    break
                if self.color == -1:
                    boardProper[i][j].checkedW = True
                if self.color == 1:
                    boardProper[i][j].checkedB = True
                if boardBinary[i][j] != 0:
                    break


class Rook(GamePiece):
    def __init__(self, piece_type, row, col, color):
        super().__init__("rook", row, col, color, False, False)

    def move(self, row, col, boardProper, boardBinary, turn):
        if MoveRules.rookRules(self, int(row), int(col), boardBinary):
            return GamePiece.move(self, row, col, boardProper, boardBinary, turn)
        else:
            print("invalid move.")
            return False

    def scan(self, boardProper, boardBinary):

        n = self.row
        while True:
            # increment away from rook
            n += 1
            # loop exit condition
            if n > 7:
                break
            # set spaces as checked
            if self.color == -1:
                boardProper[n][self.col].checkedW = True
            if self.color == 1:
                boardProper[n][self.col].checkedB = True
            if boardBinary[n][self.col] != 0:
                break

        n = self.row
        while True:
            # decrement away from rook
            n -= 1
            # loop exit condition
            if n < 0:
                break
            # set spaces as checked
            if self.color == -1:
                boardProper[n][self.col].checkedW = True
            if self.color == 1:
                boardProper[n][self.col].checkedB = True
            if boardBinary[n][self.col] != 0:
                break

        n = self.col
        while True:
            # increment or decrement away from rook
            n += 1
            if n > 7:
                break
            # set spaces as checked
            if self.color == -1:
                boardProper[self.row][n].checkedW = True
            if self.color == 1:
                boardProper[self.row][n].checkedB = True
            if boardBinary[self.row][n] != 0:
                break

        n = self.col
        while True:
            # increment or decrement away from rook
            n -= 1
            # loop exit condition
            if n < 0:
                break
            # set spaces as checked
            if self.color == -1:
                boardProper[self.row][n].checkedW = True
            if self.color == 1:
                boardProper[self.row][n].checkedB = True
            if boardBinary[self.row][n] != 0:
                break


class Knight(GamePiece):
    def __init__(self, piece_type, row, col, color):
        super().__init__("nite", row, col, color, False, False)

    def move(self, row, col, boardProper, boardBinary, turn):
        if MoveRules.knightRules(self, row, col):
            return GamePiece.move(self, row, col, boardProper, boardBinary, turn)
        else:
            print("invalid move.")
            return False

    def scan(self, boardProper, boardBinary):
        if self.color == -1:
            if self.row <= 6:
                if self.col <= 5:
                    boardProper[self.row + 1][self.col + 2].checkedW = True
                if self.col >= 2:
                    boardProper[self.row + 1][self.col - 2].checkedW = True
                if self.row <= 5:
                    if self.col <= 6:
                        boardProper[self.row + 2][self.col + 1].checkedW = True
                    if self.col >= 1:
                        boardProper[self.row + 2][self.col - 1].checkedW = True
            if self.row >= 1:
                if self.col <= 5:
                    boardProper[self.row - 1][self.col + 2].checkedW = True
                if self.col >= 2:
                    boardProper[self.row - 1][self.col - 2].checkedW = True
                if self.row >= 2:
                    if self.col <= 6:
                        boardProper[self.row - 2][self.col + 1].checkedW = True
                    if self.col >= 1:
                        boardProper[self.row - 2][self.col - 1].checkedW = True

        elif self.color == 1:
            if self.row <= 6:
                if self.col <= 5:
                    boardProper[self.row + 1][self.col + 2].checkedB = True
                if self.col >= 2:
                    boardProper[self.row + 1][self.col - 2].checkedB = True
                if self.row <= 5:
                    if self.col <= 6:
                        boardProper[self.row + 2][self.col + 1].checkedB = True
                    if self.col >= 1:
                        boardProper[self.row + 2][self.col - 1].checkedB = True
            if self.row >= 1:
                if self.col <= 5:
                    boardProper[self.row - 1][self.col + 2].checkedB = True
                if self.col >= 2:
                    boardProper[self.row - 1][self.col - 2].checkedB = True
                if self.row >= 2:
                    if self.col <= 6:
                        boardProper[self.row - 2][self.col + 1].checkedB = True
                    if self.col >= 1:
                        boardProper[self.row - 2][self.col - 1].checkedB = True
        return False


class Bishop(GamePiece):
    def __init__(self, piece_type, row, col, color):
        super().__init__("bish", row, col, color, False, False)

    def move(self, row, col, boardProper, boardBinary, turn):
        if MoveRules.bishopRules(self, int(row), int(col), boardBinary):
            return GamePiece.move(self, row, col, boardProper, boardBinary, turn)
        else:
            print("invalid move.")
            return False

    def scan(self, boardProper, boardBinary):
        i = self.row
        j = self.col
        while True:
            i += 1
            j += 1
            if i > 7 or j > 7:
                break
            if self.color == -1:
                boardProper[i][j].checkedW = True
            if self.color == 1:
                boardProper[i][j].checkedB = True
            if boardBinary[i][j] != 0:
                break

        i = self.row
        j = self.col
        while True:
            i -= 1
            j += 1
            if i < 0 or j > 7:
                break
            if self.color == -1:
                boardProper[i][j].checkedW = True
            if self.color == 1:
                boardProper[i][j].checkedB = True
            if boardBinary[i][j] != 0:
                break

        i = self.row
        j = self.col
        while True:
            i += 1
            j -= 1
            if i > 7 or j < 0:
                break
            if self.color == -1:
                boardProper[i][j].checkedW = True
            if self.color == 1:
                boardProper[i][j].checkedB = True
            if boardBinary[i][j] != 0:
                break

        i = self.row
        j = self.col
        while True:
            i -= 1
            j -= 1
            if i < 0 or j < 0:
                break
            if self.color == -1:
                boardProper[i][j].checkedW = True
            if self.color == 1:
                boardProper[i][j].checkedB = True
            if boardBinary[i][j] != 0:
                break


class Queen(GamePiece):
    def __init__(self, piece_type, row, col, color):
        super().__init__("quen", row, col, color, False, False)

    def move(self, row, col, boardProper, boardBinary, turn):
        if MoveRules.bishopRules(self, int(row), int(col), boardBinary) or MoveRules.rookRules(self, int(row), int(col), boardBinary):
            return GamePiece.move(self, row, col, boardProper, boardBinary, turn)
        else:
            print("invalid move.")
            return False

    def scan(self, boardProper, boardBinary):
        # Rook check
        n = self.row
        while True:
            # increment or decrement away from rook
            n += 1
            # loop exit condition
            if n > 7:
                break
            # set spaces as checked if not own side
            if self.color == -1:
                boardProper[n][self.col].checkedW = True
            if self.color == 1:
                boardProper[n][self.col].checkedB = True
            if boardBinary[n][self.col] != 0:
                break

        n = self.row
        while True:
            # increment or decrement away from rook
            n -= 1
            # loop exit condition
            if n < 0:
                break
            # set spaces as checked if not own side
            if self.color == -1:
                boardProper[n][self.col].checkedW = True
            if self.color == 1:
                boardProper[n][self.col].checkedB = True
            if boardBinary[n][self.col] != 0:
                break

        n = self.col
        while True:
            # increment or decrement away from rook
            n += 1
            if n > 7:
                break
            # set spaces as checked if not own side
            if self.color == -1:
                boardProper[self.row][n].checkedW = True
            if self.color == 1:
                boardProper[self.row][n].checkedB = True
            if boardBinary[self.row][n] != 0:
                break

        n = self.col
        while True:
            # increment or decrement away from rook
            n -= 1
            # loop exit condition
            if n < 0:
                break
            # set spaces as checked if not own side
            if self.color == -1:
                boardProper[self.row][n].checkedW = True
            if self.color == 1:
                boardProper[self.row][n].checkedB = True
            if boardBinary[self.row][n] != 0:
                break

        # bishop check
        i = self.row
        j = self.col
        while True:
            i += 1
            j += 1
            if i > 7 or j > 7:
                break
            if self.color == -1:
                boardProper[i][j].checkedW = True
            if self.color == 1:
                boardProper[i][j].checkedB = True
            if boardBinary[i][j] != 0:
                break

        i = self.row
        j = self.col
        while True:
            i -= 1
            j += 1
            if i < 0 or j > 7:
                break
            if self.color == -1:
                boardProper[i][j].checkedW = True
            if self.color == 1:
                boardProper[i][j].checkedB = True
            if boardBinary[i][j] != 0:
                break

        i = self.row
        j = self.col
        while True:
            i += 1
            j -= 1
            if i > 7 or j < 0:
                break
            if self.color == -1:
                boardProper[i][j].checkedW = True
            if self.color == 1:
                boardProper[i][j].checkedB = True
            if boardBinary[i][j] != 0:
                break

        i = self.row
        j = self.col
        while True:
            i -= 1
            j -= 1
            if i < 0 or j < 0:
                break
            if self.color == -1:
                boardProper[i][j].checkedW = True
            if self.color == 1:
                boardProper[i][j].checkedB = True
            if boardBinary[i][j] != 0:
                break


class King(GamePiece):
    def __init__(self, piece_type, row, col, color):
        super().__init__("king", row, col, color, False, False)

    def move(self, row, col, boardProper, boardBinary, turn):
        if MoveRules.kingRules(self, int(row), int(col), boardProper, boardBinary, turn):
            return GamePiece.move(self, row, col, boardProper, boardBinary, turn)
        else:
            print("invalid move.")
            return False

    def isChecked(self, board):
        if self.color == -1:
            if board[self.row][self.col].checkedB:
                return True
        if self.color == 1:
            if board[self.row][self.col].checkedW:
                return True

    def scan(self, boardProper, boardBinary):
        for i in range(self.row - 1, self.row + 2):
            for j in range(self.col - 1, self.col + 2):
                if 0 <= i <= 7 and 0 <= j <= 7:
                    if self.color == -1:
                        boardProper[i][j].checkedW = True
                    if self.color == 1:
                        boardProper[i][j].checkedB = True
