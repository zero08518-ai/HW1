import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
# 1) Інтроспекція
print(Fore.CYAN + "Атрибути бібліотеки:")
attributes = dir(colorama)

print(Fore.LIGHTCYAN_EX + str(attributes[:12]))
print(Fore.LIGHTGREEN_EX + str(attributes[12:]))

# 2) Основні атрибути

fore = dir(Fore)
back = dir(Back)
style = dir(Style)

print(Fore.GREEN + "\nАтрибути Fore:")
print(*fore[:15], sep="  ")
print(*fore[15:], sep="   ")
print(*fore[30:], sep="   ")

print("Приклад: ")
print(Fore.GREEN + "Успіх")

print(Fore.YELLOW + "\nАтрибути Back:")
print(*back[:15], sep="  ")
print(*back[15:], sep="   ")
print(*back[30:], sep="   ")

print("Приклад:")
print(Fore.BLACK + Back.RED + "Синтаксична помилка!")

print(Fore.RED + "\nАтрибути Style:")
print(*style[:15], sep="  ")
print(*style[15:], sep="   ")
print(*style[30:], sep="   ")

print(Style.DIM + "Приклад:")
print(Style.BRIGHT + "Помилка при виконанні!")

# 3) Основні методи
print(Fore.LIGHTCYAN_EX + "Основні методи:")
print(Fore.GREEN + "colorama.init(autoreset=True)")
print("Після кожного виводу стилі, фони та кольори тексту скидуються")

print(Fore.YELLOW + "colorama.deinit()")
print("Вимикає обробку ANSI-послідовностей та відновлює стандартний вивід.")

print(Fore.RED + "colorama.reinit()")
print("Повторно вмикає обробку ANSI-послідовностей.")

# 4) Программа


luck = random.randint(1, 20)
while True:
    num = int(input("\nВгадай число 1-20"))
    if num < 1 or num > 20:
        print(Fore.BLACK + Back.RED + "Помилка")

    elif num > luck:
        print(Fore.RED + Back.LIGHTBLACK_EX + "менше")

    elif num < luck:
        print(Fore.RED + Back.LIGHTBLACK_EX + "більше")


    elif num == luck:
        print(Fore.GREEN + Back.CYAN + "Вгадав!")
        break
    else:
        print(Back.BLACK + Fore.RED + "тут я вже хз")
