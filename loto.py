"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import os
import random

class Card:
   def __init__(self):
      self._barrel_count = 15
      self._card_nubers_list = []
      self._card_positions_list = []
      for __ in range(0, 3):     # создаём карточку
         self._card_positions_list += sorted(random.sample(list(range(0, 9)), 5))
         while True:
            numbers_row = random.sample(list(range(1, 91)), 5)
            compare = False
            for num in numbers_row:
               if num in self._card_nubers_list:
                  compare = True
                  break
            if compare:
               continue
            self._card_nubers_list += sorted(numbers_row)      
            break
      self._card_positions_list.append(-1)
      
   def print_card(self):      # печатаем карточку
      index = 0
      for __ in range(0, 3):
         card_string = ''
         for pos in range(0, 9):
            if pos == self._card_positions_list[index]:
               if self._card_nubers_list[index] > 9:
                  card_string += str(self._card_nubers_list[index])
               elif 0 <= self._card_nubers_list[index] <= 9:
                  card_string += ' '
                  card_string += str(self._card_nubers_list[index])
               else:
                  card_string += "--"
               index += 1
            else:
               card_string += "  "
            card_string += " "
         print(card_string[:len(card_string) - 1])

   def new_barrel(self, burrel_number):      # сравниваем с числом на бочонке
      try:
         burrel_number = int(burrel_number)
      except Exception:
         return -1
      if 1 > burrel_number > 91:
         return -1
      if burrel_number in self._card_nubers_list:
         for ind in range(0, len(self._card_nubers_list)):
            if burrel_number == self._card_nubers_list[ind]:
               self._card_nubers_list[ind] = -1
         return True
      else:
         return False

   def get_barrel_count(self):      # выводим число оставшихся полей
      return self._barrel_count


player_card = Card()
computer_card = Card()
burrels_list = []
while True:
   os.system('cls')
   while True:
      new_burrel = random.randint(1, 91)
      if new_burrel in burrels_list:      
         continue
      else:
         break
   burrels_list.append(new_burrel)
   print("Новый бочонок: {} (осталось {})".format(new_burrel, 90 - len(burrels_list)))
   computer_card.new_barrel(new_burrel)
   print("------ Ваша карточка -----")
   player_card.print_card()
   print("--------------------------")
   print("-- Карточка компьютера ---")
   computer_card.print_card()
   print("--------------------------")
   while True:
      aswer = input("Зачеркнуть цифру? (y/n) (выйти q)")
      if aswer == 'y':
         player_card.new_barrel(new_burrel)
         break
      elif aswer == 'n':
         player_card.new_barrel(new_burrel)
      elif aswer == 'q':
         exit()
      else:
         print("Некорректный ввод!")

