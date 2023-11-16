class Player:
    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        self.rank = rank

    def pass_ball(self):
        print(f"{self.name} passes the ball.")

    def shoot_ball(self):
        print(f"{self.name} shoots the ball.")

    def jump(self):
        print(f"{self.name} jumps.")

# Example Test
player1 = Player("John", 25, 3)
player1.pass_ball()
player1.shoot_ball()
player1.jump()
