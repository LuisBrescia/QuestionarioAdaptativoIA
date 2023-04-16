from transformers import BertTokenizer, BertModel
import torch

import logging
logging.getLogger("transformers.modeling_utils").setLevel(logging.ERROR)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# def comparaRespostas(respostaAluno):
def comparaRespostas(respostaAluno, caminhoRespostaIA):
    
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

    from torch.nn.functional import cosine_similarity
    similarity = cosine_similarity(last_hidden_states1, last_hidden_states2)
    
    x = similarity.item() 
    x = ((x + 1) / 2) * 100
    x = (x - 50) * 2

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