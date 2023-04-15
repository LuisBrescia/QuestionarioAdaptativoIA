import torch
import torch.nn as nn

# ? Modelo IA pré-treinado: BERT
from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')



# > Respostas do Aluno e da IA
respostaAluno = "Primeira resposta"
# ? With garante que o arquivo será fechado corretamente após o uso.
with open('Respostas/resposta1.txt', 'r') as resposta1:
    respostaIA = resposta1.read()


# * Transforma as respostas em algo que o modelo entenda
# // resposta1 = tokenizer.encode(resposta1, return_tensors='pt')    # tensor
tokenAluno = tokenizer.encode(respostaAluno, add_special_tokens=True)
tokenIA = tokenizer.encode(respostaIA, add_special_tokens=True)
# > add_special_tokens=True: Adiciona os tokens Bert [CLS] e [SEP] para indicar o início e o fim da sentença.

# * Transforma os tokens em tensores PyTorch
# ? Tensores são estruturas de dados multidimensionais que podem ser usadas para representar vetores e matrizes.
inputs1 = torch.tensor([tokenAluno])
inputs2 = torch.tensor([tokenIA])

# * Obter as saídas do modelo para cada sequência
outputs1 = model(inputs1)
outputs2 = model(inputs2)

# * Extrair o último estado escondido de cada token
# ? O último estado escondido é o vetor de características que representa o token.
last_hidden_states1 = outputs1[0][:, 0, :]
last_hidden_states2 = outputs2[0][:, 0, :]

# * Calcular a similaridade entre as duas sequências
from torch.nn.functional import cosine_similarity
similarity = cosine_similarity(last_hidden_states1, last_hidden_states2)

# * Imprimir o resultado
x = similarity.item() 
x = ((x + 1) / 2) * 100
print(f"A similaridade entre as duas respostas é de: {x:.2f}%")
