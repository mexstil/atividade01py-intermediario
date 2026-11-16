# 12. A Guilda de Robótica (Verificação de Idade): Pergunte a idade do usuário.
# Se for maior ou igual a 14, diga "Bem‑vindo à equipe avançada!". Senão, diga "Faltam X anos para você entrar na equipe avançada!"

idade = int(input("Digite sua idade: "))

if idade >= 14:
    print("Bem‑vindo à equipe avançada!")
else:
    faltam = 14 - idade
    print(f"Faltam {faltam} anos para você entrar na equipe avançada!")
