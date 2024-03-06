import unittest
from axe import Axe
from swords_bonus import SwordBonus

# клас для тестування повинен починатись з слова Test
class TestSwordBonus(unittest.TestCase):
    # В даному класі реалізуються всі юніттести у вигляді методів
    # кожен юніттест (назва функції) повинен починатись з преікса імені "test_"
    # оскільки ми працюємо в класі, ми працюємо з методами, і маємо вказівник на обєкт self який містить 
    # весь функціонал батьківського класу TestCase, з якого ми будемо використовувати перевірки assert

    def test_bonus_poison(self):
        """Тестуємо правильність накладення бафу отрути"""
        sw = Axe() # створений макет на який можемо накласти баф отрути
        sb = SwordBonus() # імплементація бонусів

        d = sw.damag # тут ми фіксуємо початкове значення нанесення шкоди
        result = sb.bonus_poison(sw) # після накладення бонусі наша метод має повернути якись результат
        # нам відомий результат що повертається, тому ми просто перевіряємо результат на рівність
        self.assertEqual(result, f"Застосовано бонус отрути {sw.name}")
        # після накладення бафу отрути наш демедж має збільшитись, 
        # тому перевіряємо що поточно значення шкоди має бути більшим за початкове
        self.assertGreater(sw.damag, d, "Накладений бонус отрути не збільшив значення шкоди.")

    def test_bonus_strength(self):
        """Тестуємо накладання бафу міцності"""
        sw = Axe() # створений макет на який можемо накласти баф отрути
        sb = SwordBonus() # імплементація бонусів
        
        v = sw.vitality # Початкове значення міцності
        result = sb.bonus_strength(sw)
        self.assertEqual(result, f"Застосовано бонус сили до {sw.name}")
        self.assertGreater(sw.vitality, v, "Накладений бонус міцності не збільшив значення міцності.")
        # Якщо ми передали неправильний обєкт, до якого не можна накласти баф, то ам просто поварнеться значення None
        self.assertIsNone(sb.bonus_strength(1), "До цього обєкне не можна застосовувати накладення бафів, неправильний обєкт")
        
#
    #def test_split(self):
    #    s = 'hello world'
    #    self.assertEqual(s.split(), ['hello', 'world'])
    #    # check that s.split fails when the separator is not a string
    #    with self.assertRaises(TypeError):
    #        s.split(2)

# Ця конструкція if не дозволить запустити цей код якщо ми його імпортнемо в інший файл
if __name__ == '__main__':
    unittest.main(verbosity=2)