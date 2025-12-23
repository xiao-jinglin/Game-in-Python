# battle.py
from monsters import Monster  # 确保有这一行（之前加过）

def attack(attacker, defender):
    # 攻击力：角色用装备加成，怪物用基础
    if hasattr(attacker, 'get_total_atk'):
        base_damage = attacker.get_total_atk()
    else:
        base_damage = attacker.atk
    
    damage = base_damage
    
    # 防御减免
    if isinstance(defender, Monster):
        actual_damage = max(0, damage - defender.defense)
    else:
        actual_damage = max(0, damage - defender.get_total_defense())
    
    defender.take_damage(actual_damage)
    return actual_damage, False, False