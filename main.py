import GameBoard
import PieceDict
import pygame
from numpy import *
pygame.init()

# creates pygame screen
screen = pygame.display.set_mode([400, 400])

# variables
turn = 1
playing = True
winner = 0
selectPiece = PieceDict.defaultPiece
promoting = False
promotionScreenB = pygame.image.load('./Art/FrameB.png')
promotionScreenW = pygame.image.load('./Art/FrameW.png')
promotePawn = PieceDict.defaultPiece

# set up board
# updates board
PieceDict.updateBoard()
# GameBoard.printBoard()
# GameBoard.printBoardBinary()

# sprites for pieces
defaultImage = pygame.image.load('./Art/TokenDefault.png')
pawnImage = defaultImage
bishopImage = defaultImage
rookImage = defaultImage
knightImage = defaultImage
queenImage = defaultImage
kingImage = defaultImage


# is the king in check?
def kingChecked(theTurn):
    # runs test
    PieceDict.updateBoard()
    if theTurn == 1:
        return PieceDict.Chad.isChecked(GameBoard.Board)
    if theTurn == -1:
        return PieceDict.Sigma.isChecked(GameBoard.Board)


# turn passing
def passTurn():

    # updates board
    PieceDict.updateBoard()

    # draws board
    global pawnImage, bishopImage, rookImage, knightImage, queenImage, kingImage
    global turn
    screen.fill((255, 255, 255))
    for i in range(0, 8):
        for j in range(0, 8):
            pygame.draw.rect(screen, (255 * (i % 2), 255 * (i % 2), 255 * (i % 2)),
                             pygame.Rect(50 * i, 100 * j + 50, 50, 50))
            pygame.draw.rect(screen, (255 * ((i + 1) % 2), 255 * ((i + 1) % 2), 255 * ((i + 1) % 2)),
                             pygame.Rect(50 * i, 100 * j, 50, 50))
    # draws pieces
    for piece in PieceDict.namesDictionary:
        # does not draw if piece is dead
        if not PieceDict.namesDictionary[piece].slain:
            # differentiates between piece types
            if PieceDict.namesDictionary[piece].piece_type == "pawn":
                # en passant
                if PieceDict.namesDictionary[piece].color == turn * -1:
                    PieceDict.namesDictionary[piece].passantable = False
                # en passant over
                if PieceDict.namesDictionary[piece].color == 1:
                    pawnImage = pygame.image.load('./Art/PawnB.png')
                elif PieceDict.namesDictionary[piece].color == -1:
                    pawnImage = pygame.image.load('./Art/PawnW.png')
                screen.blit(pawnImage, ((PieceDict.namesDictionary[piece].col * 50), (PieceDict.namesDictionary[piece].row * 50)))
            if PieceDict.namesDictionary[piece].piece_type == "bish":
                if PieceDict.namesDictionary[piece].color == 1:
                    bishopImage = pygame.image.load('./Art/BishopB.png')
                elif PieceDict.namesDictionary[piece].color == -1:
                    bishopImage = pygame.image.load('./Art/BishopW.png')
                screen.blit(bishopImage, ((PieceDict.namesDictionary[piece].col * 50), (PieceDict.namesDictionary[piece].row * 50)))
            if PieceDict.namesDictionary[piece].piece_type == "rook":
                if PieceDict.namesDictionary[piece].color == 1:
                    rookImage = pygame.image.load('./Art/RookB.png')
                if PieceDict.namesDictionary[piece].color == -1:
                    rookImage = pygame.image.load('./Art/RookW.png')
                screen.blit(rookImage, ((PieceDict.namesDictionary[piece].col * 50), (PieceDict.namesDictionary[piece].row * 50)))
            if PieceDict.namesDictionary[piece].piece_type == "nite":
                if PieceDict.namesDictionary[piece].color == 1:
                    knightImage = pygame.image.load('./Art/KnightB.png')
                if PieceDict.namesDictionary[piece].color == -1:
                    knightImage = pygame.image.load('./Art/KnightW.png')
                screen.blit(knightImage, ((PieceDict.namesDictionary[piece].col * 50), (PieceDict.namesDictionary[piece].row * 50)))
            if PieceDict.namesDictionary[piece].piece_type == "quen":
                if PieceDict.namesDictionary[piece].color == 1:
                    queenImage = pygame.image.load('./Art/QueenB.png')
                if PieceDict.namesDictionary[piece].color == -1:
                    queenImage = pygame.image.load('./Art/QueenW.png')
                screen.blit(queenImage, ((PieceDict.namesDictionary[piece].col * 50), (PieceDict.namesDictionary[piece].row * 50)))
            if PieceDict.namesDictionary[piece].piece_type == "king":
                if PieceDict.namesDictionary[piece].color == 1:
                    kingImage = pygame.image.load('./Art/KingB.png')
                if PieceDict.namesDictionary[piece].color == -1:
                    kingImage = pygame.image.load('./Art/KingW.png')
                screen.blit(kingImage, ((PieceDict.namesDictionary[piece].col * 50), (PieceDict.namesDictionary[piece].row * 50)))

            if promoting and turn == -1:
                screen.blit(promotionScreenW, (0, 150))
            elif promoting and turn == 1:
                screen.blit(promotionScreenB, (0, 150))

    pygame.display.flip()
    if not promoting:
        turn *= -1


# initial board setup
passTurn()

# main loop
while playing:
    # processes input
    for event in pygame.event.get():
        # surrender
        if event.type == pygame.KEYDOWN and pygame.K_c:
            playing = False
            winner = turn * -1

        if event.type == pygame.QUIT:
            playing = False

        # selecting pieces
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseCol, mouseRow = pygame.mouse.get_pos()
            if not promoting:
                # records int position of mouse 0 <= x <= 7
                mouseCol = int(mouseCol / 50)
                mouseRow = int(mouseRow / 50)
                # selects piece at position mouseCol, mouseRow
                selectPiece = GameBoard.Board[mouseRow][mouseCol]
                print(selectPiece.piece_type + " selected")
            else:
                # promotion selection
                if 175 < mouseRow < 225:
                    if 25 < mouseCol < 75:
                        promotePawn.piece_type = "rook"
                    elif 125 < mouseCol < 175:
                        promotePawn.piece_type = "nite"
                    elif 225 < mouseCol < 275:
                        promotePawn.piece_type = "bish"
                    elif 325 < mouseCol < 375:
                        promotePawn.piece_type = "quen"
                promoting = False
                passTurn()


        # moving by dragging
        elif event.type == pygame.MOUSEBUTTONUP and selectPiece != PieceDict.defaultPiece and not promoting:
            mouseCol, mouseRow = pygame.mouse.get_pos()
            mouseCol = int(mouseCol / 50)
            mouseRow = int(mouseRow / 50)
            # moves selected piece, update board if successful. If king, give board, otherwise, boardBinary
            if selectPiece.piece_type != "king":
                # stores board because it will be altered in process of kingChecked()
                storageRow = selectPiece.row
                storageCol = selectPiece.col
                if selectPiece.move(mouseRow, mouseCol, GameBoard.Board, GameBoard.BoardBinary, turn):
                    # exit condition: succesful move
                    if not kingChecked(turn):
                        if selectPiece.piece_type == "pawn" and (selectPiece.row == 0 or selectPiece.row == 7):
                            promotePawn = selectPiece
                            promoting = True
                        passTurn()
                    else:
                        if turn == 1:
                            PieceDict.Chad.checkedW = False
                        else:
                            PieceDict.Sigma.checkedB = False
                        selectPiece.row = storageRow
                        selectPiece.col = storageCol
                        print("King is checked.")
                        PieceDict.updateBoard()

            else:
                # stores board because it will be altered in process of kingChecked()
                storageRow = selectPiece.row
                storageCol = selectPiece.col
                if selectPiece.move(mouseRow, mouseCol, GameBoard.Board, GameBoard.BoardBinary, turn):
                    if not kingChecked(turn):
                        passTurn()
                    else:
                        if turn == 1:
                            PieceDict.Chad.checkedW = False
                        else:
                            PieceDict.Sigma.checkedB = False
                        selectPiece.row = storageRow
                        selectPiece.col = storageCol
                        print("King is checked.")
                        PieceDict.updateBoard()

            selectPiece = PieceDict.defaultPiece

# ending
if winner == -1:
    print("White wins!")
elif winner == 1:
    print("Black wins!")
