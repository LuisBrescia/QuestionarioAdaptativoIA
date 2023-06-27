from flask import Flask, render_template, request, session
from problema import comparaRespostas
from perguntas import perguntas
import random

# * Cria o app
questionario = Flask(__name__, template_folder='../FrontEnd', static_folder='../FrontEnd')

# * Vetor com as questões
vetorQuestoes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# * Rota inicial
@questionario.route("/", methods=['GET', 'POST'])
def inicia():

    # ? Código para bagunçar a ordem das questões
    random.shuffle(vetorQuestoes)

    return render_template('index.html')

# * Rota para cada questão
@questionario.route("/problema<numeroQuestao>", methods=['GET', 'POST'])
def problema(numeroQuestao):
    if request.method == 'POST':
        respostaAluno = request.form['respostaAluno']
    else:
        respostaAluno = ''

    caminhoRespostaIA = f"Respostas/resposta{vetorQuestoes[int(numeroQuestao)-1]}.txt"
    resultado, status = comparaRespostas(respostaAluno, caminhoRespostaIA)
    
    return render_template('problema.html', resposta=resultado, status=status, questao=numeroQuestao, 
    respostaAluno=respostaAluno, pergunta=perguntas[f'pergunta{vetorQuestoes[int(numeroQuestao)-1]}'])

# * Rota para a página de resultados
@questionario.route("/resultados", methods=['GET'])
def resultado():    
    return render_template('resultado.html')


# * Caso o arquivo seja executado diretamente
if __name__ == '__main__':
    questionario.run(debug=False)

