from sword import Swords

def test_get_buff_damag():
    
    # будь-який тест складається з 3 частин
    # частина 1 - ініціалізація даних
    test_obj = Swords.create_random_rarity("Меч Екзаменатора")
    damage = int(5)
    # частина 2 - виклик тастованого коду
    result = test_obj.get_buff_damag(damage)
    # частина 3 - перевірка правильності роботи викликаного коду
    assert isinstance(result, str)
    assert test_obj.buff_damage != 0
    assert test_obj.buff_damage == damage
    assert test_obj.__hash__ in Swords.who_has_buff
    assert "Меч Екзаменатора" in result
