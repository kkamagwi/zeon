import unittest

sys.path.append(os.getcwd())
from main import *

Class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_rerturn_mass(self):
        self.assertEqual(nitro_salt(1000), 10)
        self.assertEqual(nitro_salt(1500), 15)
        self.assertEqual(nitro_salt(800), 8)

    def test_nitro_salt_returns_int(self):
        self.assertInstance(nitro_salt(1000), int)

    def nitro_salt_recives_str_return_int(self):
        self.assertEqual(nitro_salt('1000'), 10)

    def nitro_salt_recives_alpha_returns_zero(self):
        self.assertEqual(nitro_salt('abc'), 0)