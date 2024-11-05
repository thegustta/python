# Inicializa uma lista vazia para armazenar os dados dos alunos
alunos = []

# Lê os nomes e notas de 5 alunos
for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append((nome, nota))  # Armazena o nome e a nota como uma tupla

# Exibe o nome e a nota de cada aluno
print("\nNomes e notas dos alunos:")
for aluno in alunos:
    nome, nota = aluno
    print(f"Nome: {nome} - Nota: {nota}")
