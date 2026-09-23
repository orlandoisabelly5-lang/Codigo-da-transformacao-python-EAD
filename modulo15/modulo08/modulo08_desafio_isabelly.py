
import random
import time

class Carro:
    def __init__(self, nome, velocidade_max, aceleracao, consumo_combustivel, durabilidade):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.aceleracao = aceleracao
        self.consumo_combustivel = consumo_combustivel  # Litros por km/h acelerado
        self.durabilidade_max = durabilidade
        self.durabilidade = durabilidade
        
        self.velocidade_atual = 0
        self.distancia_percorrida = 0
        self.combustivel = 100.0  # Porcentagem (100%)
        self.nitro_disponivel = 1  # 1 uso de nitro por corrida

    def acelerar(self):
        if self.combustivel <= 0:
            print("⛽ Sem combustível! Você não pode acelerar.")
            return

        incremento = random.randint(self.aceleracao - 5, self.aceleracao + 5)
        self.velocidade_atual = min(self.velocidade_max, self.velocidade_atual + incremento)
        
        # Consumo proporcional à velocidade
        gasto = (self.velocidade_atual / 10) * (self.consumo_combustivel / 5)
        self.combustivel = max(0.0, self.combustivel - gasto)
        
        print(f"🚀 Você pisou no fundo! Velocidade atual: {self.velocidade_atual} km/h (Combustível: {self.combustivel:.1f}%)")

    def frear(self):
        reducao = random.randint(20, 40)
        self.velocidade_atual = max(0, self.velocidade_atual - reducao)
        print(f"🛑 Você pisou no freio. Velocidade atual: {self.velocidade_atual} km/h")

    def usar_nitro(self):
        if self.nitro_disponivel > 0:
            self.nitro_disponivel -= 1
            self.velocidade_atual = min(self.velocidade_max + 30, self.velocidade_atual + 50)
            self.combustivel = max(0.0, self.combustivel - 15)
            print(f"🔥 NITRO ATIVADO! Velocidade subiu para {self.velocidade_atual} km/h!")
        else:
            print("❌ Você já usou seu Nitro!")

    def reparar(self):
        if self.velocidade_atual > 0:
            print("⚠️ Você precisa parar o carro completamente (0 km/h) para fazer reparos!")
            return
        
        ganho_funilaria = 30
        self.durabilidade = min(self.durabilidade_max, self.durabilidade + ganho_funilaria)
        print(f"🔧 Pit Stop de emergência realizado! Durabilidade restaurada para: {self.durabilidade}/{self.durabilidade_max}")

    def atualizar_posicao(self):
        # Avança distância com base na velocidade
        self.distancia_percorrida += self.velocidade_atual / 10


def selecionar_carro():
    garagem = [
        Carro("Fusca Tunado", velocidade_max=140, aceleracao=15, consumo_combustivel=2, durabilidade=120),
        Carro("Sedan Esportivo", velocidade_max=190, aceleracao=22, consumo_combustivel=4, durabilidade=100),
        Carro("Superesportivo V8", velocidade_max=240, aceleracao=32, consumo_combustivel=7, durabilidade=70)
    ]

    print("==================================================")
    print("🚗 BEM-VINDO AO DESAFIO DE CORRIDA & SOBREVIVÊNCIA 🏎️")
    print("==================================================")
    print("\nEscolha seu veículo para a competição:\n")

    for idx, c in enumerate(garagem, 1):
        print(f"[{idx}] {c.nome}")
        print(f"    │ Velocidade Máx: {c.velocidade_max} km/h | Aceleração: {c.aceleracao}")
        print(f"    │ Consumo: {c.consumo_combustivel}/10 | Durabilidade: {c.durabilidade}\n")

    while True:
        try:
            escolha = int(input("Digite o número do seu carro (1-3): "))
            if 1 <= escolha <= len(garagem):
                return garagem[escolha - 1]
        except ValueError:
            pass
        print("Opção inválida! Escolha entre 1 e 3.")


def evento_aleatorio(carro):
    # Chance de evento ocorrer (40%)
    if random.random() > 0.40 or carro.velocidade_atual == 0:
        return

    eventos = ["oleo", "buraco", "radar", "combustivel_pista"]
    evento = random.choice(eventos)

    print("\n⚠️  EVENTO NA PISTA!")

    if evento == "oleo":
        print("🛢️ Mancha de óleo na pista! O carro derrapou!")
        dano = random.randint(10, 25)
        carro.durabilidade -= dano
        carro.velocidade_atual = max(0, carro.velocidade_atual - 30)
        print(f"   Dano sofrido: -{dano} de durabilidade. Velocidade caiu!")

    elif evento == "buraco":
        print("🕳️ Um grande buraco apareceu na sua frente!")
        dano = random.randint(15, 30)
        carro.durabilidade -= dano
        print(f"   Impacto forte! Durabilidade -{dano}.")

    elif evento == "radar":
        if carro.velocidade_atual > 110:
            print(f"📸 RADAR DA PISTA! Você passou a {carro.velocidade_atual} km/h e levou uma penalidade de tempo!")
            carro.velocidade_atual = max(0, carro.velocidade_atual - 40)
        else:
            print("📸 Radar detectado, mas você estava dentro do limite prudente. Passou limpo!")

    elif evento == "combustivel_pista":
        print("⛽ Você encontrou um galão de combustível na pista!")
        carro.combustivel = min(100.0, carro.combustivel + 20)
        print("   +20% de combustível recuperado!")


def iniciar_desafio():
    carro = selecionar_carro()
    DISTANCIA_TOTAL = 150.0  # Km até a linha de chegada
    rodada = 0

    print(f"\n🎮 Desafio iniciado com o **{carro.nome}**!")
    print(f"🎯 Meta: Percorrer {DISTANCIA_TOTAL} km sem quebrar ou ficar sem combustível!\n")

    while carro.distancia_percorrida < DISTANCIA_TOTAL:
        rodada += 1
        print("\n" + "="*45)
        print(f"📍 TURNO {rodada}")
        print(f"🏁 Progresso: {carro.distancia_percorrida:.1f} / {DISTANCIA_TOTAL} km")
        print(f"⏱️  Velocidade: {carro.velocidade_atual} km/h")
        print(f"⛽ Combustível: {carro.combustivel:.1f}% | 🛠️ Durabilidade: {carro.durabilidade}/{carro.durabilidade_max}")
        print("="*45)

        print("\nO que você deseja fazer?")
        print("[1] Acelerar 🚀")
        print("[2] Frear 🛑")
        print("[3] Usar Nitro 🔥")
        print("[4] Fazer Pit Stop (Reparar) 🔧")

        opcao = input("\nEscolha sua ação (1-4): ").strip()

        print("\n--- AÇÃO ---")
        if opcao == "1":
            carro.acelerar()
        elif opcao == "2":
            carro.frear()
        elif opcao == "3":
            carro.usar_nitro()
        elif opcao == "4":
            carro.reparar()
        else:
            print("⚠️ Ação inválida! Você perdeu o tempo de reação neste turno.")

        # Atualiza a posição do carro no turno
        carro.atualizar_posicao()

        # Ocorrência de eventos aleatórios
        evento_aleatorio(carro)

        # Checagens de Derrota
        if carro.durabilidade <= 0:
            print("\n💥 SEU CARRO QUEBROU E FOI DESTRUIDO!")
            print("❌ GAME OVER - Você não conseguiu terminar o desafio.")
            return

        if carro.combustivel <= 0 and carro.velocidade_atual == 0:
            print("\n⛽ SEU COMBUSTÍVEL ACABOU COMPLETAMENTE!")
            print("❌ GAME OVER - O carro ficou parado na pista.")
            return

        time.sleep(1)

    # Vitória
    print("\n" + "🎉"*15)
    print(f"🏆 PARABÉNS! Você cruzou a linha de chegada em {rodada} turnos!")
    print(f"🚗 Veículo: {carro.nome}")
    print(f"📊 Estado Final: Combustível {carro.combustivel:.1f}% | Durabilidade {carro.durabilidade}/{carro.durabilidade_max}")
    print("🎉"*15)


if __name__ == "__main__":
    iniciar_desafio()