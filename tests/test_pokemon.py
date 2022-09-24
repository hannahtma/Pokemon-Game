from pokemon import Venusaur, Squirtle
from tests.base_test import BaseTest

class TestPokemon(BaseTest):

    def test_venusaur_stats(self):
        v = Venusaur()
        self.assertEqual(v.get_hp(), 21)
        self.assertEqual(v.get_level(), 2)
        self.assertEqual(v.get_attack_damage(), 5)
        self.assertEqual(v.get_speed(), 4)
        self.assertEqual(v.get_defence(), 10)
        v.level_up()
        v.level_up()
        v.level_up()
        self.assertEqual(v.get_hp(), 22)
        self.assertEqual(v.get_level(), 5)
        self.assertEqual(v.get_attack_damage(), 5)
        self.assertEqual(v.get_speed(), 5)
        self.assertEqual(v.get_defence(), 10)
        v.lose_hp(5)

        self.assertEqual(str(v), "LV. 5 Venusaur: 17 HP")
    
    def test_squirtle_stats(self):
        s = Squirtle()
        self.assertEqual(s.get_hp(), 11)
        self.assertEqual(s.get_level(), 1)
        self.assertEqual(s.get_attack_damage(), 4)
        self.assertEqual(s.get_speed(), 7)
        self.assertEqual(s.get_defence(), 7)
        s.level_up()
        s.level_up()
        s.level_up()
        self.assertEqual(s.get_level(), 4)
