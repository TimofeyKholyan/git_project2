import os
def load_level():
    levels = []
    for currentdir, dirs, files in os.walk('data'):
        for file in files:
            f = open('data/' + str(file))
            level_board = [list(map(int, line.strip().split())) for line in f]
            max_width = max(map(len, level_board))
            for i in level_board:
                if len(i) < max_width:
                    i += [10] * (max_width - len(i))
            print(level_board)
            levels.append(level_board)
load_level()