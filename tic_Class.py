class TicTacToe:
    def __init__(self):
        self.winner = None
        self.full = False
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player = "X"

    def board_full(self):
        for i in self.board:
            for j in i:
                if j == " ":
                    self.full = True
                else:
                    self.full = False

    def check_winner(self):
        print("current " + self.player)
        if (self.board[0][0] == self.board[0][1] == self.board[0][2] == self.player) or (
                self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player) or (
                self.board[0][0] == self.board[1][0] == self.board[2][0] == self.player) or (
                self.board[1][0] == self.board[1][1] == self.board[1][2] == self.player) or (
                self.board[2][0] == self.board[2][1] == self.board[2][2] == self.player) or (
                self.board[0][2] == self.board[1][2] == self.board[2][2] == self.player) or (
                self.board[0][1] == self.board[1][1] == self.board[2][1] == self.player):
            print(f'{self.player} wins!')
            self.print_board()
            self.winner = True
        else:
            self.winner = False

    def play(self):
        while True:
            self.print_board()
            decision = input("Make your move, enter (x,y) coordinates separated by space ")
            coordinates = decision.split()
            x = int(coordinates[0])
            y = int(coordinates[1])
            if self.board[x][y] == " ":
                self.board[x][y] = self.player
                self.check_winner()
                if self.winner:
                    break
                elif self.full:
                    print('tie')
                    break
                if self.player == "O":
                    self.player = "X"
                else:
                    self.player = "O"
            else:
                print("unavailable coordinates, try again")

    def print_board(self):
        for i in self.board:
            print(" | ".join(i))
            print("-" * 9)


def tic():
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    tic()
