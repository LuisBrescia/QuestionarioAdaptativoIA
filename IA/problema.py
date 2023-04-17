from transformers import BertTokenizer, BertModel
from torch.nn.functional import cosine_similarity
import torch

# ? Esse código é para não aparecer os avisos de erro do modelo, no momentos estou ignorando eles
import logging
logging.getLogger("transformers.modeling_utils").setLevel(logging.ERROR)

# ! Carrega o modelo e o tokenizador, não sei como funciona, mas funciona
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# * Função que compara as respostas
def comparaRespostas(respostaAluno, caminhoRespostaIA):

    # ? Importante usar with, para garantir que o arquivo será fechado
    with open(caminhoRespostaIA, 'r') as resposta:
        respostaIA = resposta.read()

    tokenAluno = tokenizer.encode(respostaAluno, add_special_tokens=True)
    tokenIA = tokenizer.encode(respostaIA, add_special_tokens=True)

    inputs1 = torch.tensor([tokenAluno])
    inputs2 = torch.tensor([tokenIA])

    outputs1 = model(inputs1)
    outputs2 = model(inputs2)

    last_hidden_states1 = outputs1[0][:, 0, :]
    last_hidden_states2 = outputs2[0][:, 0, :]
    
    similarity = cosine_similarity(last_hidden_states1, last_hidden_states2)

    # > Cálculo provisório, precisa ser melhorado    
    x = similarity.item() 
    x = ((x + 1) / 2) * 100
    x = (x - 50) * 2

    # > Para ajudar no debug
    print(respostaAluno)
    print(x)

    if x >= 60:
        status = "APROVADO"
    else:
        status = "REPROVADO"

    if respostaAluno == '':
        resultado = "Resposta não enviada"
        status = ""
    else:
        resultado = f"A similaridade entre as duas respostas é de: {x:.2f}%"

    return resultado, status