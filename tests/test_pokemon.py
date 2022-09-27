from pokemon import Venusaur, Haunter, Gengar, Gastly, Squirtle
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
        self.assertEqual(s.can_evolve(), True)
        s = s.get_evolved_version()
        self.assertEqual(s.get_hp(), 21)
        self.assertEqual(s.get_level(), 3)
        self.assertEqual(s.get_attack_damage(), 9)
        self.assertEqual(s.get_speed(), 10)
        self.assertEqual(s.get_defence(), 11)
        s.lose_hp(5)
        self.assertEqual(str(s), "LV. 3 Blastoise: 16 HP")

    ### additional test files ### attack, can evolve, get evolve, defend
    def test_haunter_stats(self):
        h = Haunter()
        self.assertEqual(h.get_hp(), 9)
        self.assertEqual(h.get_level(), 1)
        self.assertEqual(h.get_attack_damage(), 8)
        self.assertEqual(h.get_speed(), 6)
        self.assertEqual(h.get_defence(), 6)
        g = h.get_evolved_version()
        self.assertIsInstance(g, Gengar)
        h.level_up()
        #haunter evolved to gengar
        gengar_class = Gengar()
        self.assertEqual(gengar_class.get_hp(), 13)
        self.assertEqual(gengar_class.get_level(), 3)
        self.assertEqual(gengar_class.get_attack_damage(), 18)
        self.assertEqual(gengar_class.get_speed(),12)
        self.assertEqual(gengar_class.get_defence(), 3)
        new_g = gengar_class.can_evolve()
        self.assertEqual(new_g, False)
        gengar_class.lose_hp(5)

        self.assertEqual(str(gengar_class), "LV. 3 Gengar: 8 HP")

    def test_gengar_stats(self):
        g = Gengar()
        self.assertEqual(g.get_hp(), 13)
        self.assertEqual(g.get_level(), 3)
        self.assertEqual(g.get_attack_damage(), 18)
        self.assertEqual(g.get_speed(), 12)
        self.assertEqual(g.get_defence(), 3)
        self.assertEqual(g.can_evolve(), False)
        g.level_up()
        g.level_up()
        g.level_up()
        self.assertEqual(g.get_hp(), 15)
        self.assertEqual(g.get_level(), 6)
        self.assertEqual(g.get_attack_damage(), 18)
        self.assertEqual(g.get_speed(), 12)
        self.assertEqual(g.get_defence(), 3)
        g.lose_hp(5)

        self.assertEqual(str(g), "LV. 6 Gengar: 10 HP")

    def test_gastly_stats(self):
        g = Gastly()
        self.assertEqual(g.get_hp(), 6)
        self.assertEqual(g.get_level(), 1)
        self.assertEqual(g.get_attack_damage(), 4)
        self.assertEqual(g.get_speed(), 2)
        self.assertEqual(g.get_defence(), 8)
        self.assertEqual(g.can_evolve(), True)
        H = g.get_evolved_version()
        self.assertIsInstance(H, Haunter)
        H.level_up()
        self.assertEqual(H.get_hp(), 10)
        self.assertEqual(H.get_level(), 2)
        self.assertEqual(H.get_attack_damage(), 8)
        self.assertEqual(H.get_speed(), 6)
        self.assertEqual(H.get_defence(), 6)
        H.lose_hp(5)

        self.assertEqual(str(H), "LV. 2 Haunter: 5 HP")


