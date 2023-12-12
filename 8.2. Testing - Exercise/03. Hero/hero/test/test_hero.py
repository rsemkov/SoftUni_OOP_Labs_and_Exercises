from unittest import TestCase, main
from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self):
        self.hero = Hero("Goshko", 100, 100.0, 100.0)

    def test_correct_input(self):
        self.assertEqual("Goshko", self.hero.username)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(100.0, self.hero.damage)

    def test_battle_when_enemy_name_same_as_hero_name_expect_raise_error(self):
        enemy_hero = Hero("Goshko", 10, 1.0, 1.0)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_health_less_than_equal_to_zero_expect_raise_error(self):
        enemy_hero = Hero("Peshko", 10, 1.0, 1.0)
        self.hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_when_enemy_health_less_than_equal_to_zero_expect_raise_error(self):
        enemy_hero = Hero("Peshko", 10, 0.0, 1.0)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight Peshko. He needs to rest", str(ex.exception))

    def test_battle_with_outcome_draw_expect_return_draw_message(self):
        enemy_hero = Hero("Peshko", 10, 100.0, 10000.0)

        self.assertEqual("Draw", self.hero.battle(enemy_hero))

    def test_battle_with_outcome_hero_win_expect_return_win_message_and_level_health_damage_increase(self):
        enemy_hero = Hero("Peshko", 1, 1.0, 1.0)
        self.hero.health = 10000.0

        self.assertEqual("You win", self.hero.battle(enemy_hero))
        self.assertEqual(101, self.hero.level)
        self.assertEqual(10004.0, self.hero.health)
        self.assertEqual(105.0, self.hero.damage)

    def test_battle_with_outcome_hero_lose_expect_return_lose_message_and_level_health_damage_increase_for_enemy(self):
        enemy_hero = Hero("Peshko", 100, 11000.0, 100.0)

        self.assertEqual("You lose", self.hero.battle(enemy_hero))
        self.assertEqual(101, enemy_hero.level)
        self.assertEqual(1005.0, enemy_hero.health)
        self.assertEqual(105.0, enemy_hero.damage)

    def test_str_representation_expect_string_with_object_data(self):
        self.assertEqual("Hero Goshko: 100 lvl\nHealth: 100.0\nDamage: 100.0\n", self.hero.__str__())


if __name__ == "__main__":
    main()

#level, health, damage