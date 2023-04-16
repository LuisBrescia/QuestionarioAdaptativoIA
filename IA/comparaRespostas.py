from transformers import BertTokenizer, BertModel
from flask import Flask, render_template, request
import torch

import logging
logging.getLogger("transformers.modeling_utils").setLevel(logging.ERROR)



# Nome do meu site
questionario = Flask(__name__, template_folder='../FrontEnd', static_folder='../FrontEnd')

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Rota para a página inicial
@questionario.route("/", methods=['GET', 'POST'])

def comparaRespostas():

    respostaAluno = request.form['respostaAluno'].lower()
    # ! Descobrir porque não está funcionando sempre
    # respostaAluno = "Eu não sei"
    
    with open('Respostas/resposta1.txt', 'r') as resposta1:
        respostaIA = resposta1.read()

    tokenAluno = tokenizer.encode(respostaAluno, add_special_tokens=True)
    tokenIA = tokenizer.encode(respostaIA, add_special_tokens=True)

    inputs1 = torch.tensor([tokenAluno])
    inputs2 = torch.tensor([tokenIA])

    outputs1 = model(inputs1)
    outputs2 = model(inputs2)

    last_hidden_states1 = outputs1[0][:, 0, :]
    last_hidden_states2 = outputs2[0][:, 0, :]

    from torch.nn.functional import cosine_similarity
    similarity = cosine_similarity(last_hidden_states1, last_hidden_states2)
    
    x = similarity.item() 
    x = ((x + 1) / 2) * 100
    x = (x - 50) * 2

    print(respostaAluno)
    print(x)

    if x >= 60:
        status = "APROVADO"
        statusColor = 'green'
    else:
        status = "REPROVADO"
        statusColor = 'red'

    resultado = f"A similaridade entre as duas respostas é de: {x:.2f}%"

    return render_template('index.html', resposta=resultado, status=status, statusColor=statusColor)

# Caso esteja rodando o arquivo diretamente, execute o servidor
if __name__ == '__main__':
    questionario.run(debug=True)