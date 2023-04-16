from flask import Flask, render_template, request
from problema import comparaRespostas

questionario = Flask(__name__, template_folder='../FrontEnd', static_folder='../FrontEnd')

@questionario.route("/", methods=['GET', 'POST'])
def inicia():
    return render_template('index.html')

@questionario.route("/problema", methods=['GET', 'POST'])
def problema():
    if request.method == 'POST':
        respostaAluno = request.form['respostaAluno']
    else:
        respostaAluno = ''

    resultado, status = comparaRespostas(respostaAluno)
    return render_template('problema.html', resposta=resultado, status=status)

if __name__ == '__main__':
    questionario.run(debug=True)