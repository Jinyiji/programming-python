class TictactoeGameEngine:
    def __init__(self):
        self.SIZE = 3
        self.board = list('.' * self.SIZE * self.SIZE)  # ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'

    def show_board(self):       # FPI
        for a in range(len(self.board)):
            print(self.board[a], end=' ')
            if a % self.SIZE == self.SIZE -1:   # *
                print()

    def set(self, row, col):    # 송이김밥
        self.board[self.SIZE*(row-1)*(col-1)] = self.turn

    def set_winner(self):       # 쓰리라프
        # - 3 줄
        # | 3 줄
        # \
        # /
        # return self.turn
        # 비기는 조건 : 디 채워졌을 때 위의 것에 해당되지 않았을 때 : self.board 에 '.'이 없는 상태  # 스우파 도윤
        # print('X len: ', len(self.board['X']))
        # print('O len: ', len(self.board['O']))
        # if len(self.board['X']) + len(self.board['O']) == 9:
        #     return 'd'      # draw



    def change_turn(self):      # 모두의 틱택토
        # self. turn 'X' 면 'O' 틀리면 'X'로 바꾸자
        # if self.turn == 'X':
        #     self.turn = 'O'
        # else:
        #     self.turn = 'X'

        self.turn = 'O' if self.turn == 'X' else 'X'    # 위의 4줄과 같음

if __name__ == '__main__':      # main + ctrl + space bar
    game_engine = TictactoeGameEngine()
    game_engine.show_board()            # ...\n...\n...
    game_engine.set(3, 2)
    game_engine.show_board()
    game_engine.set(3, 1)
    game_engine.set(3, 3)
    print(game_engine.set_winner())     # 'X'
    game_engine.change_turn()
    print(game_engine.turn)             # 'O'
    # 무승부 만들자, 확인하자
    game_engine.board = ['X', 'O', 'X',
                         'O', 'O', 'X',
                         'X', 'X', 'O']
