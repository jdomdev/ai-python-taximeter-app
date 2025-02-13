import unittest
from unittest.mock import patch
from src.trip_service import start_trip
from src.billing import calculate_cost, apply_vat

class TestTripService(unittest.TestCase):

    @patch('builtins.input', side_effect=['y', 'y', 'y', 'n'])  # Simula las respuestas del usuario
    @patch('src.billing.calculate_cost', return_value=10.0)  # Simula el cálculo del costo
    @patch('src.billing.apply_vat', return_value=12.1)  # Simula la aplicación del IVA
    def test_start_trip_end_trip(self, mock_apply_vat, mock_calculate_cost, mock_input):
        with patch('builtins.print') as mock_print:  # Mock para verificar la salida de print
            start_trip()

            # Verificar que la función de cálculo del costo fue llamada con los tiempos de espera y movimiento
            mock_calculate_cost.assert_called_with(0, 0)  # Ajusta estos valores si cambian en el código real

            # Verificar que el IVA se aplicó correctamente
            mock_apply_vat.assert_called_with(10.0)

            # Verificar las salidas esperadas
            mock_print.assert_any_call("Calculating trip cost...")
            mock_print.assert_any_call("Thank you for using the Taximeter App. Goodbye!")

    @patch('builtins.input', side_effect=['y', 'y', 'n', 'y'])  # Primero mueve, luego detiene, luego termina
    @patch('src.billing.calculate_cost', return_value=10.0)
    @patch('src.billing.apply_vat', return_value=12.1)
    def test_start_trip_move_and_stop(self, mock_apply_vat, mock_calculate_cost, mock_input):
        with patch('builtins.print') as mock_print:
            start_trip()

            # Verificar que el estado del taxi cambió de "detenido" a "en movimiento"
            mock_print.assert_any_call("Taxi is now moving...")
            mock_print.assert_any_call("Taxi is now stopped...")

            # Verificar que el cálculo del costo se hizo correctamente
            mock_calculate_cost.assert_called_with(0, 0)

            # Verificar que el IVA fue aplicado
            mock_apply_vat.assert_called_with(10.0)

            # Verificar la salida de finalización del viaje
            mock_print.assert_any_call("Thank you for using the Taximeter App. Goodbye!")

    @patch('builtins.input', side_effect=['n', 'n'])  # No mueve el taxi, lo mantiene detenido
    @patch('src.billing.calculate_cost', return_value=10.0)
    @patch('src.billing.apply_vat', return_value=12.1)
    def test_start_trip_no_move(self, mock_apply_vat, mock_calculate_cost, mock_input):
        with patch('builtins.print') as mock_print:
            start_trip()

            # Verificar que el taxi nunca comenzó a moverse
            mock_print.assert_any_call("Taxi is now stopped...")
            mock_print.assert_any_call("Calculating trip cost...")

    @patch('builtins.input', side_effect=['y', 'y', 'n'])  # Simula entradas para finalizar el viaje
    @patch('src.billing.calculate_cost', return_value=10.0)
    @patch('src.billing.apply_vat', return_value=12.1)
    def test_start_trip_no_new_trip(self, mock_apply_vat, mock_calculate_cost, mock_input):
        with patch('builtins.print') as mock_print:
            start_trip()

            # Verificar que la opción de no continuar con el viaje fue procesada correctamente
            mock_print.assert_any_call("Thank you for using the Taximeter App. Goodbye!")

if __name__ == '__main__':
    unittest.main()
