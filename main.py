from leitor_csv import carregar_transacoes
from relatorio import gerar_resumo

def main():
    try:
        transacoes = carregar_transacoes("dados/extrato.csv")
        resumo = gerar_resumo(transacoes)

        print("Resumo Financeiro")
        print("-----------------")
        print(f"Total gasto: R$ {resumo['total']:.2f}")
        print(f"Quantidade de transações: {resumo['quantidade']}")
        print(f"Média por transação: R$ {resumo['media']:.2f}")

    except ValueError as erro:
        print("Erro ao processar o arquivo.")
        print(erro)

if __name__ == "__main__":
    main()
