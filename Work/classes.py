class Player:
    "Represents a player in a game. Main properties are the players (x,y) coordinates and their health."
    def __init__(self, x, y):
        "Creates a new player."
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        "Moves the player relative to their current position"
        self.x += dx
        self.y += dy

    def damage(self, pts):
        "Damages a player."
        self.health -= min(pts, self.health)
        if self.health == 0:
            raise ValueError("Player is dead")
