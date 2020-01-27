# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 03:44:21 2019

@author: randel
"""
from menu import Menu

class Main(object):
    '''
    Classe Main, a denominada principal, pois será a que executara o programa em si.
    Chamando todos as demais classes, métodos e funções necessários, para o devido
    funcionamento do programa.
    '''
    def __init__(self):    
        '''
        Método construtor da classe Main.
        '''       
        self.running = True # Estado do programa principal        
        self.menu = Menu() # Instancia do Menu.
        
    def _run_(self):
        '''
        Método que rodara de fato o programa.
        '''
        # Execução principal
        while self.running:    
            self.menu.showMenu_and_getOption()           
            self.running = self.menu.treat_option()
                     
# Instanciando a classe Main
main = Main()   
             
# Executando a main
if __name__ == "__main__": 
    main._run_()
