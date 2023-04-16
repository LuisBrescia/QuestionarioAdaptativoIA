from flask import Flask, render_template, request
from problema import comparaRespostas

questionario = Flask(__name__, template_folder='../FrontEnd', static_folder='../FrontEnd')

@questionario.route("/", methods=['GET', 'POST'])
def inicia():
    return render_template('index.html')

@questionario.route("/problema", methods=['GET', 'POST'])
def problema():
    respostaAluno = request.form['respostaAluno'].lower()
    resultado, status, statusColor = comparaRespostas(respostaAluno)
    return render_template('problema.html', resposta=resultado, status=status, statusColor=statusColor)

if __name__ == '__main__':
    questionario.run(debug=True)