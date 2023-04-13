import torch

# ? Modelo IA pré-treinado: BERT
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModel.from_pretrained('bert-base-uncased')

# > Respostas do Aluno e da IA
respostaAluno = "Primeira resposta"
respostaIA = "Segunda resposta"

# * Transforma as respostas em algo que o modelo entenda
# // resposta1 = tokenizer.encode(resposta1, return_tensors='pt')    # tensor
tokenAluno = tokenizer.encode(respostaAluno, add_special_tokens=False)
tokenIA = tokenizer.encode(respostaIA, add_special_tokens=False)

# * Adiciona os tokens especiais
# ? Tokens Especiais são usados em modelos de linguagem natural para indicar o início e o fim de uma sentença.
tokenAluno = [tokenizer.cls_token_id] + tokenAluno + [tokenizer.sep_token_id]
tokensIA = [tokenizer.cls_token_id] + tokenIA + [tokenizer.sep_token_id]

# * Transforma os tokens em tensores PyTorch
inputs1 = torch.tensor([tokens1])
inputs2 = torch.tensor([tokens2])

# * Obter as saídas do modelo para cada sequência
outputs1 = model(inputs1)
outputs2 = model(inputs2)

# * Extrair o último estado escondido de cada token
last_hidden_states1 = outputs1[0][:, 0, :]
last_hidden_states2 = outputs2[0][:, 0, :]

# * Calcular a similaridade entre as duas sequências
from torch.nn.functional import cosine_similarity
similarity = cosine_similarity(last_hidden_states1, last_hidden_states2)