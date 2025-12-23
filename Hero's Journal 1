class Character:
    def __init__(self, name, max_hp, max_mp, atk, defense, crit_rate=0.1, dodge_rate=0.1, ultimate_rate=0.05):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp          # 当前血量
        self.max_mp = max_mp
        self.mp = max_mp          # 当前魔力
        self.atk = atk            # 攻击力
        self.defense = defense    # 防御力
        self.level = 1            # 等级
        self.exp = 0              # 当前经验
        self.crit_rate = crit_rate      # 暴击率（默认10%）
        self.dodge_rate = dodge_rate    # 闪避率（默认10%）
        self.ultimate_rate = ultimate_rate  # 必杀率（默认5%）

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

# 勇者：血厚、防高、攻击中等
hero = Character(
    name="勇者",
    max_hp=150,
    max_mp=30,
    atk=25,
    defense=20,
    crit_rate=0.15,      # 暴击率稍高一点
    dodge_rate=0.10,
    ultimate_rate=0.05   # 基础必杀率5%
)

# 魔法师：血薄、攻高、防低、暴击和必杀稍高
mage = Character(
    name="魔法师",
    max_hp=80,
    max_mp=100,
    atk=35,
    defense=8,
    crit_rate=0.20,
    dodge_rate=0.15,
    ultimate_rate=0.07
)

def choose_main_character():
    print("=== 勇者日志 ===")
    print("请选择你要主控的角色：")
    print("1. 勇者（耐打的前排坦克，擅长近战）")
    print("2. 魔法师（高输出后排，魔法伤害爆炸）")
    
    while True:
        choice = input("请输入数字（1 或 2）：").strip()
        if choice == "1":
            main_char = hero
            sub_char = mage
            print("\n你选择了主控【勇者】！必杀率 +10%！")
            break
        elif choice == "2":
            main_char = mage
            sub_char = hero
            print("\n你选择了主控【魔法师】！必杀率 +10%！")
            break
        else:
            print("请输入有效的数字！")
    
    # 给主控角色加必杀率加成
    main_char.ultimate_rate += 0.10
    
    return main_char, sub_char

if __name__ == "__main__":
    main_char, sub_char = choose_main_character()
    
    print("\n--- 队伍状态 ---")
    print(f"主控: {main_char.name}")
    print(f"   HP: {main_char.hp}/{main_char.max_hp}  ATK: {main_char.atk}  必杀率: {main_char.ultimate_rate:.0%}")
    print(f"队友: {sub_char.name}")
    print(f"   HP: {sub_char.hp}/{sub_char.max_hp}  ATK: {sub_char.atk}  必杀率: {sub_char.ultimate_rate:.0%}")