#Simulador de dado de 6faces
#Simular de um dado de 6faces, gerando valor de 1 até 6

import random

class Simulardado:
     def __init__(self):
        self.valor_minino = 1
        self.valor_maximo = 6
        self.frase = " Gostaria de gerar um valor para o dado? "

     def Iniciar(self):
        resposta = input(self.frase)
        try:
            if resposta == "sim" or resposta == "s":
                self.Valordodado()
            elif resposta == "não" or resposta == "n":
                print("Agradecemos a sua participação!")
            else:
                print("Digite sim ou não")
           
        except:
            print("Ocorreu um erro ao receber sua resposta")

    
     def Valordodado(self):
        print(random.randint(self.valor_minino,self.valor_maximo))

simulador = Simulardado()
simulador.Iniciar()


