class Dinosuar:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        self.robot = self.robo_target
        self.robo_target -= self.attack_power

Godzilla = Dinosuar("Godzilla", 21)