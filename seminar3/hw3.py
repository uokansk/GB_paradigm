class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        print(self.board)

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "0" if self.current_player == "X" else "X"
        else:
            print('The position is occupied.')
        winner = self.check_winner()
        if winner: print(f'The winner is: {winner}! Congratulations!')

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return self.board[line[0]]
            if " " not in self.board:
                return "Draw"
            return None


game = TicTacToe()

for i in range(9):
    game.make_move(i)
    print(game.board)

game.check_winner()
