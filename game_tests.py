import unittest


from game import calculate_bulls_and_cows, check_player_num, \
    str_process


class TestStringMethods(unittest.TestCase):

    def test_bulls_and_cows(self):
        assert calculate_bulls_and_cows("1234",
                                        "4321") == (0, 4)
        assert calculate_bulls_and_cows("4321",
                                        "4321") == (4, 0)

    def test_player_num(self):
        self.assertTrue(check_player_num("4321"))
        self.assertFalse(check_player_num("123"))
        self.assertFalse(check_player_num("a123"))

    def test_decorator(self):
        self.assertEqual(str_process("a#bc#d"), "bd")
        self.assertNotEqual(str_process("abc##d######"), "ad")


if __name__ == '__main__':
    unittest.main()
