# ДЗУрок5 ДЭДЛАЙН 21.05.2023 23 59
# ДЗ*:
# 1. Установить в свою виртуальную среду проекта внешний модуль python-decouple
# 2. В файле requirements.txt зафиксировать зависимости проекта с помощью команды pip freeze
# 3. Создать многомодульную игру Казино
# 4. Сам запуск игры в отдельном файле
# 5. Логика выигрыша или проигрыша в отдельном файле
# Правила игры такие :
# A. Есть массив из чисел от 1 до 30, каждый раз вы делаете ставку на определенную слоту из чисел и ставите деньги
# B. Рандомно выбирается выигрышная слота, если вы выигрываете, вам причисляется удвоенная сумма,
# той которую вы поставили, если вы загадали не выигрышную слоту - теряете поставленную сумму
# C. В начале игры у вас также есть деньги например 1000$, но в конце мы понимаем вы в выигрыше или в проигрыше
# D. значение переменной начального капитала должно считываться с системной переменной под названием
# MY_MONEY из файла settings.ini
# E. После каждой ставки вам задается вопрос хотите ли вы сыграть еще, если да - то делаете ставку,
# если нет - то подводится итог игры


from decouple import config
import random


def casino():
    while True:
        winning_bet = random.randint(1, 30)
        money = config('MY_MONEY', cast=int)
        your_number = int(input('Enter your number from 1 to 30: '))
        try:
            if your_number not in range(1,  31):
                print('Your number does not fit')
                continue
        except ValueError:
            print('Enter only numbers')
            continue
        bet = int(input('Your bet: '))
        try:
            if bet > money:
                print(f'Bet is bigger than your money {money}')
        except ValueError:
            print('Enter only numbers')
            continue
        if your_number == winning_bet:
            money += bet * 2
            print(f'You won: {bet * 2}')
        else:
            money -= bet
            print(f'You lost: {bet}')
        next_round = input('Do you want to continue? Yes or No: ')
        if next_round.lower() == 'yes':
            continue
        if next_round.lower() == 'no':
            print(f'Your money: {money}')
            break


if __name__ == "__main__":
    casino()
