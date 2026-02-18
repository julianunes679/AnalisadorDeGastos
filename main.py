from leitor_csv import carregar_transacoes

def main():
    try:
        transacoes = carregar_transacoes("dados/extrato.csv")
        print("Arquivo carregado com sucesso.")
        print(transacoes)

    except ValueError as erro:
        print("Erro ao processar o arquivo.")
        print(erro)

if __name__ == "__main__":
    main()
