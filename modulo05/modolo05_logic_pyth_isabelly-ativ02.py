def calcular_media(notas):
    if len(notas) == 0:
        return 0
    
    media = sum(notas) / len(notas)
    print(f"Média calculada: {media:.2f}")
    
    if media >= 6.0:
        print("Situação: Aprovado!")
    else:
        print("Situação: Reprovado!")


notas_aluno = [7.7, 8.0, 6.0]
print(f"Notas do aluno: {notas_aluno}")
calcular_media(notas_aluno)
def maior_menor(lista):
    if len(lista) == 0:
        return "A lista está vazia."
    
    maior = max(lista)
    menor = min(lista)
    
    return maior, menor

numeros = [10, 5, 83, 2, 45, 19]
maior_valor, menor_valor = maior_menor(numeros)

print(f"Lista de números: {numeros}")
print(f"O maior valor é: {maior_valor}")
print(f"O menor valor é: {menor_valor}")