class Character:
    def __init__(self, name, max_hp, max_mp, atk, defense, crit_rate=0.1, dodge_rate=0.1, ultimate_rate=0.05):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_mp = max_mp
        self.mp = max_mp
        self.atk = atk
        self.defense = defense
        self.level = 1
        self.exp = 0
        self.exp_to_next = 50         # 到下一级需要的经验（简单起见，先固定50，后面可以做表）
        self.crit_rate = crit_rate
        self.dodge_rate = dodge_rate
        self.ultimate_rate = ultimate_rate
        
        # ========== 装备系统初始化 ==========
        self.weapon = None      # 当前武器
        self.armor = None       # 当前护具
        # ====================================

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)
    
    def gain_exp(self, amount):

        """获得经验值如果升级返回True"""
        self.exp += amount
        leveled_up = False
        while self.exp >= self.exp_to_next:
            self.exp -= self.exp_to_next
            self.level += 1
            # 属性成长（简单版：每级加固定值）
            self.max_hp += 20
            self.hp += 20          # 当前血量也补上
            self.atk += 5
            self.defense += 3
            # 下一级所需经验增加（越来越难升级）
            self.exp_to_next += 20
            leveled_up = True
            print(f"{self.name} 升到 {self.level} 级！最大HP+20，攻击+5，防御+3！")
        return leveled_up
    
    def get_total_atk(self):
        """总攻击力 = 基础 + 武器加成"""
        bonus = 0
        if self.weapon:
            bonus = self.weapon["atk_bonus"]
        return self.atk + bonus

    def get_total_defense(self):
        """总防御力 = 基础 + 护具加成"""
        bonus = 0
        if self.armor:
            bonus = self.armor["def_bonus"]
        return self.defense + bonus

    def equip_item(self, item_data):
        """自动装备：武器进武器槽，护具进护具槽（覆盖旧的）"""
        if item_data["type"] == "weapon":
            self.weapon = item_data
            print(f"{self.name} 装备了 {item_data['name']}！攻击力 +{item_data['atk_bonus']}！")
        elif item_data["type"] == "armor":
            self.armor = item_data
            print(f"{self.name} 装备了 {item_data['name']}！防御力 +{item_data['def_bonus']}！")


# 勇者和魔法师实例
hero = Character("勇者", 150, 30, 25, 20, crit_rate=0.15, dodge_rate=0.10, ultimate_rate=0.05)
mage = Character("魔法师", 80, 100, 35, 8, crit_rate=0.20, dodge_rate=0.15, ultimate_rate=0.07)


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
    
    main_char.ultimate_rate += 0.10
    
    return main_char, sub_char