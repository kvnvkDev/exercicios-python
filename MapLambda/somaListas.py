

lista = [21, 5, 34, 8, 16, 7, 3]

lpar = list(map(lambda n: n if n % 2 == 0 else 0,lista))
limpar = list(map(lambda n: n if n % 2 != 0 else 0,lista))

print("lista par: " + str(sum(lpar)))
print("lista impar: " + str(sum(limpar)))