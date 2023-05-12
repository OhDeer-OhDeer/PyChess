import GamePiece

Empty = GamePiece.Empty(8, 8)

Board = [
    [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
    [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
    [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
    [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
    [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
    [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
    [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
    [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
]

BoardBinary = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]


def updateBoardBinary():
    i = 0
    for row in Board:
        j = 0
        for col in row:
            if col.piece_type == "null":
                BoardBinary[i][j] = 0
            else:
                if not Board[i][j].slain:
                    BoardBinary[i][j] = col.color
            j += 1
        i += 1


def printBoard():
    for row in Board:
        for col in row:
            print(col.piece_type, end=" ")
        print("\n")


def printCheckedB():
    for row in Board:
        for col in row:
            if col.checkedB:
                print("!", end=" ")
            else:
                print("-", end=" ")
            #print(col.checkedB, end=" ")
        print("\n")


def printCheckedW():
    for row in Board:
        for col in row:
            if col.checkedW:
                print("!", end=" ")
            else:
                print("-", end=" ")
            #print(col.checkedW, end=" ")
        print("\n")


def printBoardBinary():
    for row in BoardBinary:
        for col in row:
            print(col, end="")
        print("\n")
