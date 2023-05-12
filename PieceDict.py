import GamePiece
import GameBoard


# calls all methods necessary to update board
def updateBoard():
    updateBoardPieces()
    GameBoard.updateBoardBinary()
    updateBoardChecks()


# fills board with empty variables
def updateBoardPieces():
    for i in range(0, 8):
        for j in range(0, 8):
            GameBoard.Board[i][j] = GamePiece.Empty(i, j)

    for piece in namesDictionary:
        #                                                    is an int
        GameBoard.Board[namesDictionary[piece].row][namesDictionary[piece].col] = namesDictionary[piece]


# updates checks
def updateBoardChecks():
    # clears previous checks
    for i in range(0, 8):
        for j in range(0, 8):
            GameBoard.Board[i][j].checkedB = False
            GameBoard.Board[i][j].checkedW = False
    # new checks
    for piece in namesDictionary:
        if not namesDictionary[piece].slain:
            namesDictionary[piece].scan(GameBoard.Board, GameBoard.BoardBinary)

# note: 1 -> black, -1 -> white


# extra
defaultPiece = GamePiece.GamePiece("default", 8, 8, 0, False, False)
bitch1 = GamePiece.Rook("temp", 8, 8, 0)
bitch2 = GamePiece.Bishop("temp", 8, 8, 0)


# black
# pawns
Azog = GamePiece.Pawn("pawn", 1, 0, 1)
Diadora = GamePiece.Pawn("pawn", 1, 1, 1)
Nephenee = GamePiece.Pawn("pawn", 1, 2, 1)
Hecate = GamePiece.Pawn("pawn", 1, 3, 1)
Medea = GamePiece.Pawn("pawn", 1, 4, 1)
Baal = GamePiece.Pawn("pawn", 1, 5, 1)
Hades = GamePiece.Pawn("pawn", 1, 6, 1)
Pluto = GamePiece.Pawn("pawn", 1, 7, 1)
# rooks
Rivalta = GamePiece.Rook("rook", 0, 0, 1)
Bardi = GamePiece.Rook("rook", 0, 7, 1)
# knights
Stibor = GamePiece.Knight("nite", 0, 1, 1)
Aragon = GamePiece.Knight("nite", 0, 6, 1)
# bishops
Jan = GamePiece.Bishop("bishop", 0, 2, 1)
Karol = GamePiece.Bishop("bishop", 0, 5, 1)
# queen
Helena = GamePiece.Queen("queen", 0, 3, 1)

# white
# pawns
Edric = GamePiece.Pawn("pawn", 6, 0, -1)
Carl = GamePiece.Pawn("pawn", 6, 1, -1)
Samuel = GamePiece.Pawn("pawn", 6, 2, -1)
Bob = GamePiece.Pawn("pawn", 6, 3, -1)
Marley = GamePiece.Pawn("pawn", 6, 4, -1)
Trent = GamePiece.Pawn("pawn", 6, 5, -1)
Nestor = GamePiece.Pawn("pawn", 6, 6, -1)
Damian = GamePiece.Pawn("pawn", 6, 7, -1)
# rooks
Mesola = GamePiece.Rook("rook", 7, 0, -1)
Loriano = GamePiece.Rook("rook", 7, 7, -1)
# knights
Vytautas = GamePiece.Knight("nite", 7, 1, -1)
Nicholas = GamePiece.Knight("nite", 7, 6, -1)
# bishops
Henryk = GamePiece.Bishop("bishop", 7, 2, -1)
Jerzy = GamePiece.Bishop("bishop", 7, 5, -1)
# queen
RuPaul = GamePiece.Queen("queen", 7, 3, -1)

# kings
Chad = GamePiece.King("king", 0, 4, 1)
Sigma = GamePiece.King("king", 7, 4, -1)

# ordered left to right
namesDictionary = dict([

#extra

    #("defaultPiece", defaultPiece),

# black

    # pawns
    ("Azog", Azog),
    ("Diadora", Diadora),
    ("Nephenee", Nephenee),
    ("Hecate", Hecate),
    ("Medea", Medea),
    ("Baal", Baal),
    ("Ba'al", Baal),
    ("Hades", Hades),
    ("Pluto", Pluto),

    # rooks
    ("Rivalta", Rivalta),
    ("Bardi", Bardi),
    # knights
    ("Stibor", Stibor),
    ("Aragon", Aragon),
    # bishops
    ("Jan", Jan),
    ("Karol", Karol),
    # queen
    ("Helena", Helena),
    # king
    ("Chad", Chad),


    # white

    # pawns
    ("Edric", Edric),
    ("Carl", Carl),
    ("Samuel", Samuel),
    ("Bob", Bob),
    ("Marley", Marley),
    ("Trent", Trent),
    ("Nestor", Nestor),
    ("Damian", Damian),

    # rooks
    ("Mesola", Mesola),
    ("Loriano", Loriano),

    # knights
    ("Vytautas", Vytautas),
    ("Nicholas", Nicholas),

    # bishops
    ("Henryk", Henryk),
    ("Jerzy", Jerzy),

    # queen
    ("Rupaul", RuPaul),
    ("RuPaul", RuPaul),
    # king
    ("Sigma", Sigma),
])
