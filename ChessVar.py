# Author: Brody Arbon
# GitHub username: Brodee042
# Date: 3/17/2024
# Description: Overall, This program creates a list of dictionaries, called chessboard, and 4 different fairy pieces initialized as true.
# We also have a private class called gamestate and a turn system, which keeps track of which colour is allowed to move. Besides, that, it
# is a standard chess board, with some of the movement of the pieces determined by methods which recusively check ahead, to the left, right diagnonally, etc.

class ChessVar:
    """Creates a chess board, and from their one can play chess as one normally would with some slight rule changes, with
    no promotion and fairy pieces existing. Each piece has its own moveset, which we then call to see if the eligible moves
    it can play includes the next location  the player wants to go towards. This is done with recursion via submethods for a
    lot of the pieces, but some simply have lists of possible moves thorugh the use
    of index positions"""
    def __init__(self):
        self._chessboard = [
                            {'a8': 'BR', 'b8': 'BN', 'c8': 'BB', 'd8': 'BQ', 'e8': 'BK', 'f8': 'BB', 'g8': 'BN', 'h8': 'BR'},

                            {'a7': 'BP', 'b7': 'BP', 'c7': 'BP', 'd7': 'BP', 'e7': 'BP', 'f7': 'BP', 'g7': 'BP', 'h7': 'BP'},

                            {'a6': '  ', 'b6': '  ', 'c6': '  ', 'd6': '  ', 'e6': '  ', 'f6': '  ', 'g6': '  ', 'h6': '  '},

                            {'a5': '  ', 'b5': '  ', 'c5': '  ', 'd5': '  ', 'e5': '  ', 'f5': '  ', 'g5': '  ', 'h5': '  '},

                            {'a4': '  ', 'b4': '  ', 'c4': '  ', 'd4': '  ', 'e4': '  ', 'f4': '  ', 'g4': '  ', 'h4': '  '},

                            {'a3': '  ', 'b3': '  ', 'c3': '  ', 'd3': '  ', 'e3': '  ', 'f3': '  ', 'g3': '  ', 'h3': '  '},

                            {'a2': 'WP', 'b2': 'WP', 'c2': 'WP', 'd2': 'WP', 'e2': 'WP', 'f2': 'WP', 'g2': 'WP', 'h2': 'WP'},

                            {'a1': 'WR', 'b1': 'WN', 'c1': 'WB', 'd1': 'WQ', 'e1': 'WK', 'f1': 'WB', 'g1': 'WN', 'h1': 'WR'}

        ]

        self._bhunter = True
        self._bfalcon = True
        self._whunter = True
        self._wfalcon = True
        self._gamestate = 'UNFINISHED'
        self._turn = 1


    def get_chessboard(self):
        """get's chessboard"""
        return self._chessboard

    def get_turn(self):
        """gets turn"""
        return self._turn

    def get_game_state(self):
        """gets gamestate"""
        return self._gamestate

    def new_game_state(self, given_state):
        """changes the gamestate"""
        self._gamestate = given_state
        return

    def print_chessboard(self):
        """loops through all the values in chessboard, then returns them with a space between them all, creating a real board virtually"""
        given_board = self.get_chessboard()

        for dictionaries in given_board:
            print('  '.join(dictionaries.values()))

    def get_piece(self, location):
        """loops through every single dicitonary, and every value in said dictionary to get the piece of a given location"""
        given_board = self.get_chessboard()

        for dictionaries in given_board:
            for each_value in dictionaries:
                if each_value == location:
                    return dictionaries[each_value]
                # else:
                #     return False

    def enter_fairy_piece(self, piece_type, position):
        """allows the user to play a fairy piece on their given turn, and other specifications"""

        if ((self.get_turn() % 2) == 0 and piece_type == 'f' or piece_type == 'h'):
            new_row = int(position[1:])
            new_row = 8 - new_row
            if (position in self.get_chessboard[new_row] and self.get_chessboard[new_row][position]) == '  ':
                self.get_chessboard[new_row][position] = piece_type
                self._turn = self._turn + 1
                return True

        if piece_type == 'F' or piece_type == 'H':
            new_row = int(position[1:])
            new_row = 8 - new_row
            if (position in self.get_chessboard[new_row] and self.get_chessboard[new_row][position]) == '  ':
                self.get_chessboard[new_row][position] = piece_type
                self._turn = self._turn + 1
                return True
        return False







    def make_move(self, initial_location, next_location):
        """ This function controls all the movement of every piece. We first create a lot of parameters which we then pass on,
        but before we do that we check if the game is over or not, if it is still being played we check the turn, then go thorugh
        the elif tree, eventually we will find a the piece and its associated movement"""

        letter, number = initial_location[:1], initial_location[1]
        piece_type = self.get_piece(initial_location)
        replacement_type = self.get_piece(next_location)
        allowed_moves = []
        game_state = self.get_game_state()
        if game_state == 'BLACK_WON' or game_state == 'WHITE_WON':
            return False


        if (self.get_turn() % 2) == 0:
             if piece_type == 'BP':
                 allowed_moves = self.pawn_moveset(initial_location, next_location, letter, number, piece_type)
             elif piece_type == 'BR':
                 allowed_moves = self.rook_moveset(initial_location, next_location, letter, number, piece_type)
             elif piece_type == 'BN':
                 allowed_moves = self.knight_moveset(initial_location, next_location, letter, number, piece_type)
             elif piece_type == 'BB':
                 allowed_moves = self.bishop_moveset(initial_location, next_location, letter, number, piece_type)
             elif piece_type == 'BK':
                 allowed_moves = self.king_moveset(initial_location, next_location, letter, number, piece_type)
             elif piece_type == 'BQ':
                 allowed_moves = self.queen_moveset(initial_location, next_location, letter, number, piece_type)
             elif piece_type == 'BF':
                 allowed_moves = self.falcon_moveset(initial_location, next_location, letter, number, piece_type)
             elif piece_type == 'BH':
                 allowed_moves = self.hunter_moveset(initial_location, next_location, letter, number, piece_type)
             elif piece_type == '  ':
                 return False

        if (self.get_turn() % 2) != 0:
            if piece_type == 'WP':
                 allowed_moves = self.pawn_moveset(initial_location, next_location, letter, number, piece_type)
            elif piece_type == 'WR':
                 allowed_moves = self.rook_moveset(initial_location, next_location, letter, number, piece_type)
            elif piece_type == 'WN':
                 allowed_moves = self.knight_moveset(initial_location, next_location, letter, number, piece_type)
            elif piece_type == 'WB':
                 allowed_moves = self.bishop_moveset(initial_location, next_location, letter, number, piece_type)
            elif piece_type == 'WK':
                 allowed_moves = self.king_moveset(initial_location, next_location, letter, number, piece_type)
            elif piece_type == 'WF':
                 allowed_moves = self.falcon_moveset(initial_location, next_location, letter, number, piece_type)
            elif piece_type == 'WQ':
                 allowed_moves = self.queen_moveset(initial_location, next_location, letter, number, piece_type)
            elif piece_type == 'WH':
                 allowed_moves = self.hunter_moveset(initial_location, next_location, letter, number, piece_type)
            elif piece_type == '  ':
                return False
            # else:
            #     return False

        # have to loop through the list and take out the None's, as they break the following loop
        no_none_list = [x for x in allowed_moves if x is not None]

        # We get no_none_list, which we then loop through twice as our lists are double wrapped by lists, seing if
        # our given next_move is on the list of possible moves, if it is we then do some math to get the actual
        # row of the old and new location, replacing old with space and new with the new piece, checking if
        # new location has king on it as moving onto it would then end the game,

        for possible_move in no_none_list:
            for move in possible_move:
                if move == next_location:
                    new_row = int(next_location[1:])
                    old_row = int(initial_location[1:])
                    new_row = 8 - new_row
                    old_row = 8 - old_row

                    game_state = self.get_game_state()

                    if replacement_type[1] == 'K':
                        if replacement_type[0] == 'W':

                            self.new_game_state('BLACK_WON')
                        else:
                            self.new_game_state('WHITE_WON')

                    # self._chessboard[new_row][next_location] = piece_type
                    # self._chessboard[old_row][initial_location] = '  '
                    chessboard = self.get_chessboard()
                    chessboard[new_row][next_location] = piece_type
                    chessboard[old_row][initial_location] = '  '
                    self._turn = self._turn + 1
                    return True

        return False


    def pawn_moveset(self, initial_location, next_location, letter, number, piece_type):
        """creates a pawns moveset via a list of diagonal moves if their is an enemy, and moves forward
        if their is emptiness. We also check the row to see if the pawn is eligible for a 2 movement forward"""
        allowed_moves = []
        allowed_moves_container = []
        W_or_B = piece_type[:1]

        alph_notation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        num_notation = [1, 2, 3, 4, 5, 6, 7, 8]


        letter_index = alph_notation.index(letter)
        number_index = num_notation.index(int(number))

        pawn_diagonal = [(letter_index + 1, number_index + 1),
                      (letter_index - 1, number_index + 1)]


        for move in pawn_diagonal:
            new_letter_index, new_number_index = move
            if 0 <= new_letter_index < len(alph_notation) and 0 <= new_number_index < len(num_notation):

                direction_change = 1 if W_or_B == 'W' else -1
                new_number_index = number_index + direction_change

                new_position = alph_notation[new_letter_index] + str(num_notation[new_number_index])
                piece_on_square = self.get_piece(new_position)
                if piece_on_square[:1] != W_or_B and piece_on_square != '  ':
                    allowed_moves.append(new_position)
        allowed_moves_container.append(allowed_moves)


        # this is for if they are at their spawn location and can move 2 ahead
        forward_steps = 1
        if W_or_B == 'W' and number == '2':         # If white and on initial position
            forward_steps = 2
        elif W_or_B == 'B' and number == '7':       # If black and on initial position
            forward_steps = 2

        for i in range(1, forward_steps + 1):
            new_number_index = number_index + i if W_or_B == 'W' else number_index - i
            if 0 <= new_number_index < len(num_notation):
                new_position = letter + str(num_notation[new_number_index])
                piece_on_square = self.get_piece(new_position)
                if piece_on_square == '  ':
                    allowed_moves.append(new_position)
                else:
                    break

        # all our other lists are inside lists so we must do the same
        allowed_moves_container.append(allowed_moves)


        return allowed_moves_container




    def rook_moveset(self, initial_location, next_location, letter, number, piece_type):
        """creates teh rooks moveset via making a lot of lists, which we then feed as parameters to
        our submethods which check certain directions"""
        allowed_moves = []
        allowed_moves_up = []
        allowed_moves_down = []
        allowed_moves_left = []
        allowed_moves_right = []
        alph_notation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        num_notation = [1, 2, 3, 4, 5, 6, 7, 8]

        W_or_B = piece_type[:1]

        letter_index = alph_notation.index(letter)
        number_index = num_notation.index(int(number))

        allowed_moves.append(self.check_up(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_up))
        allowed_moves.append(self.check_down(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_down))
        allowed_moves.append(self.check_left(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_left))
        allowed_moves.append(self.check_right(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_right))

        return allowed_moves


    def knight_moveset(self, initial_location, next_location, letter, number, piece_type):
        """knight movement operates on a list basis, as no recursion is needed as you can't skip over a piece as a knight"""
        allowed_moves = []
        allowed_moves_container = []
        W_or_B = piece_type[:1]

        alph_notation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        num_notation = [1, 2, 3, 4, 5, 6, 7, 8]


        letter_index = alph_notation.index(letter)
        number_index = num_notation.index(int(number))

        knight_moves = [(letter_index + 2, number_index + 1),
                      (letter_index + 1, number_index + 2),
                      (letter_index + 2, number_index - 1),
                      (letter_index + 1, number_index - 2),

                      (letter_index - 1, number_index + 2),
                      (letter_index - 1, number_index - 2),
                      (letter_index - 2, number_index - 1),
                      (letter_index - 2, number_index + 1)]

        # this checks to make sure we are inbounds and the new location doesn't have a friendly unit
        for move in knight_moves:
            new_letter_index, new_number_index = move
            if 0 <= new_letter_index < len(alph_notation) and 0 <= new_number_index < len(num_notation):

                new_position = alph_notation[new_letter_index] + str(num_notation[new_number_index])
                piece_on_square = self.get_piece(new_position)
                if piece_on_square == '  ' or piece_on_square[:1] != W_or_B:
                    allowed_moves.append(new_position)
        allowed_moves_container.append(allowed_moves)
        return allowed_moves_container

    def bishop_moveset(self, initial_location, next_location, letter, number, piece_type):
        """We create a whole bunch of list, which are then fed into sub methods with deal with certian directions"""
        allowed_moves = []
        allowed_moves_up = []
        allowed_moves_down = []
        allowed_moves_left = []
        allowed_moves_right = []
        alph_notation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        num_notation = [1, 2, 3, 4, 5, 6, 7, 8]

        W_or_B = piece_type[:1]

        letter_index = alph_notation.index(letter)
        number_index = num_notation.index(int(number))

        allowed_moves.append(self.diagonal_left_up(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_up))
        allowed_moves.append(self.diagonal_right_up(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_down))
        allowed_moves.append(self.diagonal_left_down(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_left))
        allowed_moves.append(self.diagonal_right_down(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_right))

        return allowed_moves

    def queen_moveset(self, initial_location, next_location, letter, number, piece_type):
        """create lots of lists, which we are then fed back after our submethods go through and recursively check each direction"""
        allowed_moves = []
        allowed_moves_up = []
        allowed_moves_down = []
        allowed_moves_left = []
        allowed_moves_right = []
        alph_notation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        num_notation = [1, 2, 3, 4, 5, 6, 7, 8]

        W_or_B = piece_type[:1]

        letter_index = alph_notation.index(letter)
        number_index = num_notation.index(int(number))

        allowed_moves.append(self.diagonal_left_up(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_up))
        allowed_moves.append(self.diagonal_right_up(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_down))
        allowed_moves.append(self.diagonal_left_down(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_left))
        allowed_moves.append(self.diagonal_right_down(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_right))

        allowed_moves_up1 = []
        allowed_moves_down1 = []
        allowed_moves_left1 = []
        allowed_moves_right1 = []

        allowed_moves.append(self.check_up(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_up1))
        allowed_moves.append(self.check_down(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_down1))
        allowed_moves.append(self.check_left(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_left1))
        allowed_moves.append(self.check_right(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_right1))

        return allowed_moves

    def king_moveset(self, initial_location, next_location, letter, number, piece_type):
        """king can't skip over pieces, so no recursion is needed, only a list of possible moves"""
        allowed_moves = []
        allowed_moves_container = []
        W_or_B = piece_type[:1]

        alph_notation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        num_notation = [1, 2, 3, 4, 5, 6, 7, 8]


        letter_index = alph_notation.index(letter)
        number_index = num_notation.index(int(number))

        king_moves = [(letter_index + 1, number_index),
                (letter_index + 1, number_index + 1),
                (letter_index, number_index + 1),
                (letter_index - 1, number_index + 1),
                (letter_index - 1, number_index),
                (letter_index - 1, number_index - 1),
                (letter_index, number_index - 1),
                (letter_index + 1, number_index - 1)]

        # that list is fed here, which checks if the move is inbounds or not, if it is, it then checks if the piece on the new square is empty or an enemy
        for move in king_moves:
            new_letter_index, new_number_index = move
            if 0 <= new_letter_index < len(alph_notation) and 0 <= new_number_index < len(num_notation):

                new_position = alph_notation[new_letter_index] + str(num_notation[new_number_index])
                piece_on_square = self.get_piece(new_position)
                if piece_on_square == '  ' or piece_on_square[:1] != W_or_B:
                    allowed_moves.append(new_position)
        allowed_moves_container.append(allowed_moves)
        return allowed_moves_container

    def falcon_moveset(self, initial_location, next_location, letter, number, piece_type):
        """falcon moveset created with our submethods, for the colour we swap/reverse the list of possible numbers/letters, so that the
        moveset is mirrored"""
        allowed_moves = []
        allowed_moves_up = []
        allowed_moves_down = []
        allowed_moves_left = []
        allowed_moves_right = []
        alph_notation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        num_notation = [1, 2, 3, 4, 5, 6, 7, 8]

        W_or_B = piece_type[:1]

        # mirrors moveset for black
        if W_or_B == 'B':
            alph_notation.reverse()
            num_notation.reverse()
        else:
            pass

        letter_index = alph_notation.index(letter)
        number_index = num_notation.index(int(number))

        allowed_moves.append(self.diagonal_left_up(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_up))
        allowed_moves.append(self.diagonal_right_up(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_down))
        allowed_moves.append(self.check_down(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_left))

        return allowed_moves

    def hunter_moveset(self, initial_location, next_location, letter, number, piece_type):
        """hunter moveset created with recusive submethods, we mirror if the piece is black"""

        allowed_moves = []
        allowed_moves_up = []
        allowed_moves_down = []
        allowed_moves_left = []
        allowed_moves_right = []
        alph_notation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        num_notation = [1, 2, 3, 4, 5, 6, 7, 8]

        W_or_B = piece_type[:1]

        # mirror if black
        if W_or_B == 'B':
            alph_notation.reverse()
            num_notation.reverse()
        else:
            pass

        letter_index = alph_notation.index(letter)
        number_index = num_notation.index(int(number))

        # the given submethods
        allowed_moves.append(self.check_up(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_up))
        allowed_moves.append(self.diagonal_left_down(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_left))
        allowed_moves.append(self.diagonal_right_down(letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_right))

        return allowed_moves

    def check_up(self, letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_up):
        """a submethod we use to check up from white's perspective"""
        new_number_index = number_index + 1

        # checks if out of bounds
        if 0 <= new_number_index < len(num_notation):
            new_position = alph_notation[letter_index] + str(num_notation[new_number_index])
            piece_on_position = self.get_piece(new_position)

            if piece_on_position == '  ':
                allowed_moves_up.append(new_position)
                self.check_up(letter_index, new_number_index, num_notation, alph_notation, W_or_B, allowed_moves_up)

            # if the peice infront is friendly, just return list/end recursion
            if piece_on_position[:1] == W_or_B:                                                   # see if the pieces are the same color
                return allowed_moves_up

            # if enemy, put that location then end recursion as we can only take one piece and cant skip over
            elif piece_on_position[:1] != W_or_B:
                allowed_moves_up.append(new_position)
                return allowed_moves_up

    def check_down(self, letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_down):
        """submethod for checking down from whites perspective"""
        new_number_index = number_index - 1

        # makes sure it's not out of bounds
        if 0 <= new_number_index < len(num_notation):
            new_position = alph_notation[letter_index] + str(num_notation[new_number_index])
            piece_on_position = self.get_piece(new_position)

            if piece_on_position == '  ':
                allowed_moves_down.append(new_position)
                self.check_down(letter_index, new_number_index, num_notation, alph_notation, W_or_B, allowed_moves_down)

            if piece_on_position[:1] == W_or_B:  # see if the pieces are the same color
                return allowed_moves_down

            # if enemy, put that location then end recursion as we can only take one piece and cant skip over
            elif piece_on_position[:1] != W_or_B:
                allowed_moves_down.append(new_position)
                return allowed_moves_down

    def check_left(self, letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_left):
        """submethod for checking left from whites perspective"""
        new_letter_index = letter_index - 1

        if 0 <= new_letter_index < len(num_notation):
            new_position = alph_notation[new_letter_index] + str(num_notation[number_index])
            piece_on_position = self.get_piece(new_position)

            if piece_on_position == '  ':
                allowed_moves_left.append(new_position)
                self.check_left(new_letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_left)

            if piece_on_position[:1] == W_or_B:  # see if the pieces are the same color
                return allowed_moves_left

            # if enemy, put that location then end recursion as we can only take one piece and cant skip over
            elif piece_on_position[:1] != W_or_B:
                allowed_moves_left.append(new_position)
                return allowed_moves_left


    def check_right(self, letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_right):
        """submethod for checking right from whites perspective"""
        new_letter_index = letter_index + 1

        if 0 <= new_letter_index < len(num_notation):
            new_position = alph_notation[new_letter_index] + str(num_notation[number_index])
            piece_on_position = self.get_piece(new_position)

            if piece_on_position == '  ':
                allowed_moves_right.append(new_position)
                self.check_right(new_letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_right)

            if piece_on_position[:1] == W_or_B:  # see if the pieces are the same color
                return allowed_moves_right

            # if enemy, put that location then end recursion as we can only take one piece and cant skip over
            elif piece_on_position[:1] != W_or_B:
                allowed_moves_right.append(new_position)
                return allowed_moves_right

    def diagonal_left_up(self, letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_up):
        """submethod for checking diagnoal up"""
        new_number_index = number_index + 1
        new_letter_index = letter_index - 1

        if 0 <= new_number_index < len(num_notation) and 0 <= new_letter_index < len(alph_notation):
            new_position = alph_notation[new_letter_index] + str(num_notation[new_number_index])
            piece_on_position = self.get_piece(new_position)

            if piece_on_position == '  ':
                allowed_moves_up.append(new_position)
                self.diagonal_left_up(new_letter_index, new_number_index, num_notation, alph_notation, W_or_B, allowed_moves_up)

            if piece_on_position[:1] == W_or_B:  # see if the pieces are the same color
                return allowed_moves_up

            # if enemy, put that location then end recursion as we can only take one piece and cant skip over
            elif piece_on_position[:1] != W_or_B:
                allowed_moves_up.append(new_position)
                return allowed_moves_up

    def diagonal_right_up(self, letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_down):
        """submethod for checking diagonal right down"""
        new_number_index = number_index + 1
        new_letter_index = letter_index + 1

        if 0 <= new_number_index < len(num_notation) and 0 <= new_letter_index < len(alph_notation):
            new_position = alph_notation[new_letter_index] + str(num_notation[new_number_index])
            piece_on_position = self.get_piece(new_position)

            if piece_on_position == '  ':
                allowed_moves_down.append(new_position)
                self.diagonal_right_up(new_letter_index, new_number_index, num_notation, alph_notation, W_or_B, allowed_moves_down)

            if piece_on_position[:1] == W_or_B:  # see if the pieces are the same color
                return allowed_moves_down

            # if enemy, put that location then end recursion as we can only take one piece and cant skip over
            elif piece_on_position[:1] != W_or_B:
                allowed_moves_down.append(new_position)
                return allowed_moves_down

    def diagonal_left_down(self, letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_left):
        """submethod for checking diagnoal left down"""

        new_letter_index = letter_index - 1
        new_number_index = number_index - 1

        # checks if out of position
        if 0 <= new_letter_index < len(num_notation) and 0 <= new_number_index < len(alph_notation):
            new_position = alph_notation[new_letter_index] + str(num_notation[new_number_index])
            piece_on_position = self.get_piece(new_position)

            if piece_on_position == '  ':
                allowed_moves_left.append(new_position)
                self.diagonal_left_down(new_letter_index, new_number_index, num_notation, alph_notation, W_or_B, allowed_moves_left)

            if piece_on_position[:1] == W_or_B:  # see if the pieces are the same color
                return allowed_moves_left

            # if enemy, put that location then end recursion as we can only take one piece and cant skip over
            elif piece_on_position[:1] != W_or_B:
                allowed_moves_left.append(new_position)
                return allowed_moves_left

    def diagonal_right_down(self, letter_index, number_index, num_notation, alph_notation, W_or_B, allowed_moves_right):
        """submethod for checking diagonal right down"""

        new_letter_index = letter_index + 1
        new_number_index = number_index - 1

        if 0 <= new_letter_index < len(num_notation) and 0 <= new_number_index < len(alph_notation):
            new_position = alph_notation[new_letter_index] + str(num_notation[new_number_index])
            piece_on_position = self.get_piece(new_position)

            if piece_on_position == '  ':
                allowed_moves_right.append(new_position)
                self.diagonal_right_down(new_letter_index, new_number_index, num_notation, alph_notation, W_or_B, allowed_moves_right)

            if piece_on_position[:1] == W_or_B:  # see if the pieces are the same color
                return allowed_moves_right

            # if enemy, put that location then end recursion as we can only take one piece and cant skip over
            elif piece_on_position[:1] != W_or_B:
                allowed_moves_right.append(new_position)
                return allowed_moves_right



# game = ChessVar()
# game.print_chessboard()
#
#
# # print(game.make_move('d2', 'd4'))
# # print(game.make_move('d1', 'd3'))
# # print(game.make_move('d3', 'e3'))
# # print(game.make_move('e3', 'e7'))
# # # print(game.make_move('d8', 'f6'))
# print(game.make_move('d7', 'e8'))
# print(game.get_game_state())
# print(game.make_move('a7', 'a6'))
# print(game.get_game_state())
# print(game.make_move('a7', 'a6'))
#
# # game.enter_fairy_piece('F', 'c4')
# print(game.get_game_state())
# game.print_chessboard()
#



