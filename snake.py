from enum import Enum
from collections import deque

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    STILL = 4


class Snake:

    length = None
    body = None
    direction = None
    color = (220, 230, 60)
    body_dim = None
    map_dim = None
    grid_width = None
    grid_height = None


    def __init__(self, map_dim:tuple, body_dim):
        self.body_dim = body_dim
        self.map_dim = map_dim
        self.grid_width = self.map_dim[0] // self.body_dim
        self.grid_height = self.map_dim[1] // self.body_dim

        self.direction_queue = deque(maxlen=2)

        self.respawn()

    def respawn(self):
        self.length = 3
        middle = (self.grid_width // 2, self.grid_height // 2)
        self.body = [(self.grid_position(middle[0] - 2, middle[1])), (self.grid_position(middle[0] - 1, middle[1])), (self.grid_position(middle[0], middle[1]))]
        self.direction = Direction.RIGHT

    def draw(self, game, window):
        for segment in self.body:
            game.draw.rect(window, "black", (segment[0], segment[1], self.body_dim, self.body_dim))
            game.draw.rect(window, self.color, (segment[0] + 1, segment[1] + 1, self.body_dim - 2, self.body_dim - 2))
            if segment == self.body[-1]:
                game.draw.rect(window, "black", (segment [0] + 5, segment[1] + 1, 2, 2))
                game.draw.rect(window, "black", (segment[0] + 5, segment[1] + 10, 2, 2))

    def move(self):
        if self.direction_queue:
            self.direction = self.direction_queue.popleft()
        curr_head = self.body[-1]
        if self.direction == Direction.DOWN:
            next_head = (curr_head[0], curr_head[1] + self.body_dim)
            self.body.append(next_head)
        if self.direction == Direction.UP:
            next_head = (curr_head[0], curr_head[1] - self.body_dim)
            self.body.append(next_head)
        if self.direction == Direction.LEFT:
            next_head = (curr_head[0] - self.body_dim, curr_head[1])
            self.body.append(next_head)
        if self.direction == Direction.RIGHT:
            next_head = (curr_head[0] + self.body_dim, curr_head[1])
            self.body.append(next_head)

        if self.length < len(self.body):
            self.body.pop(0)

    def steer(self, new_dir):
        last_dir = self.direction_queue[-1] if self.direction_queue else self.direction
        if len(self.direction_queue) < 3:  # only enqueue new direction if there is room
            if last_dir == Direction.DOWN and new_dir != Direction.UP:
                self.direction_queue.append(new_dir)
            elif last_dir == Direction.UP and new_dir != Direction.DOWN:
                self.direction_queue.append(new_dir)
            elif last_dir == Direction.LEFT and new_dir != Direction.RIGHT:
                self.direction_queue.append(new_dir)
            elif last_dir == Direction.RIGHT and new_dir != Direction.LEFT:
                self.direction_queue.append(new_dir)
    
    def eat(self):
        self.length += 1

    def check_for_food(self, food):
        head = self.body[-1]
        if head[0] == food.x and head[1] == food.y:
            self.eat()
            food.respawn()

    def check_tail_collision(self):
        head = self.body[-1]
        has_eaten_tail = False

        for i in range(len(self.body) - 1):
            segment = self.body[i]
            if head[0] == segment[0] and head[1] == segment[1]:
                has_eaten_tail = True

        return has_eaten_tail
    
    def check_bounds(self):
        head = self.body[-1]
        if head[0] >= self.map_dim[0]:
            return True
        if head[1] >= self.map_dim[1]:
            return True
        
        if head[0] < 0:
            return True
        if head[1] < 0:
            return True
        
        return False


    def grid_position(self, x_grid, y_grid):
        x = x_grid * self.body_dim
        y = y_grid * self.body_dim

        return x, y