# Classe Mãe (Superclasse)
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.marca} {self.modelo} foi ligado.")
        else:
            print(f"O {self.marca} {self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O {self.marca} {self.modelo} foi desligado.")
        else:
            print(f"O {self.marca} {self.modelo} já está desligado.")

    def exibir_informacoes(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}")


# Classe Filha (Subclasse) que herda de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, quantidade_portas, tipo_combustivel):
        # Chama o construtor da classe pai (Veiculo)
        super().__init__(marca, modelo, ano)
        self.quantidade_portas = quantidade_portas
        self.tipo_combustivel = tipo_combustivel

    # Método específico da classe Carro
    def abrir_porta_malas(self):
        print(f"O porta-malas do {self.modelo} foi aberto.")

    # Sobrescrevendo o método da classe pai (Polimorfismo)
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Portas: {self.quantidade_portas} | Combustível: {self.tipo_combustivel}")


# Classe Filha de um Carro Elétrico (Herança em cadeia)
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, quantidade_portas, capacidade_bateria):
        # Para carro elétrico, definimos o combustível automaticamente como 'Elétrico'
        super().__init__(marca, modelo, ano, quantidade_portas, tipo_combustivel="Elétrico")
        self.capacidade_bateria = capacidade_bateria  # em kWh

    def carregar_bateria(self):
        print(f"Carregando a bateria de {self.capacidade_bateria} kWh do {self.modelo}...")


# ==========================================================
# 🧪 TESTANDO O CÓDIGO
# ==========================================================

if __name__ == "__main__":
    print("--- 🚗 Carro a Combustão ---")
    carro_comum = Carro(marca="Toyota", modelo="Corolla", ano=2023, quantidade_portas=4, tipo_combustivel="Flex")
    carro_comum.exibir_informacoes()
    carro_comum.ligar()
    carro_comum.abrir_porta_malas()

    print("\n--- ⚡ Carro Elétrico ---")
    carro_eletrico = CarroEletrico(marca="Tesla", modelo="Model 3", ano=2024, quantidade_portas=4, capacidade_bateria=75)
    carro_eletrico.exibir_informacoes()
    carro_eletrico.ligar()
    carro_eletrico.carregar_bateria()