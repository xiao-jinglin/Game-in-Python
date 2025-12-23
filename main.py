import random
from characters import choose_main_character, hero, mage
from monsters import slime, boss_greis  # 新增 boss_greis
from battle import attack
from game_data import DROP_TABLE, EQUIPMENT_LIST  

def main():
    main_char, sub_char = choose_main_character()
    
    # 游戏初始化
    turn = 0  # 当前回合数
    max_turns = 100
    monsters_defeated = 0  # 击败怪物计数
    
    print("\n=== 冒险开始！总共100回合，击败魔王吧！ ===")
    print(f"当前回合: {turn}/{max_turns}")
    print(f"{main_char.name} HP: {main_char.hp}/{main_char.max_hp}")
    print(f"{sub_char.name} HP: {sub_char.hp}/{sub_char.max_hp}\n")
    
    while turn < max_turns:

        # 随机决定是否遭遇怪物 (50% 概率)
        if random.random() < 0.5 or monsters_defeated >= 10:
            # 新增：击败10只后强制遭遇BOSS
            if monsters_defeated >= 10:
                enemy = boss_greis
                print("\n！！！强大气息逼近！！！")
                print("四天王之一 —— “森罗”葛雷斯 出现了！！\n")
            else:
                enemy = slime
                print(f"\n你遭遇了一只 {enemy.name}！")
            
            # 选择：战斗 or 无视
            print("1. 战斗")
            print("2. 无视 (不消耗回合)")
            choice = input("请输入1或2：").strip()
            
            if choice == "2":
                # BOSS战不能无视！
                if monsters_defeated >= 10:
                    print("面对四天王，你无法逃避！必须战斗！")
                else:
                    print("你无视了怪物，继续前进。")
                    continue  # 普通怪物无视成功
            
            # 进入战斗（无论普通还是BOSS都消耗回合）
            turn += 1
            print(f"\n战斗开始！当前回合: {turn}/{max_turns}")
            
            # 重置敌人血量
            enemy.hp = enemy.max_hp
            
            # 注意：角色血量不要重置！保持战斗后的残血状态才刺激
            battle_result = run_battle(main_char, sub_char, enemy)
            
            if battle_result == "victory":
                monsters_defeated += 1
                print(f"胜利！获得 {enemy.exp_drop} 经验值！")
                
                main_char.gain_exp(enemy.exp_drop)
                sub_char.gain_exp(enemy.exp_drop)
                
                # 新增：掉落装备系统
                if enemy.name in DROP_TABLE:
                    drops = DROP_TABLE[enemy.name]
                    if random.random() < 0.6:  # 60% 掉落概率
                        item_name = random.choice(drops)
                        item_data = EQUIPMENT_LIST[item_name]
                        # 随机给主控或队友装备
                        target_char = random.choice([main_char, sub_char])
                        target_char.equip_item(item_data)
                
                print(f"已击败怪物数: {monsters_defeated}/10")
                if monsters_defeated >= 10:
                    print("（下次遭遇将强制BOSS战！）")
        
        if choice == "1":
            turn += 1
            main_char.hp = main_char.max_hp
            sub_char.hp = sub_char.max_hp
            print(f"休息完毕！满血复活。当前回合: {turn}/{max_turns}")
        else:
            print("你选择了继续前进。")
        
        print(f"{main_char.name} Lv.{main_char.level} HP:{main_char.hp}/{main_char.max_hp} ATK:{main_char.get_total_atk()} DEF:{main_char.get_total_defense()}")
        print(f"  武器:{main_char.weapon['name'] if main_char.weapon else '无'}  护具:{main_char.armor['name'] if main_char.armor else '无'}")
        print(f"{sub_char.name} Lv.{sub_char.level} HP:{sub_char.hp}/{sub_char.max_mp} ATK:{sub_char.get_total_atk()} DEF:{sub_char.get_total_defense()}")
        print(f"  武器:{sub_char.weapon['name'] if sub_char.weapon else '无'}  护具:{sub_char.armor['name'] if sub_char.armor else '无'}")
        print(f"EXP: {main_char.exp}/{main_char.exp_to_next} 回合: {turn}/{max_turns}\n")
        
    print("回合用尽！魔王还未击败，世界毁灭了... 游戏失败！")

def run_battle(main_char, sub_char, enemy):
    while enemy.is_alive() and main_char.is_alive() and sub_char.is_alive():
        # 主控攻击
        dmg, _, _ = attack(main_char, enemy)
        print(f"{main_char.name} 攻击 {enemy.name}，造成 {dmg} 伤害！")
        
        if not enemy.is_alive():
            return "victory"
        
        # 怪物攻击 (优先勇者)
        target = hero if hero.is_alive() else mage
        dmg, _, _ = attack(enemy, target)
        print(f"{enemy.name} 攻击 {target.name}，造成 {dmg} 伤害！")
        
        if not target.is_alive():
            # 简单死亡处理 (后期加保护机制)
            return "defeat"
        
        # 队友攻击
        dmg, _, _ = attack(sub_char, enemy)
        print(f"{sub_char.name} 攻击 {enemy.name}，造成 {dmg} 伤害！")
    
    return "victory" if not enemy.is_alive() else "defeat"

if __name__ == "__main__":
    main()