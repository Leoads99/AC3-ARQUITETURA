from abc import ABC, ABCMeta, abstractmethod


class Calculadora(object):
    
    def calcular(self, valorUm, valorDois, operador):
        fabricarOperacao = FabricarOperacao()
        operacao = fabricarOperacao.criar(operador)
        if operacao == None:
            return 0
        else:
            operacao = fabricarOperacao.criar(operador)
            resultado = operacao.executar(valorUm, valorDois)
            return resultado
    
class FabricarOperacao(metaclass= ABCMeta):
    
    def criar(self, operador):
        if operador == 'somar':
            return Soma()
        elif operador == 'subtrair':
            return Subtrair()
        elif operador == 'dividir':
            return Divisao()
        elif operador == 'multiplicar':
            return Multiplicar()
    
class Operacao(object):
    
    @abstractmethod
    def executar(self, valorUm, valorDois):
        return 
        
class Soma(Operacao):
    
    def executar(self, valorUm, valorDois):
        resultado = valorUm + valorDois
        return resultado
    
class Subtrair(Operacao):
    
    def executar(self, valorUm, valorDois):
        resultado =valorUm - valorDois
        return resultado
    
class Divisao(Operacao):
    
    def executar(self, valorUm, valorDois):
        resultado = valorUm / valorDois
        return resultado

class Multiplicar(Operacao):
    
    def executar(self, valorUm, valorDois):
        resultado = valorUm * valorDois
        return resultado

