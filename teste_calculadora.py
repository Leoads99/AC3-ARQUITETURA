import Calculadora as C
from unittest import TestCase, main

class Testes(TestCase):
    def testar_soma(self):
        calculador = C.Calculadora()
        result = calculador.calcular(2, 3, 'somar')
        self.assertEqual(result, 5)

    def testar_multiplicacao(self):
        calculador = C.Calculadora()
        result = calculador.calcular(2, 5, 'multiplicar')
        self.assertEqual(result, 10)

    def testar_Divisao(self):
        calculador = C.Calculadora()
        result = calculador.calcular(2, 4, 'dividir')
        self.assertEqual(result, 0.5)

    def testar_subtracao(self):
        calculador = C.Calculadora()
        result = calculador.calcular(2, 4, 'subtrair')
        self.assertEqual(result, -2)


if __name__ == '__main__':
    main()

    