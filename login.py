import tkinter as tk
from tkinter import messagebox
import string

def verifica_senha(senha):
    # Requisitos
    req_letra_minuscula = set(string.ascii_lowercase + 'áàãâéèêíìóòõôúùûüä')
    req_letra_maiuscula = set(string.ascii_uppercase)
    req_numeros = set(string.digits)
    req_caracteres_especiais = set(string.punctuation + 'ç')

    # Verificações
    tem_8_digitos = len(senha) >= 8
    tem_minuscula = any(char in req_letra_minuscula for char in senha)
    tem_maiuscula = any(char in req_letra_maiuscula for char in senha)
    tem_numero = any(char in req_numeros for char in senha)
    tem_especial = any(char in req_caracteres_especiais for char in senha)

    # Contagem total de requisitos atendidos
    total_atendidos = sum([tem_minuscula, tem_maiuscula, tem_numero, tem_especial])

    # Verificação da força da senha
    if not tem_8_digitos:
        return 'Senha muito curta'
    elif total_atendidos <= 2:
        return 'Senha fraca'
    elif total_atendidos <= 3:
        return 'Senha razoável'
    else:
        return 'Senha forte'

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Login")
        self.geometry("500x300")

        self.senha = ""
        self.tentativas_restantes = 3

        self.create_widgets()

    def create_widgets(self):
        self.lbl_instruction = tk.Label(self, text="Crie e confirme sua senha")
        self.lbl_instruction.pack(pady=10)

        self.lbl_senha = tk.Label(self, text="Senha:")
        self.lbl_senha.pack()
        self.entry_senha = tk.Entry(self, show='*')
        self.entry_senha.pack()

        self.lbl_confirmar_senha = tk.Label(self, text="Confirme a Senha:")
        self.lbl_confirmar_senha.pack()
        self.entry_confirmar_senha = tk.Entry(self, show='*')
        self.entry_confirmar_senha.pack()

        self.btn_criar_senha = tk.Button(self, text="Criar Senha", command=self.criar_senha)
        self.btn_criar_senha.pack(pady=10)

    def criar_senha(self):
        senha = self.entry_senha.get()
        confirmar_senha = self.entry_confirmar_senha.get()

        if senha != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não são iguais!")
            return

        resultado = verifica_senha(senha)
        messagebox.showinfo("Força da Senha", f'Força da senha: {resultado}')

        if resultado == 'Senha forte':
            self.senha = senha
            self.login_screen()
        else:
            messagebox.showwarning("Aviso", "Por favor, crie uma senha mais forte.")

    def login_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.lbl_login_instruction = tk.Label(self, text="Digite sua senha para fazer login")
        self.lbl_login_instruction.pack(pady=10)

        self.entry_login = tk.Entry(self, show='*')
        self.entry_login.pack()

        self.btn_login = tk.Button(self, text="Login", command=self.fazer_login)
        self.btn_login.pack(pady=10)

    def fazer_login(self):
        login = self.entry_login.get()

        if login == self.senha:
            messagebox.showinfo("Sucesso", "Bem-vindo!")
            self.destroy()
        else:
            self.tentativas_restantes -= 1
            if self.tentativas_restantes > 0:
                messagebox.showerror("Erro", f"Senha incorreta. Você tem {self.tentativas_restantes} tentativa(s) restante(s).")
            else:
                messagebox.showerror("Bloqueado", "Sua conta foi bloqueada devido a múltiplas tentativas incorretas.")
                self.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
