class TorneioDeDrones:
    def __init__(self, nome_torneio, provas, bateria_inicial):
        self.nome_torneio = nome_torneio
        self.provas = provas
        self.bateria = bateria_inicial
        self.pontos = 0
        self.provas_concluidas = []

    def listar_provas(self):
        print("Provas disponíveis:")
        for i in range(len(self.provas)):
            print(
                i + 1,
                "-",
                self.provas[i]["nome"],
                "| Custo:",
                self.provas[i]["custo"],
                "| Pontos:",
                self.provas[i]["pontos"]
            )

    def tentar_prova(self, numero_prova):
        if numero_prova < 1 or numero_prova > len(self.provas):
            print("Erro: número de prova inválido.")
            return

        indice = numero_prova - 1
        prova = self.provas[indice]

        if prova["nome"] in self.provas_concluidas:
            print("Essa prova já foi concluída.")
            return

        if self.bateria >= prova["custo"]:
            self.bateria -= prova["custo"]
            self.pontos += prova["pontos"]
            self.provas_concluidas.append(prova["nome"])
            print("Prova concluída com sucesso!")
        else:
            print("Bateria insuficiente para realizar a prova.")

    def calcular_progresso(self):
        return len(self.provas_concluidas)

    def verificar_situacao(self):
        if len(self.provas_concluidas) == len(self.provas):
            return "Torneio concluído"
        elif self.bateria == 0:
            return "Torneio encerrado sem bateria"
        else:
            return "Torneio em andamento"



provas = [
    {"nome": "Corrida Aérea", "custo": 20, "pontos": 100},
    {"nome": "Desvio de Obstáculos", "custo": 30, "pontos": 150},
    {"nome": "Entrega de Carga", "custo": 25, "pontos": 120}
]

torneio = TorneioDeDrones("Drone Masters", provas, 60)

torneio.listar_provas()

torneio.tentar_prova(1)
torneio.tentar_prova(2)

print("Pontos:", torneio.pontos)
print("Progresso:", torneio.calcular_progresso())
print("Bateria restante:", torneio.bateria)
print("Situação:", torneio.verificar_situacao())