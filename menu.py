# -*- coding: utf-8 -*-
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
        self.options = {
                        "ADD" : 1,
                        "SUBTRACT" : 2,
                        "MULTIPLY" : 3,
                        "DIVISION" : 4,
                        "MODULE" : 5,
                        "SQUARE ROOT" : 6,
                        "EXIT" : 7
                        }        
    
    def draw_menu(self):
        '''
        Método que mostra a lista de opções disponíveis.
        '''        
        
        for key, value in sorted(self.options.items(), key=lambda x: x[1]):
            print key," - ", value            