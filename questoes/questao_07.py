class ExpedicaoTemplo:
    def __init__(self, nome_expedicao, desafios, energia_inicial):
        self.nome_expedicao = nome_expedicao
        self.desafios = desafios
        self.energia = energia_inicial
        self.pontos = 0
        self.desafios_concluidos = []
    def listar_desafios(self):
        for i in range(len(self.desafios)):
            desafio = self.desafios[i]
            print(
                f"{i} - {desafio['nome']} | "
                f"Custo: {desafio['custo']} | "
                f"Recompensa: {desafio['energia']}"
            )
    def tentar_desafio(self, numero_desafio):
        if numero_desafio < 0 or numero_desafio >= len(self.desafios):
            print("Erro: desafio inválido.")
            return
        desafio = self.desafios[numero_desafio]
        if desafio in self.desafios_concluidos:
            print("Esse desafio já foi concluído.")
            return
        if self.energia >= desafio["custo"]:
            self.energia -= desafio["custo"]
            self.pontos += desafio["energia"]
            self.desafios_concluidos.append(desafio)
            print("Desafio concluído com sucesso!")
        else:
            print("Energia insuficiente.")
    def calcular_progresso(self):
        return len(self.desafios_concluidos)
    def verificar_situacao(self):
        if self.calcular_progresso() == len(self.desafios):
            return "expedição concluída"
        elif self.energia == 0:
            return "expedição encerrada sem energia"
        else:
            return "expedição em andamento"
    def exibir_relatorio(self):
        print(f"Expedição: {self.nome_expedicao}")
        print(f"Energia restante: {self.energia}")
        print(f"Pontos: {self.pontos}")
        print(f"Desafios concluídos: {self.calcular_progresso()}")
        print(f"Situação: {self.verificar_situacao()}")