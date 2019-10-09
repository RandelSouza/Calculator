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
        pass
    
    def draw_menu(self):
        '''
        Método que mostra a lista de opções disponíveis.
        '''
        print "ADD - 1"
        print "SUBTRACT - 2"
        print "MULTIPLY - 3"
        print "DIVISION - 4"        
        print "MODULE - 5"
        print "EXIT - 6"
