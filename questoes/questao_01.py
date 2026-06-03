class CapsulaDoTempo:
    def __init__(self, autor, mensagem, ano_abertura, ano_atual):
        self.autor = autor
        self.mensagem = mensagem
        self.ano_abertura = ano_abertura
        self.ano_atual = ano_atual
    def pode_abrir(self):
        if ano_atual >= ano_abertura:
            return("pode abrir")
        return("não pode abrir")
    def calcular_espera(self):
        anos_restantes = self.ano_abertura - self. ano_atual
        if anos_restantes >= 0:
            return(anos_restantes)
        else: return 0
    def classificar_espera(self):
         if self.calcular_espera() <= 0:
            return("pode abrir agora")
        elif self.calcular_espera() <= 3:
            return("espera curta")
        else: return("espera longa")
    def exibir_resumo(self):
        print(f"autor: {self.autor}")
        print(f"ano de abrtura: {self.ano_abertura}")
        print(f"situação da caixa: {self.classificar_espera()}")
        if self.calcular_espera == 0:
            print(f"mensagem: {self.mensagem}")