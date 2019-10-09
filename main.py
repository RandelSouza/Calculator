# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 03:44:21 2019

@author: randel
"""
from menu import Menu
from calculator import Calculator

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
        # Estado do programa principal
        self.running = True

        # Opção passada pelo usuário
        self.option = 0

        # Inicializando number1 e number2
        self.number1 = self.number2 = 0

        # Insanciar o Menu.
        self.menu = Menu()

        # Instanciar uma Calculadora.
        self.calculator = Calculator()

    def showMenu_and_getOption(self):
        '''
        Método que tem a função de mostrar as opções disponíveis
        e obter a opção desejada pelo usuário.
        '''
        self.menu.draw_menu()    
        self.option = int(raw_input("Choose an option: "))

    def treatOption_twoNumbers_input(self):
        '''
        Trata a entrada de dados dependendo da opção escolhida.
        Se não for modulo obtem-se o number1 e number2.
        Caso contrario só o number1.
        '''
        if self.option < 5:
            self.number1 = int(raw_input("Enter first number: "))
            self.number2 = int(raw_input("Enter second number: "))
        else:
            if self.option != 6:
                self.number1 = int(raw_input("Enter a number: "))
                    
    def calculate_result(self, option):
        '''
        Calcula o resultado da expresão da opção escolhida.
        '''
        result = 0
    
        if option == 1:
            result = self.calculator.add(self.number1, self.number2)            
        elif self.option == 2:
            result = self.calculator.subtract(self.number1, self.number2)
        elif self.option == 3:
            result = self.calculator.multiply(self.number1, self.number2)
        elif self.option == 4:
            result = self.calculator.division(self.number1, self.number2)
        elif self.option == 5:
            result = self.calculator.module(self.number1)        
        else:      
            result = "Exit..."
            self.running = False        
            
        return result
    
    def show_result(self, option):
        '''
        Mostra o resultado da expresão da opção escolhida (não é transparente).
        '''
        if option == 6:
            print "\n{}.\n".format(self.calculate_result(option))
        else:
            print "\nThe result was {}.\n".format(self.calculate_result(option))
                
    def treat_choice(self):        
        '''
        Mostra de forma transparente o resultado da oção.
        '''
        self.show_result(self.option)                                
                        
    def treat_option(self):
        '''
        Trata da opção escolhida.
        '''
        if type(self.option) == int:                
            self.treatOption_twoNumbers_input()
            self.treat_choice()                
        else:
            print "invalid option!"
        
    def _run_(self):
        '''
        Método que rodara de fato o programa.
        '''
        # Execução principal
        while self.running:    
            self.showMenu_and_getOption()
            self.treat_option()
     
# Instanciando a classe Main
main = Main()   
             
# Executando a main
if __name__ == "__main__": 
    main._run_()
