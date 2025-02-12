import unittest
from src.trip_service import calculate_cost, apply_vat

class TestTripService(unittest.TestCase):

    def test_calculate_cost(self):
        """Prueba que el cálculo del costo sea correcto."""
        self.assertAlmostEqual(calculate_cost(10, 20), 1.2)
        self.assertAlmostEqual(calculate_cost(0, 0), 0.0)
        self.assertAlmostEqual(calculate_cost(30, 15), 1.35)

    def test_apply_vat(self):
        """Prueba que el IVA se aplique correctamente."""
        self.assertAlmostEqual(apply_vat(10), 12.1)
        self.assertAlmostEqual(apply_vat(0), 0.0)
        self.assertAlmostEqual(apply_vat(100), 121.0)

if __name__ == '__main__':
    unittest.main()
