class Pokemon:
    def __init__(self, name, hp, attack, defense, sp_attack, sp_defense, speed, type, moves):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.type = type
        self.moves = moves

    def __str__(self):
        types_str = ", ".join(t.capitalize() for t in self.type)
        return (
            f"{self.name.capitalize()}\n"
            f"HP: {self.hp}/{self.max_hp}\n"
            f"Attack: {self.attack} | Defense: {self.defense}\n"
            f"Sp.Atk: {self.sp_attack} | Sp.Def: {self.sp_defense}\n"
            f"Speed: {self.speed}\n"
            f"Type: {types_str}"
        )

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0