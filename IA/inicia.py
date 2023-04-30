from flask import Flask, render_template, request, session
from problema import comparaRespostas
from seleciona_questao import selecionaQuestao
from perguntas import perguntas
import random

# * Cria o app
questionario = Flask(__name__, template_folder='../FrontEnd', static_folder='../FrontEnd')

# * Rota inicial
@questionario.route("/", methods=['GET', 'POST'])
def inicia():
    # > Código para zerar a lista de questões selecionadas
    # session['selecionadas'] = []
    return render_template('index.html')

# * Rota para cada questão
@questionario.route("/problema<numeroQuestao>", methods=['GET', 'POST'])
def problema(numeroQuestao):
    if request.method == 'POST':
        respostaAluno = request.form['respostaAluno']
        script = f"localStorage.setItem('resposta{numeroQuestao}', '{respostaAluno}');"
    else:
        respostaAluno = ''

    # > Código para gerar uma questão aleatória
    # questao = selecionaQuestao()
    
    caminhoRespostaIA = f"Respostas/resposta{numeroQuestao}.txt"
    resultado, status = comparaRespostas(respostaAluno, caminhoRespostaIA)
    
    return render_template('problema.html', resposta=resultado, status=status, questao=numeroQuestao, 
    respostaAluno=respostaAluno, pergunta=perguntas[f'pergunta{numeroQuestao}'])

# > Rota para a página de resultados
@questionario.route("/resultados", methods=['GET'])
def resultado():    
    return render_template('resultado.html')


# * Caso o arquivo seja executado diretamente
if __name__ == '__main__':
    questionario.run(debug=True)