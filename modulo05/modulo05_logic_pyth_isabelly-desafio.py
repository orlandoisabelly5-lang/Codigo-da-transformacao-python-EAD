usuarios_cadastrados = {
    "admin": "1234",
    "Leandro": "Doritin525$",
    "Daniel": "Vocacao2026"
}

def validar_login(usuario, senha, base_dados):
    if usuario in base_dados:
        if base_dados[usuario] == senha:
            return True
    return False

print("--- SISTEMA DE LOGIN ---")
usuario_input = input("Digite o nome de usuário: ")
senha_input = input("Digite a senha: ")

if validar_login(usuario_input, senha_input, usuarios_cadastrados):
    print(f"Bem-Vindo A Plataforma Da Vocação, {usuario_input}!")
else:
    print("Acesso negado! Usuário ou senha incorretos.")