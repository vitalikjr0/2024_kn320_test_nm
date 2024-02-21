# спочатку йдуть імпорти бібліотек
from game.sword import Swords
from random import randint
# опис функціоналу програми у вигляді функцій

# виконання всієї програми
if __name__ == "__main__":
    print("Старт гри:")
    player1 = input("Введіть імя першого гравця: ")
    player2 = input("Введіть імя другого гравця: ")
    c = Swords.create_random_rarity("Катана")
    print(f"Гравець {player1} отримує Меч:", c.info)
    d = Swords.create_random_rarity("Шпага")
    print(f"Гравець {player2} отримує Меч:", d.info)

    # емулюємо як ми користуємось нашим мечем, накладаємо баф, меч старіє/зношується від 
    # використання та ми проводимо бої де його міцність зменшується
    c.get_buff_vitality(2)
    print(f"Наклали баф: {c.info}")
    c.aging()
    print(f"Меч почав старіти: {c.info}")
    d.attack(c)
    print(f"Нас атакували {d.name} з атакою {d.damag}: {c.info}")
    c.expired_buff()
    print(f"Закінсилась дія бафу: {c.info}")
    c.repair(2)
    print(f"Справляємо Меч: {c.info}")
    c.attack(d)
    print(f"Атакували у відповідь: {d.info}")

    if c.vitality > 0 and c.vitality >= d.vitality:
        print(f"Гравець {player1} переміг над {player2}")
    else:
        print(f"Гравець {player2} переміг над {player1}")

    print("Завершення гри")
