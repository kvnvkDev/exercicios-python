import sys

print("digite o nome completo")
scan = sys.stdin.readline()

nome = scan.split(" ")

print("nome: %s %s"% (nome[0], nome[-1]))