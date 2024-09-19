from sys import stdin
from random import randint

op = True
tentativas = 5
pontos = []
tabPontos = {"5":100,"4":80,"3":50,"2":30,"1":10}
nivel = 1
num = 0

def menu():
    print("Bem vindo ao jogo. Escolha uma opção: ")
    print("1 = Iniciar\n"
          +"2 = Pontuação\n"
          +"3 = Encerrar"
          +"")
    select = stdin.readline().strip()
    match select:
        case '1':
            iniciar()
        case "2":
            pontuacao()
        case "3":
            fim()
        case _:
            print("selecione uma opção válida")
            return menu()

def iniciar():
    global nivel
    global tentativas
    global num
    global pontos
    print("ini")
    pontos = []
    num = gerarNum(nivel)
    while tentativas > 0:
        print(f"****************Nível {nivel}****************")
        numMax = 10*nivel
        print(f"Descubra o número aleatório de 1 a {numMax}\nVocê possui {tentativas} tentativas ")
        rodada = stdin.readline().strip()
        if rodada.isdigit:
            r = int(rodada)
            if r > 0 and r < numMax:
                
                if num == r:
                    print("Parabéns voce acertou")
                    p = calcPontos(str(tentativas))
                    print(f"Você ganhou {p} pontos")
                    tentativas = 5
                    nivel += 1
                    num = gerarNum(nivel)
                else:
                    print("Ops, não é esse número, tenta novamente")
                    tentativas -= 1
                
            else:
                print(f"Digite um número entre 1 e {numMax}")
        else:
            print(f"Digite um valor numérico. Tente adivinhar um valor entre 1 e {numMax}")
    print(f"Você perdeu. O número correto era {num}")
    tentativas = 5
    nivel = 1
    return ""



def calcPontos(t):
    global pontos
    global tabPontos
    pnt = tabPontos[t]
    pontos.append(pnt)
    return pnt

def gerarNum(n):
    return randint(1,10*n)

def pontuacao():
    global pontos
    print("Total de pontos: %d"% sum(pontos))

def fim():
    global op
    print("fim")
    op = False

while op:
    menu()