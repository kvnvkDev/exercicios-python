import sys

nota = []
for i in range(4):
    print("digite um valor para nota " + str(i))
    scan = int(sys.stdin.readline())
    if scan < 0:
        print("Digite apenas números maiores que 0" )
    else:
        nota.append(scan)

total = 0
max = 0
min = 99
for i in range(4):
    if max < nota[i]:
        max = nota[i]
    if min > nota[i]:
        min = nota[i]
    total += nota[i]

print("Total: "+str(total))
print("Media: "+str(total / 4))
print("Mínimo: "+ str(min))
print("Máximo: "+ str(max))

