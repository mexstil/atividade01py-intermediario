13. Segurança Dupla (If Aninhado): Crie um sistema bancário. Primeiro, ele pede a senha de letras.
# Se acertar, ele pede o PIN de 4 números. Só imprima "Acesso ao Cofre Liberado" se ele acertar as duas coisas (uma dentro da outra).

senha_letras = input("Digite a senha de letras: ")

if senha_letras == "Voldemort":
    pin = input("Digite o PIN de 4 números: ")
    if pin == "1234":
        print("Acesso ao Cofre Liberado")
    else:
        print("PIN errado! Acesso negado.")
else:
    print("Senha de letras errada! Acesso negado.")
