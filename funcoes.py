import sys

def parImpar(num):
    return "par" if (num % 2 == 0) else "impar"

print("digite um numero")
scan = sys.stdin.readline()
scan = int(scan)
if scan < 0:
    print("Digite apenas números maiores que 0" )
else:
    print(parImpar(scan))

