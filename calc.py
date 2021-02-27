
#crio uma função para o ato de calcular e chamo ela lá no final do meu código.
def calcular():

    # aqui vou criar uma variável operação que terá um input com
    # as opções para o usuário. Ele vai digitar o símbolo
    # da operação desejada e depois os números.
    # aspas triplas criam uma string multi linhas.
    operacao = input('''
Por favor escolha a operação que tu deseja:
    + adição
    - subtração
    * multiplicação
    / divisão
    ''')

    # input aceita qualquer coisa entendendo tudo como string
    # para que o ususário só consiga entrar com números usamos o int...
    number_1 = int(input('Manda aí o primeiro número:'))
    number_2 = int(input('E agora o segundo:'))

    # aqui uso o método format para inserir os valores das variáveis no texto.
    # basicamente (e essa é uma das 3 formas possíveis de se fazer isso)
    # eu uso .format com 2 argumentos(meus números) que serão exibidos na ordem em 2 conjuntos de
    # colchetes vazios. isso fornece mais feedback ao usuário.

    # para determinar qual dos trechos de código abaixo vai ser
    # executado usaremos uma condicional baseado na nossa
    # variavel operacao:


    if operacao == '+':
        # adição:
        print('{} + {} = '.format(number_1, number_2))
        print(number_1+number_2)

    elif operacao == '-':
        # subtração:
        print('{} - {} = '.format(number_1, number_2))
        print(number_1-number_2)

    elif operacao == '*':
        # multiplicação:
        print('{} * {} = '.format(number_1, number_2))
        print(number_1*number_2)

    elif operacao == '/':
        # divisão:
        print('{} / {} = '.format(number_1, number_2))
        print(number_1/number_2)
    
    #e se o usuário não digitar um operador válido criei uma mensagem de
    #erro caso nenhuma das condições acima seja atendida.    
    else:
        print('Tu não digitou um operador válido. Tenta novamente.')
        calcular()

    #NÃO ESQUECER DA TABULAÇÃO!!!!
    


#vamos criar essa função para erguntar ao usuário se 
#ele quer fazer mais algum cálculo:
def maisUmaVez():
    calc_novamente = input('''
Quer fazer mais algum cálculo?
Digita S para sim e N para não...''')
    #aqui, para converter o s e o n em maiúsculas uso .upper()
    if calc_novamente.upper() == 'S':
        calcular()
    
    elif calc_novamente.upper() == 'N':
        print('Até mais!!!')
        
    else:
        print('''É S para sim e N para não! 
              Mas como tu é indeciso vou te dar mais uma chance ;-)''')
        maisUmaVez()
       
#no final chamo as funções de calcular e de perguntar se o user deseja mais algum cálculo.   
calcular()
maisUmaVez()
    
    