'''

'''
import random
import time

# Códigos de cores ANSI para o Visual Studio
COR_RESET = "\033[0m"
COR_TITULO = "\033[1;35m"  # Roxo brilhante
COR_SUCESSO = "\033[1;32m" # Verde brilhante
COR_ERRO = "\033[1;31m"    # Vermelho brilhante
COR_AVISO = "\033[1;33m"   # Amarelo brilhante
COR_INFO = "\033[1;36m"    # Ciano brilhante
COR_CARTA = "\033[1;37m"   # Branco brilhante

def limpar_tela():
    print("\n" + "="*50 + "\n")

def desenhar_carta(texto_centro):
    """Desenha uma carta de baralho realista no terminal"""
    print(f"{COR_CARTA}┌─────────┐")
    print(f"│ 🃏      │")
    print(f"│  {str(texto_centro).center(5)}  │")
    print(f"│      🃏 │")
    print(f"└─────────┘{COR_RESET}")

def mini_jogo_cartas_adivinhacao():
    """Minigame onde o jogador tenta adivinhar a carta mágica entre 1 e 24 em 6 tentativas"""
    limite_inferior = 1
    limite_superior = 24
    carta_secreta = random.randint(limite_inferior, limite_superior)
    max_tentativas = 6
    
    print(f"{COR_AVISO}🎴 [MESA DO CASSINO MÍSTICO: DUELO DE CARTAS]{COR_RESET}")
    print(f"O Mestre de Cartas baralha o deck mágico e diz: 'Eu selecionei uma carta oculta entre {limite_inferior} e {limite_superior}.'")
    print(f"Você tem exatamente {COR_ERRO}{max_tentativas} tentativas{COR_RESET} para descobrir o valor da carta!\n")

    tentativas = 0
    while tentativas < max_tentativas:
        try:
            print(f"{COR_INFO}Tentativa {tentativas + 1} de {max_tentativas}{COR_RESET}")
            palpite_str = input("Qual o número da carta que você quer puxar/chutar? ").strip()
            palpite = int(palpite_str)
        except ValueError:
            print(f"{COR_ERRO}O Mestre ri: 'Isso não é um número de carta válido! Perdeu a chance desta jogada.'{COR_RESET}")
            tentativas += 1
            continue

        tentativas += 1

        if palpite == carta_secreta:
            print(f"\n{COR_SUCESSO}🎉 INCRÍVEL! A carta virou e revelou o número:{COR_RESET}")
            desenhar_carta(carta_secreta)
            print(f"{COR_SUCESSO}Você acertou em {tentativas} tentativa(s) e venceu a rodada de cartas!{COR_RESET}")
            return True
        elif palpite < carta_secreta:
            print(f"{COR_AVISO}📉 A carta oculta é MAIOR que {palpite}.{COR_RESET}\n")
        else:
            print(f"{COR_AVISO}📈 A carta oculta é MENOR que {palpite}.{COR_RESET}\n")

    print(f"\n{COR_ERRO}💀 Suas {max_tentativas} tentativas acabaram! Suas cartas se esvaziaram.{COR_RESET}")
    print("A carta oculta era:")
    desenhar_carta(carta_secreta)
    return False

def escolher_personagem():
    """Permite ao jogador escolher sua classe de RPG"""
    print(f"{COR_TITULO}=== ESCOLHA A SUA CLASSE DE HERÓI ==={COR_RESET}")
    print(f"{COR_INFO}1. Guerreiro{COR_RESET} (Resistente, começa com HP extra e 20 de ouro)")
    print(f"{COR_INFO}2. Mago{COR_RESET}      (Sábio, começa com 40 de ouro)")
    print(f"{COR_INFO}3. Ladino{COR_RESET}     (Ágil, começa com 30 de ouro)")
    
    while True:
        escolha = input(f"\n{COR_AVISO}Escolha sua classe (1-3): {COR_RESET}").strip()
        if escolha == "1":
            return "Guerreiro", 120, 20
        elif escolha == "2":
            return "Mago", 100, 40
        elif escolha == "3":
            return "Ladino", 90, 30
        else:
            print(f"{COR_ERRO}Opção inválida! Escolha 1, 2 ou 3.{COR_RESET}")

def iniciar_jogo():
    print(f"{COR_TITULO}=== RPG DE CARTAS: AS CRÔNICAS DO DECK MÁGICO ==={COR_RESET}")
    nome = input(f"{COR_INFO}Digite o nome do seu Herói: {COR_RESET}").strip()
    if not nome:
        nome = "Aventureiro"
        
    classe, hp, ouro = escolher_personagem()
    hp_maximo = hp
    
    print(f"\nBem-vindo à taverna, {COR_SUCESSO}{nome}{COR_RESET} o(a) {COR_AVISO}{classe}{COR_RESET}! Suas cartas estão prontas.")
    time.sleep(1)

    while hp > 0:
        limpar_tela()
        print(f"{COR_TITULO}--- STATUS: {nome.upper()} ({classe.upper()}) ---{COR_RESET}")
        print(f"❤️ HP: {COR_SUCESSO}{hp}/{hp_maximo}{COR_RESET} | 💰 Ouro: {COR_AVISO}{ouro}{COR_RESET}")
        print(f"\n{COR_INFO}Escolha sua ação na mesa de jogo:{COR_RESET}")
        print("1. Jogar Duelo de Cartas (Adivinhar carta de 1 a 24 / 6 tentativas)")
        print("2. Explorar o Salão do Baralho (Procurar moedas de ouro)")
        print("3. Visitar a Taverna (Recuperar 25 de HP - Custa 10 de ouro)")
        print("4. Abandonar a Mesa e Sair")
        
        escolha = input(f"\n{COR_INFO}Sua escolha (1-4): {COR_RESET}").strip()

        if escolha == "1":
            print(f"\n{nome} o(a) {classe} senta-se à mesa para o duelo de cartas...")
            venceu = mini_jogo_cartas_adivinhacao()
            if venceu:
                print(f"{COR_SUCESSO}🏆 Prêmio: Você ganhou 50 moedas de ouro na aposta!{COR_RESET}")
                ouro += 50
            else:
                print(f"{COR_ERRO}💥 Derrota na aposta: Você perdeu 35 de HP devido ao estresse do jogo!{COR_RESET}")
                hp -= 35
                if hp <= 0:
                    break
            input(f"\n{COR_AVISO}Pressione ENTER para continuar...{COR_RESET}")

        elif escolha == "2":
            print(f"\n{nome} vasculha os cantos da taverna...")
            time.sleep(1)
            evento = random.randint(1, 2)
            if evento == 1:
                achou = random.randint(10, 25)
                print(f"{COR_SUCESSO}💰 Sorte! Achou uma carteira caída com {achou} de ouro.{COR_RESET}")
                ouro += achou
            else:
                dano = random.randint(10, 20)
                print(f"{COR_ERRO}🍻 Um valentão te desafiou de surpresa e você perdeu {dano} de HP.{COR_RESET}")
                hp -= dano
            input(f"\n{COR_AVISO}Pressione ENTER para continuar...{COR_RESET}")

        elif escolha == "3":
            if ouro >= 10:
                ouro -= 10
                hp = min(hp_maximo, hp + 25)
                print(f"{COR_SUCESSO}💤 Você pagou 10 de ouro e descansou na estalagem. HP restaurado!{COR_RESET}")
            else:
                print(f"{COR_ERRO}❌ Ouro insuficiente! Você precisa de pelo menos 10 moedas.{COR_RESET}")
            input(f"\n{COR_AVISO}Pressione ENTER para continuar...{COR_RESET}")

        elif escolha == "4":
            print(f"\n{COR_INFO}Até mais, {nome}! Você deixou a mesa com {ouro} de ouro.{COR_RESET}")
            break
        else:
            print(f"{COR_ERRO}⚠️ Opção inválida! Escolha um número de 1 a 4.{COR_RESET}")
            input(f"\n{COR_AVISO}Pressione ENTER para continuar...{COR_RESET}")

    if hp <= 0:
        print(f"\n{COR_ERRO}{'='*50}")
        print(f"GAME OVER, {nome}. Você perdeu todas as apostas e sua energia acabou.")
        print(f"{'='*50}{COR_RESET}")

if __name__ == "__main__":
    iniciar_jogo()