from random import randint


def set_enemy_health():
    return randint(80, 120)


def get_lite_attack():
    return randint(2, 5)


def get_mid_attack():
    return randint(15, 25)


def get_hard_attack():
    return randint(30, 40)


def compare_valumes(enemy_health, user_total_attack):
    point_difference = abs(enemy_health - user_total_attack)
    if 0 <= point_difference <= 10:
        return True
    return False


def get_user_attack():
    total = 0
    attacks_types = {
        'lite': get_lite_attack,
        'mid': get_mid_attack,
        'hard': get_hard_attack,
    }

    for i in range(5):
        input_attack = input('Введи тип атаки: ').lower()
        attack_value = attacks_types[input_attack]()
        print(f'Количество очков твоей атаки: {attack_value}.')
        total += 1
    return total


def run_game():
    user_total_attack = get_user_attack()
    enemy_health = set_enemy_health()
    print(f'Тобой нанесён урон противнику равный {user_total_attack}.')
    print(f'Очки здоровья противника после твоей атаки: {enemy_health}.')
    if compare_valumes(enemy_health, user_total_attack):
        print('Ура! Победа за тобой!')
    else:
        print('В этот раз не повезло :( Бой проигран.')
    yes_no = {
        'Y': True,
        'N': False,
    }
    replay = input('Чтобы сыграть ещё раз, введи "y"; '
                   'если не хочешь продолжать игру, введи "n": ')
    if replay not in yes_no:
        raise ValueError('Такой команды в игре нет.')
    return yes_no[replay]
