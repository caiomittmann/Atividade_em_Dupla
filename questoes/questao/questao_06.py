class GaleriaAlienigena:
    def __init__(self, nome_galeria, obras):
        self.nome_galeria = nome_galeria
        self.obras = obras

    def adicionar_item(self, nome, valor):
        if nome != "" and valor > 0:
            self.obras.append(nome + ":" + str(valor))
            print("Obra adicionada!")
        else:
            print("Dados inválidos.")

    def listar_itens(self):
        print("Obras cadastradas:")
        for obra in self.obras:
            print("-", obra)

    def calcular_total(self):
        total = 0

        for obra in self.obras:
            dados = obra.split(":")
            valor = float(dados[1])
            total += valor

        return total

    def encontrar_item_mais_valioso(self):
        maior_nome = ""
        maior_valor = 0

        for obra in self.obras:
            dados = obra.split(":")
            nome = dados[0]
            valor = float(dados[1])

            if valor > maior_valor:
                maior_valor = valor
                maior_nome = nome

        return maior_nome + " (" + str(maior_valor) + ")"

    def classificar_colecao(self):
        total = self.calcular_total()

        if total < 500:
            return "Galeria comum"
        elif total <= 1500:
            return "Galeria rara"
        else:
            return "Galeria intergaláctica"

    def exibir_relatorio(self):
        print("=== RELATÓRIO DA GALERIA ===")
        print("Nome da galeria:", self.nome_galeria)
        print("Total de raridade:", self.calcular_total())
        print("Obra mais rara:", self.encontrar_item_mais_valioso())
        print("Classificação:", self.classificar_colecao())



galeria = GaleriaAlienigena(
    "Museu de Andrômeda",
    ["Cristal Azul:300", "Escultura Quântica:800"]
)

galeria.adicionar_item("Pintura Estelar", 600)

galeria.listar_itens()

print("Total:", galeria.calcular_total())

galeria.exibir_relatorio()