import unittest
import lista_uteis

class TesteSomaLista(unittest.TestCase):
    def test_soma_com_um_unico_numero(self):
        lista_com_um_unico_numero = [1]
        resultado_soma = lista_uteis.soma(lista_com_um_unico_numero) 
        self.assertEqual(resultado_soma, 1, "Soma de um unico numero deve ser 1")

    def test_soma_com_multiplos_numeros(self):
        lista_com_multiplos_numeros = [1,2,3]
        resultado_soma = lista_uteis.soma(lista_com_multiplos_numeros) 
        self.assertEqual(resultado_soma, 6, "Soma de multiplos numeros deve ser 6")

if __name__ == '__main__':
    unittest.main()