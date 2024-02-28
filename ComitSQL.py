import sqlite3

def criar_conexao(nome_banco):
    try:
        conexao = sqlite3.connect(nome_banco)
        return conexao
    except sqlite3.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

def cadastrar_cliente(conexao, nome, email):
    try:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO clientes (nome, email)
            VALUES (?, ?)
        """, (nome, email))
        conexao.commit()
        print("Cliente cadastrado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao cadastrar cliente:", e)

def main():
    conexao = criar_conexao("exemplo.db")
    if conexao:
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o email do cliente: ")
        cadastrar_cliente(conexao, nome, email)
        conexao.close()

if __name__ == "__main__":
    main()
