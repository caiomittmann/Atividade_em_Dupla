class PortalDimensional:
    def __init__(self, nome, destino, energia_necessaria, energia_disponivel):
        self.nome = nome
        self.destino = destino
        self.energia_necessaria = energia_necessaria
        self.energia_disponivel = energia_disponivel

    def pode_abrir(self):
        if self.energia_disponivel >= self.energia_necessaria:
            return True
        else:
            return False

    def calcular_falta_energia(self):
        if self.pode_abrir():
            return 0
        else:
            return self.energia_necessaria - self.energia_disponivel

    def classificar_estabilidade(self):
        falta = self.calcular_falta_energia()

        if falta == 0:
            return "Portal estável"
        elif falta <= 20:
            return "Portal quase estável"
        else:
            return "Portal instável"

    def exibir_resumo(self):
        print("Nome do portal:", self.nome)
        print("Destino:", self.destino)
        print("Energia disponível:", self.energia_disponivel)
        print("Energia necessária:", self.energia_necessaria)
        print("Situação:", self.classificar_estabilidade())

        if not self.pode_abrir():
            print("Faltam", self.calcular_falta_energia(), "pontos de energia.")
        else:
            print("O portal pode ser aberto.")


portal = PortalDimensional("Portal Alpha", "Marte", 100, 85)

portal.exibir_resumo()