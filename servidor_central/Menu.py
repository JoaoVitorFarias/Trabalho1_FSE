
import mensagem

class Menu:
    def __init__(self):
        self.opcao = 0

    def menu_principal(self):
        while True:
            print("===== MENU =====\n\n")
            print("1 - Monitoramento dos semáforos\n")
            print("2 - Acionamento do modos noturno ou de emergência\n")
            self.opcao  = int(input("Selecione uma das opções: "))
            if (self.opcao  == 1):
                self.painel_monitoramento()

            elif (self.opcao  == 2):
                self.menu_modos()
    
    def menu_modos(self):
        while True:
            print("===== MENU =====\n\n")
            print("1 - Modo noturno\n")
            print("2 - Modo emergência\n")
            print("3 - Voltar\n")
            self.opcao = int(input("Selecione uma das opções: ")) 
            if (self.opcao == 1): 
                self.menu_modo_noturno()     
            elif (self.opcao == 2): 
                self.menu_modo_emergencia()
            elif(self.opcao == 3):
                self.menu_principal()
    
    def menu_modo_noturno(self):
        while True:
            print("===== MODO NOTURNO =====\n\n")
            print("1 - Todos cruzamentos\n")
            print("2 - Cruzamentos 1 e 2\n")
            print("3 - Cruzamentos 3 e 4\n")
            print("4 - Voltar\n")
            self.opcao = int(input("Selecione uma das opções: "))
            if (self.opcao == 1):
                mensagem.enviar_mensagem(1, 0, 1)
                self.desativar_modo_noturno()

            elif (self.opcao == 2):
                mensagem.enviar_mensagem(1, 0, 2)
                self.desativar_modo_noturno()

            elif (self.opcao == 3):
                mensagem.enviar_mensagem(1, 0, 3)
                self.desativar_modo_noturno()
                
            elif (self.opcao == 4):
                self.menu_modos()
            

    def menu_modo_emergencia(self):
        while True:
            print("===== MODO EMERGÊNCIA =====\n\n")
            print("1 - Todos cruzamentos\n")
            print("2 - Cruzamentos 1 e 2\n")
            print("3 - Cruzamentos 3 e 4\n")
            print("4 - Voltar\n")
            self.opcao = int(input("Selecione uma das opções: "))
            if (self.opcao == 1):
                mensagem.enviar_mensagem(0, 1, 1)
                self.desativar_modo_emergencia()

            elif (self.opcao == 2):
                mensagem.enviar_mensagem(0, 1, 2)
                self.desativar_modo_emergencia()

            elif (self.opcao == 3):
                mensagem.enviar_mensagem(0, 1, 3)
                self.desativar_modo_emergencia()
                
            elif (self.opcao == 4):
                self.menu_modos()
    
    def desativar_modo_noturno(self):
        while True:
            print("Desativar modo noturno\n\n")
            print("1 - Sim\n")
            opcao_destivar = int(input(""))
            if (opcao_destivar == 1):
                mensagem.enviar_mensagem(0, 0, self.opcao)
                self.menu_modo_noturno()

    def desativar_modo_emergencia(self):
        while True:
            print("Desativar modo de emergência\n\n")
            print("1 - Sim\n")
            opcao_destivar = int(input(""))
            if (opcao_destivar == 1):
                mensagem.enviar_mensagem(0, 0, self.opcao)
                self.menu_modo_noturno()

    def painel_monitoramento(self):
        print("Selecione a opção:\n\n")
        print("1 - Voltar para o Menu\n")
        mensagem.acionar_monitoramento(1)

        while True:
            opcao_destivar = int(input(""))
            if (opcao_destivar == 1):
                mensagem.acionar_monitoramento(0)
                self.menu_principal()

    
    
    
    
