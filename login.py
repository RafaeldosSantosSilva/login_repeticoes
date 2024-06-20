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