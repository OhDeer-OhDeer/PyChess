def pawnRules(pawn, row, col, boardProper, board, turn):

    # movement
    if col == pawn.col:
        # single move
        if row == pawn.row + (1 * turn):
            if board[row][col] == 0:
                return True

        # double move, en passant
        if pawn.row == (turn + 7) % 7:
            # double move
            if row == pawn.row + (2 * turn):
                if board[row - (1 * turn)][col] == 0 and board[row][col] == 0:
                    pawn.passantable = True
                    return True

    # capturing
    elif col == pawn.col - 1 or col == pawn.col + 1:
        if row == pawn.row + turn:
            if board[row][col] == -pawn.color:
                return True

            if boardProper[row - turn][col].piece_type == "pawn" and board[row - turn][col] == -pawn.color:
                if boardProper[row - turn][col].passantable:
                    boardProper[row - turn][col].slain = True
                    boardProper[row - turn][col].row = -1
                    boardProper[row - turn][col].col = -1
                    return True
    return False


def rookRules(rook, row, col, board):
    if col == rook.col and not row == rook.row:
        n = rook.row
        while True:
            # increment or decrement away from rook
            if row - rook.row > 0:
                n += 1
            else:
                n -= 1
            # free movement
            if n == row and board[n][col] == 0:
                return True
            # capturing and blocking
            if board[n][col] == rook.color * -1 and row == n:
                return True
            else:
                if board[n][col] != 0:
                    return False

    if row == rook.row and not col == rook.col:
        n = rook.col
        while True:
            # increment or decrement away from rook
            if col - rook.col > 0:
                n += 1
            else:
                n -= 1
            # free movement
            if n == col and board[row][n] == 0:
                return True
            # capturing and blocking
            elif board[row][n] == rook.color * -1 and col == n:
                return True
            else:
                if board[row][n] != 0:
                    return False


def knightRules(knight, row, col):
    if row == knight.row + 2 and (col == knight.col + 1 or col == knight.col - 1):
        return True
    elif row == knight.row + 1 and (col == knight.col + 2 or col == knight.col - 2):
        return True
    elif row == knight.row - 2 and (col == knight.col - 1 or col == knight.col + 1):
        return True
    elif row == knight.row - 1 and (col == knight.col - 2 or col == knight.col + 2):
        return True
    return False


def bishopRules(bishop, row, col, board):
    i = bishop.row
    j = bishop.col

    # disallows moving to its own space
    if row == bishop.row and col == bishop.col:
        return False

    # increments or decrements diagonally
    while True:
        if row - bishop.row > 0:
            i += 1
        else:
            i -= 1
        if col - bishop.col > 0:
            j += 1
        else:
            j -= 1

        # free movement
        if i == row and j == col:
            if board[i][j] == 0:
                return True
        # capturing and blocking
        if board[i][j] == -bishop.color:
            if i == row and j == col:
                return True
            else:
                return False
        if board[i][j] == bishop.color or i == 0 or i == 7 or j == 0 or j == 7:
            return False


def kingRules(king, row, col, board, boardBinary, turn):
    # index of the king's starting row. Used for castling.
    homeRow = (turn + 8) % 9
    # move one space
    if king.col + 1 >= col >= king.col - 1 and king.row + 1 >= row >= king.row - 1:
        if king.color == -1:
            if not board[row][col].checkedB:
                return True
        if king.color == 1:
            if not board[row][col].checkedW:
                return True
    # castling
    elif row == homeRow and col == 2:
        if king.row == homeRow and king.col == 4 and row == homeRow:
            if board[homeRow][0].piece_type != "rook" or board[homeRow][0].color != turn:
                return False
            if king.isChecked(board):
                return False
            for i in range(1, 4):
                if board[homeRow][i].color != 0:
                    return False
                if turn == -1:
                    if board[homeRow][i].checkedB:
                        return False
                if turn == 1:
                    if board[homeRow][i].checkedW:
                        return False
            board[homeRow][0].move(homeRow, 3, board, boardBinary, turn)
            return True
    elif row == homeRow and col == 6:
        if king.row == homeRow and king.col == 4 and row == homeRow:
            if board[homeRow][7].piece_type != "rook" or board[homeRow][7].color != turn:
                return False
            if king.isChecked(board):
                return False
            for i in range(5, 7):
                if board[homeRow][i].color != 0:
                    return False
                if turn == -1:
                    if board[homeRow][i].checkedB:
                        return False
                if turn == 1:
                    if board[homeRow][i].checkedW:
                        return False
            board[homeRow][7].move(homeRow, 5, board, boardBinary, turn)
            return True
    return False
