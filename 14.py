# 14. O Clube dos Rebeldes (Validação Inversa): O clube secreto aceita todo mundo, exceto quem se chamar "Voldemort".
# Pergunte o nome e use o operador de diferença (!=) para barrar o vilão e liberar os outros.

nome = input("Digite seu nome: ")

if nome != "Voldemort":
    print("Bem‑vindo ao clube dos rebeldes!")
else:
    print("Você está barrado, Voldemort!")

# 15. A Senha Sensível (Caps Lock): Peça a senha secreta. Adicione um elif para testar se o usuário digitou a senha certa, mas toda em MAIÚSCULAS,
# e imprima um aviso: "Quase! Mas você gritou a senha (Caps Lock). Tente minúsculas."

senha_correta = "senha123"
digitado = input("Digite a senha secreta: ")

if digitado == senha_correta:
    print("Senha correta! Acesso liberado.")
elif digitado == senha_correta.upper():
    print("Quase! Mas você gritou a senha (Caps Lock). Tente minúsculas.")
else:
    print("Senha errada, tente novamente.")


# 16. O Jogo Novo: Pergunte o valor da mesada guardada e o preço de um jogo que o aluno quer.
# Se o valor for suficiente, calcule e mostre o troco. Senão, diga exatamente quanto dinheiro falta.

mesada = float(input("Quanto você tem guardado de mesada? R$"))
preco_jogo = float(input("Quanto custa o jogo? R$"))

if mesada >= preco_jogo:
    troco = mesada - preco_jogo
    print(f"Você consegue comprar! O troco será de R${troco:.2f}")
else:
    falta = preco_jogo - mesada
    print(f"Falta R${falta:.2f} para comprar o jogo!")

# 17. A Feira de Poções Múltiplos Produtos: Mostre um menu com 3 poções e preços diferentes.
# Peça para o usuário digitar 1, 2 ou 3. Use if/elif/else para calcular o valor da compra baseado na escolha.

print("=== MENU POÇÕES ===")
print("1‑Poção de Cura R$12,00")
print("2‑Poção de Força R$18,00")
print("3‑Poção de Velocidade R$15,00")

escolha = int(input("Digite 1, 2 ou 3 para escolher sua poção: "))

if escolha == 1:
    valor = 12
elif escolha == 2:
    valor = 18
elif escolha == 3:
    valor = 15
else:
    valor = 0
    print("Escolha inválida!")

if valor != 0:
    print(f"Total da compra: R${valor:.2f}")

# 18. Imposto do Reino: Peça o valor do tesouro do herói.
# Se o tesouro for maior que 1000 moedas, ele recebe uma taxa de 10% de desconto.
# Se for menor ou igual a 1000, herói não paga imposto.

tesouro = float(input("Digite quantas moedas tem no tesouro: "))

if tesouro > 1000:
    desconto = tesouro * 0.10
    total = tesouro - desconto
    print(f"Desconto de 10% aplicado! Valor final: {total:.2f} moedas")
else:
    print(f"Sem imposto! Valor mantido: {tesouro:.2f} moedas")


# 19. Caixa Eletrônico da Mesada: O pai deu a mesada, mas perguntou: "Você tirou nota A em matemática?".
# Se a resposta for "sim", a mesada recebe um bônus de 20 moedas. Se for "não", recebe apenas o valor normal.

mesada = float(input("Digite o valor normal da mesada: "))
notaA = input("Você tirou nota A em matemática? (sim / não): ").lower()

if notaA == "sim":
    total = mesada + 20
else:
    total = mesada

print(f"Total final da mesada: R${total:.2f}")

# 20. A Cantina Inflacionada: Usuário informa o dinheiro que tem e escolhe Lanche (R$15), Suco (R$8) ou Combo (R$20).
# Use elif para identificar a escolha, verificar se tem dinheiro para pagar, liberar ou negar a venda.

print("=== CANTINA ===")
print("1‑Lanche R$15,00")
print("2‑Suco R$8,00")
print("3‑Combo R$20,00")

dinheiro = float(input("Quanto dinheiro você tem? R$"))
pedido = int(input("Digite 1‑Lanche / 2‑Suco / 3‑Combo: "))

if pedido == 1:
    preco = 15
elif pedido == 2:
    preco = 8
elif pedido == 3:
    preco = 20
else:
    preco = 0
    print("Pedido inválido")

if preco != 0:
    if dinheiro >= preco:
        troco = dinheiro - preco
        print(f" Venda liberada! Troco: R${troco:.2f}")
    else:
        print("Dinheiro insuficiente, venda negada")


# 21. O Chapéu Seletor Clássico: Pergunte: "Você prefere:1‑Livros, 2‑Esportes, 3‑Natureza, 4‑Pegadinhas?"
# Use if/elif/else para sortear o aluno em uma das 4 casas da escola de magia (ex: Corvinal, Grifinória, Lufa‑Lufa, Sonserina).

print("=== CHAPÉU SELETOR ===")
print("1‑Livros")
print("2‑Esportes")
print("3‑Natureza")
print("4‑Pegadinhas")

resposta = int(input("Digite o número da sua preferência: "))

if resposta == 1:
    casa = "Corvinal"
elif resposta == 2:
    casa = "Grifinória"
elif resposta == 3:
    casa = "Lufa‑Lufa"
elif resposta == 4:
    casa = "Sonserina"
else:
    casa = "Indefinida"

print(f"Você foi selecionado para a casa: {casa}")


# 22. O Bug do Chapéu: Melhore o exercício anterior.
# Adicione um else poderoso no final para caso o usuário digitar "5" ou qualquer letra errada,
# fazendo o chapéu responder: "Hmm, escolha inválida. O Chapéu está confuso!".

print("=== CHAPÉU SELETOR V2 ===")
print("1‑Livros")
print("2‑Esportes")
print("3‑Natureza")
print("4‑Pegadinhas")

resposta = input("Digite o número da sua preferência: ")

if resposta == "1":
    casa = "Corvinal"
elif resposta == "2":
    casa = "Grifinória"
elif resposta == "3":
    casa = "Lufa‑Lufa"
elif resposta == "4":
    casa = "Sonserina"
else:
    casa = "inválido"

if casa == "inválido":
    print("Hmm, escolha inválida. O Chapéu está confuso!")
else:
    print(f"Você foi selecionado para a casa: {casa}")

# 23. Seletor de Classes RPG: Faça duas perguntas.
# 1‑Prefere atacar de longe (1) ou de perto (2)?
# Dentro do primeiro if (longe), pergunte "Magia (A) ou Arco (B)?" para definir Mago ou Arqueiro.
# Dentro do else (perto), pergunte "Espada (A) ou Adagas (B)?" para definir Guerreiro ou Assassino. (Lógica de If aninhado).

pergunta1 = int(input("Prefere atacar de longe (1) ou de perto (2)? "))

if pergunta1 == 1:
    pergunta2 = input("Longe: Magia (A) ou Arco (B)? ").upper()
    if pergunta2 == "A":
        classe = "Mago"
    elif pergunta2 == "B":
        classe = "Arqueiro"
    else:
        classe = "Inválido"
else:
    pergunta2 = input("Perto: Espada (A) ou Adagas (B)? ").upper()
    if pergunta2 == "A":
        classe = "Guerreiro"
    elif pergunta2 == "B":
        classe = "Assassino"
    else:
        classe = "Inválido"

print(f"Sua classe de RPG é: {classe}")

# 24. O Termômetro de Humor: Pergunte ao usuário uma cor (Azul, Amarelo, Vermelho).
# O sistema deve responder como ele está se sentindo usando elif (Ex: Azul = Calmo, Vermelho = Zangado).

cor = input("Escolha uma cor: Azul / Amarelo / Vermelho: ").capitalize()

if cor == "Azul":
    humor = " Calmo"
elif cor == "Amarelo":
    humor = " Feliz"
elif cor == "Vermelho":
    humor = " Zangado"
else:
    humor = " Não consegui identificar seu humor"

print(f"Seu humor: {humor}")


# 25. O Guru dos Animais: Pergunte a idade e se ele prefere gatos ou cachorros.
# Crie 4 respostas possíveis combinando os dados (Ex: "Jovem e prefere gatos", "Adulto e prefere cachorros", etc).

idade = int(input("Digite sua idade: "))
animal = input("Prefere gatos ou cachorros? ").lower()

if idade < 18:
    if animal == "gatos":
        frase = "Jovem e prefere gatos"
    elif animal == "cachorros":
        frase = "Jovem e prefere cachorros"
    else:
        frase = "Animal inválido"
else:
    if animal == "gatos":
        frase = "Adulto e prefere gatos"
    elif animal == "cachorros":
        frase = "Adulto e prefere cachorros"
    else:
        frase = "Animal inválido"

print(frase)


# 26. O Radar de Velocidade: Pergunte a velocidade do carro (número).
# Se for menor ou igual a 100: "Siga em paz!".
# Se entre 100 e 200: "Multa gravíssima de 1000!".
# Se maior que 200: "Multa gravíssima de 2000 e carteira apreendida".

velocidade = float(input("Digite a velocidade do carro: "))

if velocidade <= 100:
    print("Siga em paz!")
elif velocidade > 100 and velocidade <= 200:
    print("Multa gravíssima de 1000!")
else:
    print("Multa gravíssima de 2000 e carteira apreendida")


# 27. O Sistema Escolar (Calculadora de Notas): Peça as notas de duas provas.
# Calcule a média. Se média >= 7: Aprovado. Se >= 5 e < 7: Recuperação.
# Se média < 5: Reprovado.

nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Média: {media:.2f} — Aprovado")
elif media >= 5:
    print(f"Média: {media:.2f} — Recuperação")
else:
    print(f"Média: {media:.2f} — Reprovado")


# 28. A Máquina do Tempo: Peça para o usuário digitar um ano.
# Se ano menor que 2000: "Você está no passado!".
# Se igual a 2026: "Você está no presente!".
# Se maior que 2026: "Você está no futuro!".

ano = int(input("Digite o ano: "))

if ano < 2000:
    print("Você está no passado!")
elif ano == 2026:
    print("Você está no presente!")
else:
    print("Você está no futuro!")


# 29. O Enigma da Esfinge: Faça uma conta matemática surpresa (ex: 15 * 3).
# Peça o valor usando input. Se acertar, ganha o tesouro. Senão, perde 50 de vida.

resposta_correta = 45
chute = int(input("Quanto é 15 multiplicado por 3? "))

if chute == resposta_correta:
    print("Parabéns! Você ganhou o tesouro")
else:
    print("Errou! Perdeu 50 pontos de vida")


# 30. DESAFIO FINAL: A Taverna do Dragão
# Passo 1: Pede senha secreta para entrar. Errou → programa acaba.
# Passo 2: Se acertou, pede idade. Menor de 13 → sai. Maior/igual 13 continua.
# Passo 3: Taverneiro pergunta personalidade, escolhe item de sorteio.
# Passo 4: Calculadora de mesada para ver se tem dinheiro para comprar o item sorteado.

# PASSO 1
senha = input("Digite a senha secreta para entrar na Taverna: ")
if senha != "dragao123":
    print("Senha errada! Você foi expulso da Taverna.")

else:
    # PASSO 2
    idade = int(input("Digite sua idade: "))
    if idade < 13:
        print("Idade insuficiente para ficar na Taverna. Saia!")

    else:
        # PASSO 3
        print("Escolha sua personalidade:")
        print("1‑Corajoso")
        print("2‑Cauteloso")
        escolha = int(input("Digite 1 ou 2: "))

        if escolha == 1:
            preco_item = 30
            nome_item = "Espada Mágica"
        elif escolha == 2:
            preco_item = 20
            nome_item = "Poção de Cura"
        else:
            preco_item = 0
            nome_item = "Nenhum item"

        # PASSO 4
        if preco_item != 0:
            mesada = float(input(f"O item sorteado é {nome_item}, custa R${preco_item}. Digite quanto você tem de mesada: "))
            if mesada >= preco_item:
                troco = mesada - preco_item
                print(f"Compra aprovada! Você levou {nome_item}. Troco R${troco:.2f}")
            else:
                print(f"Falta dinheiro para comprar {nome_item}")
        else:
            print("Escolha de personalidade inválida")
