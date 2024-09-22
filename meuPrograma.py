import sys
import os

def operar(argumentos, id):
    # Encontrar a operação
    operacoes = {"+", "-", "*", "/"}
    operacao = next((arg for arg in argumentos if arg in operacoes), None)

    # Encontrar os valores
    numeros = [float(arg) for arg in argumentos if arg.replace('.', '', 1).isdigit()]

    if operacao is None or len(numeros) != 2:
        print("Argumentos inválidos!")
        return

    numero1, numero2 = numeros

    # Realizar a operação
    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        if numero2 == 0:
            print("Erro: Divisão por zero!")
            return
        resultado = numero1 / numero2

    print(f"Resultado da operação {id}: {resultado}")

def operacaoViaArgumento(argumentos):
    operar(argumentos[1:], 1)

def operacaoViaArquivo(nome_arquivo):
    args = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            try:
                quantidade_operacoes = int(arquivo.readline().strip())
            except ValueError:
                print("Erro: A primeira linha deve conter a quantidade de operações.")
                return
            
            for _ in range(quantidade_operacoes):
                linha = arquivo.readline().strip()
                if linha:
                    args.append(linha)
        
        for i in range(len(args)):
            args[i] = args[i].split(" ")
            operar(args[i], i + 1)
    else:
        print("Arquivo não encontrado!")

def main():
    argumentos = sys.argv
    if len(argumentos) < 2:
        print("Argumentos insuficientes!")
        sys.exit()

    if argumentos[1] == "matematica":
        operacaoViaArgumento(argumentos[1:])
    else:
        nome_arquivo = argumentos[1]
        operacaoViaArquivo(nome_arquivo)

if __name__ == "__main__":
    main()
