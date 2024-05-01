#ANHANGUERA EXERCICIO 2

'''
VARIAVEIS DO CASO

nm - nome do colaborador
sb - salario bruto
DD - DEDUÇÃO DO IMPOSTO EM PERCENTAGEM

'''
# PARAMENTRO DE ENTRADA:

nome_sobrenome = input('Digite seu nome: ')
print()

salario_bruto = int(input(f'Sr(a). {nome_sobrenome}, agora digite o valor do seu salário bruto: '))
print()

# SIMPLIFICAÇÃO DAS VARIAVEIS:

SALARIO_ATE_1903 = salario_bruto <= 1903
SALARIO_ATE_2826 = salario_bruto <= 2826
SALARIO_ATE_3751 = salario_bruto <= 3751
SALARIO_ATE_4664 = salario_bruto <= 4664
SALARIO_ACIMA_4664 = salario_bruto > 4664

DEDUCAO_DE_7_5 = salario_bruto / 100 * 7.5
DEDUCAO_DE_15 = salario_bruto / 100 * 15
DEDUCAO_DE_22_5 = salario_bruto / 100 * 22.5
DEDUCAO_DE_27_5 = salario_bruto / 100 * 27.5

# EXECUÇÃO DO CÓDIGO:

if SALARIO_ATE_1903:
    print(f'Você não precisa declarar o importo de renda!')
    print()

elif SALARIO_ATE_2826:
    DEDUCAO_DE_7_5
    print(f'Você teve uma DEDUÇAO DE {DEDUCAO_DE_7_5:.2f}\nvalor igual a 7,5% do seu {salario_bruto} salário bruto')
    print()
    
elif SALARIO_ATE_3751:
    DEDUCAO_DE_15
    print(f'Você teve uma DEDUÇAO DE {DEDUCAO_DE_15:.2f}\nvalor igual a 15% do seu {salario_bruto} salário bruto')
    print()
    
elif SALARIO_ATE_4664:
    DEDUCAO_DE_22_5
    print(f'Você teve uma DEDUÇAO DE {DEDUCAO_DE_22_5:.2f}\nvalor igual a 22,5% do seu {salario_bruto} salário bruto')
    print()

elif SALARIO_ACIMA_4664:
    DEDUCAO_DE_27_5
    print(f'Você teve uma DEDUÇAO DE {DEDUCAO_DE_27_5:.2f}\valor igual a 27,5% do seu {salario_bruto} salário bruto')
    print()
    