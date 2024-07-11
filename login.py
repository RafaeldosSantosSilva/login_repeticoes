# Projeto confirmação de senha
while(True):
    senha = input(f'Digite uma senha: ')
    confirmar_senha = input(f'Confirme sua senha: ')
    if (senha == confirmar_senha):
        print('Bem vindo e aproveite')
        break

    else:
        print('Senhas não são iguais.')

tentativas = 1

for i in range(1, 4):
    login = input(f'Digite sua senha: ')
    if (login == senha):
        print(f'Bem vindo')
        break
    
    print(f'“Senha incorretar. Você tem {tentativas} tentativas até o bloqueio.')
    tentativas += 1


while True:

    senha = input(('Digite sua senha: '))
    req_letra_minuscula = 'abcdefghiklmnopqrstuvxzçáàãâéèêíìóòõôúùûüä'
    req_letra_maiuscula = req_letra_minuscula.upper()
    req_numeros = '0123456789'

    tem_8_digitos = 0
    maiuscula = 0
    minuscula = 0
    numero = 0
    caracter_especial = 0
    if len(senha) >=8: 
        tem_8_digitos = 1
    for letra in senha:
        
            if letra in req_letra_minuscula:
                minuscula = 1

            elif letra in req_letra_maiuscula:
                maiuscula = 1
            
            elif letra in req_numeros:
                numero = 1

            else:
                caracter_especial = 1


print('---------------- MODO 2 ----------------')

    total_atendidos = tem_8_digitos + maiuscula + minuscula + numero + caracter_especial

        
    if len(senha) >= 8:
        if total_atendidos <= 2:
            print('Senha fulera')
        
        elif total_atendidos <= 4:
            print('Marromeno Marromeno')

        else:
            print('Ta de rocha pvt doido')
            break

    else:
        print('Tamanho da senha incorreto')

        
