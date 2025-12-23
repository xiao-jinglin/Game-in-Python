class Monster:
    def __init__(self, name, max_hp, atk, defense, exp_drop):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.defense = defense
        self.exp_drop = exp_drop

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage


# 第一只怪物
slime = Monster("史莱姆", 50, 15, 5, 20)

# 四天王之一：森罗·葛雷斯（植物毒雾系，90级风范）
boss_greis = Monster(
    name="“森罗”葛雷斯",
    max_hp=300,       # 血超级厚
    atk=45,           # 一刀能打掉你不少血
    defense=25,       # 防御高，你的攻击减免多
    exp_drop=200      # 打赢给海量经验
)