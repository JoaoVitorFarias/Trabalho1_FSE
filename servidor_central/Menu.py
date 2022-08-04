
import mensagem

class Menu:
    def __init__(self):
        self.opcao = 0

    def menu_principal(self):
        while True:
            print("===== MENU =====\n")
            print("1 - Monitoramento dos semáforos")
            print("2 - Acionamento do modos noturno ou de emergência\n")
            self.opcao  = int(input("Selecione uma das opções: "))
            if (self.opcao  == 1):
                self.painel_monitoramento()

            elif (self.opcao  == 2):
                self.menu_modos()
    
    def menu_modos(self):
        while True:
            print("===== MENU =====\n")
            print("1 - Modo noturno")
            print("2 - Modo emergência")
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
            print("===== MODO NOTURNO =====\n")
            print("1 - Todos cruzamentos")
            print("2 - Cruzamentos 1 e 2")
            print("3 - Cruzamentos 3 e 4")
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
            print("===== MODO EMERGÊNCIA =====\n")
            print("1 - Todos cruzamentos")
            print("2 - Cruzamentos 1 e 2")
            print("3 - Cruzamentos 3 e 4")
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
            print("Desativar modo noturno?")
            print("1 - Sim\n")
            opcao_destivar = int(input(""))
            if (opcao_destivar == 1):
                mensagem.enviar_mensagem(0, 0, self.opcao)
                self.menu_modo_noturno()

    def desativar_modo_emergencia(self):
        while True:
            print("Desativar modo de emergência?")
            print("1 - Sim\n")
            opcao_destivar = int(input(""))
            if (opcao_destivar == 1):
                mensagem.enviar_mensagem(0, 0, self.opcao)
                self.menu_modo_noturno()

    def painel_monitoramento(self):
        print("===== MONITORAMENTO =====\n")
        print("1 - Para sair do monitoramento\n")
        mensagem.acionar_monitoramento(1)

        while True:
            opcao_destivar = int(input(""))
            if (opcao_destivar == 1):
                mensagem.acionar_monitoramento(0)
                self.menu_principal()

    
    
    
    
