def TipoDeCalculo(operacao, calculo, n1, n2):
    if calculo == 'simples':
        return scalculo(operacao, n1, n2)
    elif calculo == 'avançado':
        return acalculo(operacao, n1, n2)
    else:
        return "nao existe esse tipo de cálculo"

def scalculo(soperacao, n1, n2):
    if soperacao == '+' :
        print(n1 + n2)
        return
    elif soperacao == '-':
        print(n1 - n2)
        return
    elif soperacao == 'x':
        print(n1 * n2)
        return
    elif soperacao == '/':
        print(n1 / n2)
        return
    else:
        return 'Operação inválida'

def acalculo(aoperacao, n1, n2):
    if aoperacao == 'potência':
        print(n1 ** n2)
        return
    elif aoperacao == 'raiz':
        print(n1 ** (1/n2))
        return
    else:
        return 'Operação inválida'

tipocalculo = input('Digite o tipo de cálculo simples ou avançado: ')
tipooperacao = input('Digite a operação: ')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
TipoDeCalculo(tipooperacao, tipocalculo, n1, n2)