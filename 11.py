O Guardião Simples: Crie um programa que pergunte "Qual a palavra mágica?".
# Se a resposta for "Abre‑te Sésamo", imprima "A caverna se abriu!". Senão, imprima "A caverna continua fechada."

palavra_magica = input("Qual a palavra mágica? ")

if palavra_magica == "Abre‑te Sésamo":
    print("A caverna se abriu!")
else:
    print("A caverna continua fechada.")

# 12. A Guilda de Robótica (Verificação de Idade): Pergunte a idade do usuário.
# Se for maior ou igual a 14, diga "Bem‑vindo à equipe avançada!". Senão, diga "Faltam X anos para você entrar na equipe avançada!"

idade = int(input("Digite sua idade: "))

if idade >= 14:
    print("Bem‑vindo à equipe avançada!")
else:
    faltam = 14 - idade
    print(f"Faltam {faltam} anos para você entrar na equipe avançada!")
