# -*- coding: utf-8 -*-
import math
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
        Ao adicionar novas funcionalidades, sempre adicionar a nova função
        antes da função exit.
        '''
        self.functions = []
        self.order = 0
        
        self.add_function('add', self.add, 2)
        self.add_function('subtract', self.subtract, 2)
        self.add_function('multiply', self.multiply, 2)
        self.add_function('division', self.division, 2)
        self.add_function('module', self.module, 1)
        self.add_function('square root', self.square_root, 1)
        self.add_function('power', self.power, 2)
        self.add_function('raise to the square', self.raise_to_the_square, 1)
        self.add_function('exit', False, 0)
        
    def add_function(self, name_function, function, number_params):    
        self.order += 1
        self.functions.append({'name' : name_function, 'function' : function, 'order' : self.order, 'number_params' : number_params})        
        
    def add(self, numbers):        
        '''
        Método add, encarregado de retornar a soma de dois números.
        '''
        return numbers[0] + numbers[1]
    
    def subtract(self, numbers):
        '''
        Método subtract, encarregado de retornar a subtração de dois números.
        '''
        return numbers[0] - numbers[1]
    
    def multiply(self, numbers):
        '''
        Método multiply, encarregado de retornar a multiplicação de dois números.
        '''
        return numbers[0] * numbers[1]
    
    def division(self, numbers):
        '''
        Método division, encarregado de retornar a divisão de dois números.
        '''        
        if numbers[0] == 0 or numbers[1] == 0:
            return 0
        return numbers[0] / numbers[1]
    
    def module(self, numbers):
        '''
        Método module, encarregado de retornar o modulo de um número.
        '''
        if numbers[0] < 0:
            return numbers[0] * -1
        return numbers[0]
    
    def square_root(self, numbers):
        '''
        Método square_root, encarregado de retornar a raiz quadrada de um número.
        '''
        return math.sqrt(numbers[0])    
    
    def power(self, numbers):
        '''
        Método power, encarreado de retornar a potência de um número n1 elevado a outro número n2.        
        '''
        return numbers[0] ** numbers[1]        
    
    def raise_to_the_square(self, numbers):
        '''
        Método raise to the square, encarregado de retornar o quadrado de um número.
        '''
        return numbers[0] ** 2