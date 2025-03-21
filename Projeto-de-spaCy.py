#Instalação no Terminal
pip install spacy
python -m spacy download pt_core_news_sm

#Projeto de spaCy
import spacy

# Carregar o modelo de linguagem em português
nlp = spacy.load('pt_core_news_sm')

# Exemplo de texto em português brasileiro
texto = "Eu gosto de aprender sobre processamento de linguagem natural."

# Processar o texto com o pipeline do spaCy
doc = nlp(texto)

# Exibir anotações do texto
print("Anotações do texto:")
for token in doc:
    print(f'Token: {token.text}, POS: {token.pos_}, Tag: {token.tag_}, Lema: {token.lemma_}, Dependência: {token.dep_}')

# Exibir entidades nomeadas (NER) no texto
print("\nEntidades Nomeadas:")
for ent in doc.ents:
    print(f'Entidade: {ent.text}, Rótulo: {ent.label_}')

# Função para exibir detalhes do texto anotado
def exibir_detalhes_anotacao(doc):
    print("\nDetalhes da Anotação:")
    for token in doc:
        print(f"""
        Texto: {token.text}
        Lema: {token.lemma_}
        Parte do Discurso: {token.pos_} ({spacy.explain(token.pos_)})
        Tag detalhada: {token.tag_} ({spacy.explain(token.tag_)})
        Dependência: {token.dep_} ({spacy.explain(token.dep_)})
        Cabeça do token: {token.head.text}
        Subtokens: {[child for child in token.children]}
        """)

# Exibir detalhes da anotação
exibir_detalhes_anotacao(doc)
