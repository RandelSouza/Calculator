# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 00:51:06 2019

@author: randel
"""

class Calculator(object):
    '''
    Classe Calculadora, especializada em realizar as seguintes operações matemáticas:
    add - adição de dois números;
    subtract - subtração de dois números;
    multiply - multiplicação de dois números;
    module - modulo de um número;
    '''
    def __init__(self):
        '''
        Método construtor da classe calculator.
        Responsávél pela correta inicialização das variáveis, caso haja.
        '''
        pass
    
    def add(self, number1, number2):        
        '''
        Método add, encarregado de retornar a soma de dois números.
        '''
        return number1 + number2
    
    def subtract(self, number1, number2):
        '''
        Método subtract, encarregado de retornar a subtração de dois números.
        '''
        return number1 - number2
    
    def multiply(self, number1, number2):
        '''
        Método multiply, encarregado de retornar a multiplicação de dois números.
        '''
        return number1 * number2     
    
    def division(self, number1, number2):
        '''
        Método division, encarregado de retornar a divisão de dois números.
        '''        
        if number1 == 0 or number2 == 0:
            return 0
        return number1 / number2
    
    def module(self, number):
        '''
        Método module, encarregado de retornar o modulo de um número.
        '''
        if number < 0:
            return number * -1
        return number

# add more functiona gere.
