import random

# cria uma lista vazia para armazenar as questões selecionadas
selecionadas = []

# função para selecionar uma questão aleatória que não tenha sido selecionada anteriormente
def selecionaQuestao():
    # cria uma lista com todas as possíveis questões
    possiveis_questoes = list(range(1, 11))
    
    # remove as questões já selecionadas da lista de possíveis questões
    for q in selecionadas:
        if q in possiveis_questoes:
            possiveis_questoes.remove(q)
    
    # escolhe uma questão aleatória da lista de possíveis questões
    questao = random.choice(possiveis_questoes)
    
    # adiciona a questão selecionada à lista de questões selecionadas
    selecionadas.append(questao)
    
    # retorna a questão selecionada como uma string
    return str(questao)