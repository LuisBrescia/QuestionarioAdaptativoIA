from flask import Flask, render_template, request
from problema import comparaRespostas
from perguntas import perguntas

# * Cria o app
questionario = Flask(__name__, template_folder='../FrontEnd', static_folder='../FrontEnd')

# * Rota inicial
@questionario.route("/", methods=['GET', 'POST'])
def inicia():
    return render_template('index.html')

# * Rota para cada questão
@questionario.route("/problema<numeroQuestao>", methods=['GET', 'POST'])
def problema(numeroQuestao):
    if request.method == 'POST':
        respostaAluno = request.form['respostaAluno']
    else:
        respostaAluno = ''

    caminhoRespostaIA = f"api/Respostas/resposta{numeroQuestao}.txt"
    resultado, status = comparaRespostas(respostaAluno, caminhoRespostaIA)
    
    return render_template('problema.html', resposta=resultado, status=status, questao=numeroQuestao, 
    respostaAluno = respostaAluno, pergunta = perguntas[f'pergunta{numeroQuestao}'])

# > Rota para a página de resultados

# * Caso o arquivo seja executado diretamente
if __name__ == '__main__':
    questionario.run(debug=True)