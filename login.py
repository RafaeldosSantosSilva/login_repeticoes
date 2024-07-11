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
print('----------------------- MODO 2 -----------------------')

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




print('----------------------- MODO 3 -----------------------')

import string

def verifica_senha(senha):
    # Requisitos
    req_letra_minuscula = set(string.ascii_lowercase + 'áàãâéèêíìóòõôúùûüä')
    req_letra_maiuscula = set(string.ascii_uppercase)
    req_numeros = set(string.digits)
    req_caracteres_especiais = set(string.punctuation + 'ç')

    # Flags de verificação
    tem_8_digitos = len(senha) >= 8
    tem_minuscula = any(char in req_letra_minuscula for char in senha)
    tem_maiuscula = any(char in req_letra_maiuscula for char in senha)
    tem_numero = any(char in req_numeros for char in senha)
    tem_especial = any(char in req_caracteres_especiais for char in senha)

    # Contagem total de requisitos atendidos
    total_atendidos = sum([tem_8_digitos, tem_minuscula, tem_maiuscula, tem_numero, tem_especial])

    # Verificação da força da senha
    if tem_8_digitos and total_atendidos <= 2:
        return 'Senha fraca'
    elif tem_8_digitos and total_atendidos <= 4:
        return 'Senha razoável'
    elif tem_8_digitos and total_atendidos > 4:
        return 'Senha forte'
    else:
        return 'Senha muito curta'

# Loop para testar senhas até que uma senha forte seja fornecida
while True:
    senha = input('Digite sua senha: ')
    resultado = verifica_senha(senha)
    print(resultado)
    if resultado == 'Senha forte':
        break


        
