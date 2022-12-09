"""
    ALL BOARD-RELATED FUNCTIONS
    :author: Sofiane DJERBI, Romain HOANG
"""
import numpy as np


class UnknownMove(Exception):
    """ Any error related to forbidden moves """
    def __init__(self):
        pass

    def __str__(self):
        return "Unknown (forbidden) move!"


class Piece:
    """ Piece codes """
    EMPTY  = 0
    OUT_OF_BOUNDS = 99
    WHITE_KING    = 01
    WHITE_QUEEN   = 02
    WHITE_ROOK    = 03
    WHITE_BISHOP  = 04
    WHITE_KNIGHT  = 05
    WHITE_PAWN    = 06
    BLACK_KING    = 11
    BLACK_QUEEN   = 12
    BLACK_ROOK    = 13
    BLACK_BISHOP  = 14
    BLACK_KNIGHT  = 15
    BLACK_PAWN    = 16


class Board:
    def __init__(self):
        """ Init board """
        self.turn = 0 # Turn number (Even: White, Odd: Black)
        self.player = 0 # Current player * 10
        self.score = (0, 0) # score[0]: White, score[1]: Black
        self.board = np.zeros((10, 10), dtype=np.int8)
        self.reset_board() # Default board config

    def reset_board(self):
        """ Default board position """
	self.board[0] = [99,99,99,99,99,99,99,99,99,99]
        self.board[1] = [99,13,15,14,12,11,14,15,13,99]
        self.board[2] = [99,16,16,16,16,16,16,16,16,99]
        self.board[3] = [99,00,00,00,00,00,00,00,00,99]
        self.board[4] = [99,00,00,00,00,00,00,00,00,99]
        self.board[5] = [99,00,00,00,00,00,00,00,00,99]
        self.board[6] = [99,00,00,00,00,00,00,00,00,99]
        self.board[7] = [99,06,06,06,06,06,06,06,06,99]
        self.board[8] = [99,03,05,04,02,01,04,05,03,99]
	self.board[9] = [99,99,99,99,99,99,99,99,99,99]

    def pseudo_legal_moves(self):
	""" All possible moves excluding king checkmates moves """
        pl_moves = list()
        pl_moves += self.pawn_moves()
        pl_moves += self.king_moves()
        pl_moves += self.knight_moves()
        pl_moves += self.queen_moves()
        pl_moves += self.bishop_moves()
        pl_moves += self.rook_moves()

    def pawn_moves(self):
        (X, Y) = np.where(self.board == (6 + player))
        for x, y in zip(X, Y):
            if x == board[x,y+1]:
		pass

 


