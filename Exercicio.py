from Classes import *

p1 = Pessoa("Maria", 70, 24)

acao_atual = ""

while True:
    if not acao_atual:
        escolha = int(input("1-Comer\n2-Andar\n3-Dormir\nEscolha uma opção: "))

        if escolha == 1:
            p1.comer()
            acao_atual = "comer"
        elif escolha == 2:
            p1.andar()
            acao_atual = "andar"
        elif escolha == 3:
            p1.dormir()
            acao_atual = "dormir"
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    else:
        continuar = input(f"Deseja parar de {acao_atual}? sim/nao: ")
        if continuar == "sim":
            if acao_atual == "comer":
                p1.pararComer()
            elif acao_atual == "andar":
                p1.pararAndar()
            elif acao_atual == "dormir":
                p1.pararDormir()
            acao_atual = None
            continue

        print(f"Você continua {acao_atual}...\n")

        if acao_atual == "comer":
            escolha = int(input("1-Comer\n2-Andar\n3-Dormir\nEscolha uma opção: "))
            if escolha == 2:
                print("Você não pode andar enquanto está comendo.")
            elif escolha == 3:
                print("Você não pode dormir enquanto está comendo.")
        elif acao_atual == "andar":
            escolha = int(input("1-Comer\n2-Andar\n3-Dormir\nEscolha uma opção: "))
            if escolha == 1:
                print("Você não pode comer enquanto está andando.")
            elif escolha == 3:
                print("Você não pode dormir enquanto está andando.")
        elif acao_atual == "dormir":
            escolha = int(input("1-Comer\n2-Andar\n3-Dormir\nEscolha uma opção: "))
            if escolha == 1:
                print("Você não pode comer enquanto está dormindo.")
            elif escolha == 2:
                print("Você não pode andar enquanto está dormindo.")

    continuar = input("Deseja continuar? sim/nao: ")
    if continuar != "sim":
        break
