import random

class Food:
    food_dim = None
    color = (252, 3, 73)
    x = None
    y = None
    map_dim = None

    def __init__(self, map_dim:tuple, food_dim):
        self.map_dim = map_dim
        self.food_dim = food_dim
        self.respawn()
    
    def draw(self, game, window):
        game.draw.rect(window, self.color, (self.x, self.y, self.food_dim, self.food_dim))

    def respawn(self):
        grid_width = self.map_dim[0] // self.food_dim
        grid_height = self.map_dim[1] // self.food_dim
        self.x = random.randint(0, grid_width - 1) * self.food_dim
        self.y = random.randint(0, grid_height - 1) * self.food_dim