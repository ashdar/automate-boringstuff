# Chess Dictionary Validator

# In this chapter, we used the dictionary value
# {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
# to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary
# argument and returns True or False depending on if the board is valid.

# A valid board will have exactly one black king and exactly one white king.
# Each player can only have
# at most 16 pieces,
# at most 8 pawns, and
# all pieces must be on a valid space from '1a' to '8h';
# that is, a piece can’t be on space '9z'.

# The piece names begin with either a 'w' or 'b' to represent white or black,
# followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.

# This function should detect when a bug has resulted in an improper chess board.

# WriteVerbose needs to inspect the stack.
import inspect

### Tool functions #########


def WriteVerbose(Verbose, Message):
    """Mimic Powershell Write-Verbose
    Returns None"""

    if (Verbose):
        print(str(inspect.stack()[1].function) + ':' + Message)

### Script functions #########


def isValidChessBoardPieceCount(ledger, Verbose=False):

    # print(ledger)

    MaxPieces = {
        'bking': 1, 'wking': 1, 'bqueen': 1, 'wqueen': 1, 'bbishop': 2, 'wbishop': 2, 'brook': 2, 'wrook': 2, 'bknight': 2, 'wknight': 2, 'bpawn': 8, 'wpawn': 8
    }

    IsValid = True
    # a 'correct count' means that there are no more than the maximum nuber of pieces
    # IOW, no color can have more than 1 king or 1 queen.
    # this isn't really true, as it ignores 'pawn promotion', a/k/a 'queening'
    # https://en.wikipedia.org/wiki/Promotion_(chess)
    for piece in ledger:
        # print("{0}\t{1}\t{2}".format(piece, MaxPieces[piece], ledger[piece]))
        # Need to use MaxPieces.get() here, because we might be fed bad piecenames. 
        # If we use MaxPieces[piece] and piece is bad (ex:wkicker), we get a run time error
        # Note taht failing to find a bad piece here will fail this test. 
        # If you check for valid piece names, that check will fail also. 
        # IOW, one problem can fail two different tests.
        if (MaxPieces.get(piece,0) < ledger[piece]):
            IsValid = False
            Message = "{0} has an incorrect count of {1}".format(
                piece, ledger[piece])
        else:
            Message = "{0} has an correct count of {1}".format(
                piece, ledger[piece])

        WriteVerbose(Verbose, Message)

    return(IsValid)


def isValidChessBoardPieceName(piece, Verbose=False):
    """Is this the name of a chess piece
    Returns boolean"""
    validPieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    # check the length. If it is bad, we will bail oout before checking the name
    IsValid = False
    if(len(piece) >= 4 and len(piece) <= 6):
        IsValid = True

    if (IsValid):
        Message = r"'{0}' has correct length".format(piece)
    else:
        Message = r"'{0}' does NOT have a correct length".format(piece)
    
    WriteVerbose(Verbose, Message)
    
    if (IsValid == False):
        return(IsValid)

    # check the name
    if(piece in validPieces):
        IsValid = True
    else:
        IsValid = False

    if (Verbose):
        if (IsValid):
            Message = r"'{0}' is a valid piece name".format(piece)
        else:
            Message = r"'{0}' is NOT a valid piece name".format(piece)
        WriteVerbose(Verbose, Message)

    return(IsValid)


def isValidChessBoardColor(color, Verbose=False):
    """Two colors, White or Black
    Returns boolean"""

    validColors = ['b', 'w']
    
    # check the length. If it is bad, we will bail oout before checking the color
    IsValid = False
    if(len(color) == 1):
        IsValid = True
    
    if (IsValid):
        Message = r"'{0}' has a correct length".format(color)
    else:
        Message = r"'{0}' does NOT have a correct length".format(color)

    WriteVerbose(Verbose, Message)
    if (IsValid == False):
        return(IsValid)

    # check the color    
    if(color in validColors):
        IsValid = True
    else:
        IsValid = False

    if (Verbose):
        if (IsValid):
            Message = r"'{0}' is a valid color".format(color)
        else:
            Message = r"'{0}' is NOT a valid color".format(color)
        WriteVerbose(Verbose, Message)

    return(IsValid)


def isValidChessBoardSpace(spot, Verbose=False):
    """ Validates each location on the board
    Returns boolean"""

    # all pieces must be on a valid space from '1a' to '8h';
    # that is, a piece can’t be on space '9z'.

    # it might be cuter to use RegEx here, but this works.
    validXPositions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    validYPositions = ['1', '2', '3', '4', '5', '6', '7', '8']

    if(len(spot) != 2):
        IsValid = False
        if (IsValid):
            Message = r"'{0}' has a correct length".format(spot)
        else:
            Message = r"'{0}' does NOT have a correct length".format(spot)
        WriteVerbose(Verbose, Message)
    else:
        if(spot[0] in validYPositions and spot[1] in validXPositions):
            IsValid = True
        else:
            IsValid = False

        if (Verbose):
            if (IsValid):
                Message = r"'{0}' is valid notation".format(spot)
            else:
                Message = r"'{0}' is NOT valid notation".format(spot)
            WriteVerbose(Verbose, Message)

    return(IsValid)


def isValidChessBoard(board, Verbose=True):
    """ Validates a chesboard, passed in as a dictionary
    Returns boolean"""

    AllPiecesHaveValidLocation = True
    AllPiecesHaveValidColor = True
    AllPiecesHaveValidName = True
    PieceCount = {}

    for k, v in board.items():
        # print('Key:' + k + '\tValue:' + str(v))
        # print('Key:{0}\tValue:{1}'.format(k, v))
        # v is color and piece, so strip those here for conveience
        color = v[0]
        piece = v[1:]
        # print('Key:{0}\tValue:{1}\tColor:{2}\tPiece:{3}'.format(
        #     k, v, color, piece))

        if (isValidChessBoardSpace(k, Verbose) != True):
            # WriteVerbose(Verbose, "{0} is not a valid space")
            AllPiecesHaveValidLocation = False

        if (isValidChessBoardColor(color, Verbose) != True):
            # WriteVerbose(Verbose, "{0} is not a valid space")
            AllPiecesHaveValidColor = False

        if (isValidChessBoardPieceName(piece, Verbose) != True):
            AllPiecesHaveValidName = False

        PieceCount.setdefault(v, 0)
        PieceCount[v] += 1

    # Now,out of the loop, summarize what we found
    AllPiecesHaveValidCount = isValidChessBoardPieceCount(PieceCount, Verbose)
    WriteVerbose(Verbose, 'AllPiecesHaveValidCount is ' +
                 str(AllPiecesHaveValidCount))

# fixme: This does not check to see if a spot is occupied by more than one piece

    WriteVerbose(Verbose, 'AllPiecesHaveValidLocation is ' +
                 str(AllPiecesHaveValidLocation))
    WriteVerbose(Verbose, 'AllPiecesHaveValidColor is ' +
                 str(AllPiecesHaveValidColor))
    WriteVerbose(Verbose, 'AllPiecesHaveValidName is ' +
                 str(AllPiecesHaveValidName))

    AllResult = AllPiecesHaveValidCount & AllPiecesHaveValidLocation & AllPiecesHaveValidColor & AllPiecesHaveValidName
    return (AllResult)


### Main ###########
Verbose = True

# this is OK
board = {'1h': 'bking', '6c': 'wqueen',
         '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

# this has too many bbishop
# board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
#          '5h': 'bqueen', '3e': 'wking', '4b': 'bbishop', '4c': 'bbishop'}

# this has a bad location
# board = {'9z': 'bking', '6c': 'wqueen',
#          '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

# this has a bad piecename
# board = {'1h': 'bking', '6c': 'wqueen',
#          '2g': 'bbishop', '5h': 'bqueen', '3e': 'wfullback'}

# this has a bad color
# board = {'1h': 'bking', '6c': 'wqueen',
#          '2g': 'bbishop', '5h': 'bqueen', '3e': 'xking'}

isValid = isValidChessBoard(board)
print('Is this a valid chess board: ' + str(isValid))

# isValidChessBoardSpace('1a', True)

# tests for isValidChessBoardSpace
# # valid
# print('The following are valid:')
# print(isValidChessBoardSpace('1a', Verbose))
# print(isValidChessBoardSpace('8a', Verbose))
# print(isValidChessBoardSpace('1h', Verbose))
# print(isValidChessBoardSpace('8h', Verbose))

# # Invalid
# print('The following are invalid, for various reasons:')
# # too few characters
# print(isValidChessBoardSpace('1', Verbose))
# # too many characters
# print(isValidChessBoardSpace('1aa', Verbose))
# # not on the board, which is only 8 by 8, or 8 by h if you use notation
# print(isValidChessBoardSpace('9a', Verbose))
# print(isValidChessBoardSpace('1i', Verbose))
