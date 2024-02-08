class Player:
    def __init__(self, initial_position):
        self.position = initial_position

    def move_up(self, distance):
        self.position[1] += distance

    def move_down(self, distance):
        self.position[1] -= distance

    def move_left(self, distance):
        self.position[0] -= distance

    def move_right(self, distance):
        self.position[0] += distance

    def get_position(self):
        return self.position