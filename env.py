import numpy as np


class environment:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.env_map = np.zeros((x_size, y_size))
        self.player_list = []

    def add_player(self, player):
        self.player_list.append(player)

    def add_trap(self, perc):
        for i in range(self.x_size):
            for j in range(self.y_size):
                if np.random.randint(0, 100, 1) > perc:
                    self.env_map[i][j] = 1

    def check_state(self):
        if self.player_list[0].loc == self.player_list[1].loc:
            print('Got you!')
            end = True
            x = self.env_map.copy()
        elif self.env_map[self.player_list[1].loc[0],self.player_list[1].loc[1]] == 1 or \
                self.env_map[self.player_list[0].loc[0],    self.player_list[0].loc[1]] == 1:
            print('An ungraceful hit on the wall')
            end = True
            x = self.env_map.copy()
        else:
            end = False
            x = self.env_map.copy()
            x[self.player_list[0].loc[0]][self.player_list[0].loc[1]] =6
            x[self.player_list[1].loc[0]][self.player_list[1].loc[1]] =7
        return x, end

if __name__ == '__main__':
    x = environment(20, 40)
    x.add_trap(80)
    print(x.env_map)
