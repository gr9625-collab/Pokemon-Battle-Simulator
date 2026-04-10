class Move:
    def __init__(self, name, power, accuracy, pp, type, damage_class):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.type = type
        self.damage_class = damage_class

    def __str__(self):
        return (
            f"{self.name.capitalize()}\n"
            f"Power: {self.power}\n"
            f"Accuracy: {self.accuracy}\n"
            f"pp: {self.pp}\n"
            f"Type: {self.type}\n"
            f"Damage class: {self.damage_class}\n"
        )