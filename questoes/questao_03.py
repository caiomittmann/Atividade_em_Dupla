class RoboColetor:
    def __init__(self, nome, amostras, capacidade_maxima):
        self.nome = nome
        self.amostras = amostras
        self.capacidade_maxima = capacidade_maxima
    def adicionar_amostra(self, amostra):
        if amostra != "" and self.contar_amostras() < self.capacidade_maxima:
            self.amostras.append(amostra)
            return "amostra adicionada"
        return "não foi possível adicionar"
    def listar_amostras(self):
        print("Amostras coletadas:")
        for amostra in self.amostras:
            print(amostra)
    def contar_amostras(self):
        return len(self.amostras)
    def verificar_armazenamento(self):
        if self.contar_amostras() >= self.capacidade_maxima:
            return "armazenamento cheio"
        else:
            return "ainda possui espaço"
    def exibir_relatorio(self):
        print(f"Nome do robô: {self.nome}")
        print(f"Quantidade de amostras: {self.contar_amostras()}")
        print(f"Capacidade máxima: {self.capacidade_maxima}")
        print(f"Situação: {self.verificar_armazenamento()}")
