

class game():
    """Handles game logic for rock-paper-scissors"""

    def __init__(self, id):
        self.p1_made_choice = False
        self.p2_made_choice = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0
    
    def get_player_move(self, player_num):
        """
        Get the move choice of player # p
            :param player_num: [0,1]
            :return: move
        """
        return self.moves[player_num]
    
    def play(self, player_num, move):
        """
        Set player move
            Param player_num: [0,1]
            Param move: ['r','p','s']
        """

        self.moves[player_num] = move
        if player_num == 0:
            self.p1_made_choice = True
        else:
            self.p2_made_choice = True
    
    def connected(self):
        return self.ready
    
    def both_players_made_choice(self):
        """
        Determines if both players made their move choice
            rtype: bool
        """
        return self.p1_made_choice and self.p2_made_choice

    def get_winner(self):
        """
        Determines which player won
            return: [-1,0,1] Where -1 indicates tie
        """

        # Case: tie
        if self.moves[0] == self.moves[1]:
            return -1
        
        if self.moves[0] == 'r':
            if self.moves[1] == 's':
                return 0
            else:
                return 1
        
        if self.moves[0] == 'p':
            if self.moves[1] == 'r':
                return 0
            else:
                return 1

        if self.moves[0] == 's':
            if self.moves[1] == 'p':
                return 0
            else:
                return 1
    
    def reset(self):
        """Resets player move choices"""
        self.p1_made_choice = False
        self.p2_made_choice = False
