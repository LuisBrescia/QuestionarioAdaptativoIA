from flask import Flask, render_template, request
from problema import comparaRespostas
from perguntas import perguntas

questionario = Flask(__name__, template_folder='../FrontEnd', static_folder='../FrontEnd')

@questionario.route("/", methods=['GET', 'POST'])
def inicia():
    return render_template('index.html')

@questionario.route("/problema<numeroQuestao>", methods=['GET', 'POST'])
def problema(numeroQuestao):
    if request.method == 'POST':
        respostaAluno = request.form['respostaAluno']
    else:
        respostaAluno = ''

    caminhoRespostaIA = f"Respostas/resposta{numeroQuestao}.txt"
    resultado, status = comparaRespostas(respostaAluno, caminhoRespostaIA)
    
    return render_template('problema.html', resposta=resultado, status=status, questao=numeroQuestao, 
    respostaAluno = respostaAluno, pergunta = perguntas[f'pergunta{numeroQuestao}'])

if __name__ == '__main__':
    questionario.run(debug=True)