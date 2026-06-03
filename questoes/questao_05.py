class CofreDoDragao:
    def __init__(self, nome_dragao, tesouros):
        self.nome_dragao = nome_dragao
        self.tesouros = tesouros
    def adicionar_item(self, nome, valor):
        if nome != "" and valor > 0:
            item = {
                "nome": nome,
                "valor": valor
            }
            self.tesouros.append(item)
    def listar_itens(self):
        for item in self.tesouros:
            print(f"Nome: {item['nome']} | Valor: {item['valor']}")
    def calcular_valor_total(self):
        total = 0
        for item in self.tesouros:
            total += item["valor"]
        return total
    def encontrar_item_mais_valioso(self):
        if len(self.tesouros) == 0:
            return None
        mais_valioso = self.tesouros[0]
        for item in self.tesouros:
            if item["valor"] > mais_valioso["valor"]:
                mais_valioso = item
        return mais_valioso
    def classificar_colecao(self):
        total = self.calcular_valor_total()
        if total < 500:
            return "coleção pequena"
        elif total <= 1500:
            return "coleção respeitável"
        else:
            return "coleção lendária"
    def exibir_relatorio(self):
        print(f"Dragão: {self.nome_dragao}")
        print(f"Valor total: {self.calcular_valor_total()}")
        item = self.encontrar_item_mais_valioso()
        if item is not None:
            print(f"Item mais valioso: {item['nome']} ({item['valor']})")
        print(f"Classificação: {self.classificar_colecao()}")