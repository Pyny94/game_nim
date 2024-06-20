from nim_engin import get_bunches, put_stones, is_gameover, take_from_bunch
import os

from colorama import Fore,Back,Style



put_stones()
user_number = 1
while True:
    print(Fore.YELLOW + 'Текущая позиция' + Style.RESET_ALL)
    print(Fore.BLUE + str(get_bunches()) + Style.RESET_ALL)
    user_color = 'Blue' if user_number == 1 else 'yellow'
    print(Fore.GREEN + f'>>> Ход игрока {user_number}' + Style.RESET_ALL)
    pos = input("Откуда берем?")
    qua = input('Сколько берем?')
    step_successed =take_from_bunch(position=int(pos), quantity=int(qua))
    if step_successed:
        user_number = 2 if user_number == 1 else 1
    else:
        print('невозможный ход!')
    if is_gameover():
        break



print(f'Победил игрок {user_number}!')