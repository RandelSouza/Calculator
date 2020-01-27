# -*- coding: utf-8 -*-
from calculator import Calculator
"""
Created on Wed Oct  9 03:28:17 2019

@author: randel
"""

class Menu(object):
    '''
    Classe Menu, especializada em mostrar as opções disponíveis.    
    '''
    def __init__(self):
        '''
        Construtor da classe Menu.
        '''
        # Opção passada pelo usuário.
        self.option = 0

        # Todas as funções implementadas em calculator.
        self.functions = Calculator().functions       
        self.params = []
        
    def draw_menu(self):
        '''
        Método que mostra a lista de opções disponíveis.
        
        for key, value in sorted(self.options.items(), key=lambda x: x[1]):
            print key," - ", value                
        '''                
        for function in self.functions:      
            print function['name'].upper(), ' - ', function['order']                    
            
    def showMenu_and_getOption(self):
        '''
        Método que tem a função de mostrar as opções disponíveis
        e obter a opção desejada pelo usuário.
        '''
        self.draw_menu()    
        self.option = int(raw_input("Choose an option: "))
        
    def treatOption_twoNumbers_input(self):
        '''
        Trata a entrada de dados dependendo da opção escolhida.
        Se não for modulo obtem-se o number1 e number2.
        Caso contrario só o number1.
        '''
        if self.option < len(self.functions):
            del self.params[:]
                        
            for function in self.functions:       
                if function['order'] == self.option:
                    for quantity_params in range(function['number_params']):                        
                        self.params.append( int(raw_input("Enter the number{}: ".format(quantity_params + 1))))
                    return self.calculate_result(function, self.params)       
        return False                                      
                                                             
    def calculate_result(self, function, params):
        '''
        Calcula o resultado da expresão da opção escolhida.
        '''
        if function['function'] != False:
            return function['function'](params)                    
        return False
    
    def show_result(self, result):
        '''
        Mostra o resultado da expresão da opção escolhida (não é transparente).
        '''
        if  (result != False) or (result == 0):
            print "\nThe result was {}.\n".format(result)     
            return True
        else:
            print "\n{}.\n".format("Exit...")    
            return False
                                            
    def treat_option(self):
        '''
        Trata da opção escolhida.
        '''
        if type(self.option) == int:                
            return self.show_result(self.treatOption_twoNumbers_input())
        else:
            print "invalid option!"        