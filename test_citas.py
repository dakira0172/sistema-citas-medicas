
import unittest
from citas import SistemaCitas

class TestSistemaCitas(unittest.TestCase):

    def setUp(self):
        self.sistema = SistemaCitas()

    def test_reservar_cita(self):
        resultado = self.sistema.reservar(
            "Juan", "2026-11-10", "09:00"
        )
        self.assertTrue(resultado)

    def test_evitar_cita_duplicada(self):
        self.sistema.reservar(
            "Juan", "2026-11-10", "09:00"
        )

        resultado = self.sistema.reservar(
            "Maria", "2026-11-10", "09:00"
        )
        self.assertFalse(resultado)

    def test_paciente_vacio(self):
        resultado = self.sistema.reservar(
            "", "2026-11-10", "10:00"
        )
        self.assertFalse(resultado)

    def test_cancelar_cita(self):
        self.sistema.reservar(
            "Ana", "2026-11-10", "11:00"
        )
        self.assertTrue(
            self.sistema.cancelar("2026-11-10", "11:00")
        )

    def test_horario_disponible(self):
        self.assertTrue(
            self.sistema.disponible("2026-11-10", "12:00")
        )

if __name__ == "__main__":
    unittest.main()
