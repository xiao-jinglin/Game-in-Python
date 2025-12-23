# game_data.py
# 所有游戏数据：装备表、经验表等

EQUIPMENT_LIST = {
    # 武器（新手村掉落）
    "铁剑": {"type": "weapon", "atk_bonus": 10, "name": "铁剑"},
    "钢剑": {"type": "weapon", "atk_bonus": 20, "name": "钢剑"},
    
    # 护具
    "皮甲": {"type": "armor", "def_bonus": 10, "name": "皮甲"},
    "铁甲": {"type": "armor", "def_bonus": 20, "name": "铁甲"},
    
    # BOSS专属神装
    "森罗之刃": {"type": "weapon", "atk_bonus": 50, "name": "森罗之刃"},
    "葛雷斯护符": {"type": "armor", "def_bonus": 40, "name": "葛雷斯护符"},
}

# 怪物掉落表（字典：怪物名 -> 可能掉落装备列表）
DROP_TABLE = {
    "史莱姆": ["铁剑", "皮甲"],  # 低级装备，概率低
    "“森罗”葛雷斯": ["钢剑", "铁甲", "森罗之刃", "葛雷斯护符"],  # BOSS掉神装
}