import random

from engine import MainBoardCoords, SubBoardCoords, SubBoard
from players.stdout import StdOutPlayer


class Random(StdOutPlayer):
    def __init__(self):
        super().__init__()

    def get_move_that_lets_me_win(self, sub_board):
        //Get all available moves
        all_moves = sub_board.get_playable_coords()
        for move in all_moves:
            if move>0:

        //For each moves
            //Play move
            //If it won
                //Return
        //Return random

    def get_my_move(self):  # -> Tuple[MainBoardCoords, SubBoardCoords]
        main_board_coords = self.pick_next_main_board_coords()
        sub_board = self.main_board.get_sub_board(main_board_coords)
        sub_board_coords = get_move_that_lets_me_win(sub_board)
        return main_board_coords, sub_board_coords

    def pick_next_main_board_coords(self) -> MainBoardCoords:
        if self.main_board.sub_board_next_player_must_play is None:
            return random.choice(self.main_board.get_playable_coords())
        else:
            return self.main_board.sub_board_next_player_must_play

    @staticmethod
    def pick_random_sub_board_coords(sub_bord: SubBoard) -> SubBoardCoords:
        return random.choice(sub_board.get_playable_coords())
