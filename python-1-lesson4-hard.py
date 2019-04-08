# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_card_number():
    card_number = input('\nВведите номер карты: ')
    if card_number.isdigit() and len(card_number) == 16:
        try:
            card_number = int(card_number)
        except Exception:
            return False
        return card_number
    return False


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person
    return False


def get_pin_code(person):
    pin_code = input('Введите пин код: ')
    if pin_code.isdigit() and len(pin_code) == 4:
        try:
            pin_code = int(pin_code)
        except Exception:
            return False
        if person['pin'] == pin_code:
            return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] >= money:
        person['money'] -= money
        return 'Вы сняли {} рублей.'.format(money)
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    if choice == '1':
        print(check_account(person))
    elif choice == '2':
        count = input('Сумма к снятию:')
        try:
            count = float(count)
        except Exception:
            return False
        if count%1 > 0.99:
            return False
        print(withdraw_money(person, count))
    return True


def start():
    while True:
        card_number = get_card_number()
        if card_number:
            person = get_person_by_card(card_number)
            if person:
                while True:
                    choice = input('\nВыберите пункт:\n'
                        '1. Проверить баланс\n'
                        '2. Снять деньги\n'
                        '3. Выход\n'
                        '--------------------\n'
                        'Ваш выбор:')
                    if choice == '3':
                        break
                    elif choice == '1' or choice == '2':
                        if get_pin_code(person):
                            if not process_user_choice(choice, person):
                                print("Некорректно введена сумма")
                        else:
                            print("Неправильно введён пин код")
                    else:
                        print("Укажите корректный пункт меню")                    
            else:
                print("Номер карты отсутствует в списке")
        else:
            print("Неправильно введён номер карты")


start()