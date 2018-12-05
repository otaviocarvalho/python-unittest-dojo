import unittest
import calculadora 

class TesteCalculatora(unittest.TestCase):
    def test_incrementar(self):
        resultado_do_calculo = calculadora.incrementar(3)
        resultado_esperado = 4
        self.assertEqual(resultado_do_calculo, resultado_esperado)

    def test_decrementar(self):
        self.assertEqual(calculadora.decrementar(3), 2)

if __name__ == '__main__':
    unittest.main()