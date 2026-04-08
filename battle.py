class Pokemon:
    def __init__(self, name, hp, attack, defense, sp_attack, sp_defense, moves):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.moves = moves

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

class Move:
    def __init__(self, name, power):
        self.name = name
        self.power = power

class Battle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def calculate_damage(self, attacker, defender, move):
        return max(1, attacker.attack + move.power - defender.defense)
    
    def turn(self, attacker, defender, move):
        damage = self.calculate_damage(attacker, defender, move)
        defender.take_damage(damage)
        print(f"{attacker.name} used {move.name}!")
        print(f"It dealt {damage} damage!")

    def run(self):
        attacker = self.p1
        defender = self.p2

        while attacker.is_alive() and defender.is_alive():
            move = attacker.moves[0] # Simply selects the first move for now
            self.turn(attacker, defender, move)
            attacker, defender = defender, attacker

        print(f"{attacker.name if attacker.is_alive() else defender.name} wins!")