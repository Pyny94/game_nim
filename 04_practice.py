from nim_engin import get_bunches, put_stones, is_gameover, take_from_bunch
import os

from termcolor import cprint, colored


put_stones()
user_number = 1
while True:
    cprint("Текущая позиция", color='green')
    cprint(get_bunches(), color='green')
    user_color = 'Blue' if user_number == 1 else 'yellow'
    cprint("Ход игрока {}".format(user_number), color=user_color)
    pos = input(colored("Откуда берем?", color=user_color))
    qua = input(colored('Сколько берем?', color=user_color))
    step_successed =take_from_bunch(position=int(pos), quantity=int(qua))
    if step_successed:
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('невозможный ход!', color='red')
    if is_gameover():
        break



cprint('выйграл игрок номер{}'.format(user_number), color='red')