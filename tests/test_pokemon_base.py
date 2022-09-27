from random_gen import RandomGen
from pokemon_base import PokemonBase, PokeType
from pokemon import Eevee, Gastly, Haunter, Charmander, Squirtle, Bulbasaur, Blastoise, Venusaur, Charizard
from tests.base_test import BaseTest

class TestPokemonBase(BaseTest):

    def test_cannot_init(self):
        """Tests that we cannot initialise PokemonBase, and that it raises the correct error."""
        self.assertRaises(TypeError, lambda: PokemonBase(30, PokeType.FIRE))

    def test_level(self):
        e = Eevee()
        self.assertEqual(e.get_level(), 1)
        e.level_up()
        self.assertEqual(e.get_level(), 2)
    
    def test_hp(self):
        e = Eevee()
        self.assertEqual(e.get_hp(), 10)
        e.lose_hp(4)
        self.assertEqual(e.get_hp(), 6)
        e.heal()
        self.assertEqual(e.get_hp(), 10)

    def test_status(self):
        RandomGen.set_seed(0)
        e1 = Eevee()
        e2 = Eevee()
        e1.attack(e2)
        # e2 now is confused.
        e2.attack(e1)
        # e2 takes damage in confusion.
        self.assertEqual(e1.get_hp(), 10)

    def test_evolution(self):
        g = Gastly()
        self.assertEqual(g.can_evolve(), True)
        self.assertEqual(g.should_evolve(), True)
        new_g = g.get_evolved_version()
        self.assertIsInstance(new_g, Haunter)

    ### additional test files ###
    def additional_pokemon_detail_tests(self):
        s = Squirtle()
        self.assertEqual(s.get_poke_name(), "Squirtle")
        self.assertEqual(s.get_poke_type(), "Water")
        self.assertEqual(s.get_level(), 1)
        self.assertEqual(s.get_attack_damage(), 4)
        self.assertEqual(s.get_defence(), 7)
        s.level_up()
        self.assertEqual(s.get_level(), 2)
        self.assertEqual(s.get_attack_damage(), 5)
        self.assertEqual(s.get_defence(), 8)

        b = Bulbasaur()
        self.assertEqual(b.get_poke_name(), "Bulbasaur")
        self.assertEqual(b.get_poke_type(), "Grass")
        self.assertEqual(b.get_level(), 1)
        self.assertEqual(b.get_attack_damage(), 5)
        self.assertEqual(b.get_defence(), 5)
        b.level_up()
        self.assertEqual(b.get_level(), 2)
        self.assertEqual(b.get_attack_damage(), 5)
        self.assertEqual(b.get_defence(), 5)

        c = Charmander()
        self.assertEqual(c.get_poke_name(), "Charmander")
        self.assertEqual(c.get_poke_type(), "Fire")
        self.assertEqual(c.get_level(), 1)

    def test_hp_and_fainted(self):
        s = Squirtle()
        self.assertEqual(s.get_hp(), 11)
        s.lose_hp(7)
        self.assertEqual(s.get_hp(), 4)
        self.assertEqual(s.is_fainted(), False)
        s.heal()
        self.assertEqual(s.get_hp(), 11)
        s.lose_hp(11)
        self.assertEqual(s.is_fainted(), True)

        b = Bulbasaur()
        self.assertEqual(b.get_hp(), 13)
        b.lose_hp(5)
        self.assertEqual(b.get_hp(), 8)
        b.heal()
        self.assertEqual(b.get_hp(), 13)
        self.assertEqual(b.is_fainted(), False)

    def additional_status_tests(self):
        RandomGen.set_seed(645)
        s1 = Squirtle()
        s2 = Squirtle()
        s1.attack(s2)
        # s2 now is paralyzed.
        self.assertEqual(s2.get_status_effect(), "Paralysis")
        s2.attack(s1)
        # s2 taking effect and speed is halved.
        self.assertEqual(s2.get_speed(), 3)
        # s1 will also immediately take paralysis effect after getting attacked.
        self.assertEqual(s1.get_status_effect(), "Paralysis")
        self.assertEqual(s1.get_speed(), 3)

        RandomGen.set_seed(7986)
        b1 = Bulbasaur()
        b2 = Bulbasaur()
        b1.attack(b2)
        # b2 now is poisoned.
        self.assertEqual(b2.get_status_effect(), "Poison")
        b2.attack(b1)
        # b2 taking effect and lose 3 hp.
        self.assertEqual(b2.get_hp(), 10)

    def additional_evolution_tests(self):
        c = Charmander()
        self.assertEqual(c.can_evolve(), True)
        self.assertEqual(c.should_evolve(), True)
        new_c = c.get_evolved_version()
        self.assertIsInstance(new_c, Charizard)
        s = Squirtle()
        self.assertEqual(s.can_evolve(), True)
        self.assertEqual(s.should_evolve(), True)
        new_s = s.get_evolved_version()
        self.assertIsInstance(new_s, Blastoise)
        b = Bulbasaur()
        self.assertEqual(b.can_evolve(), True)
        self.assertEqual(b.should_evolve(), True)
        new_b = b.get_evolved_version()
        self.assertIsInstance(new_b, Venusaur)


