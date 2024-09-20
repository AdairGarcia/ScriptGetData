import spacy
from stop_words import get_stop_words

def tokenizer(string):
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(string)
    for token in doc:
        print(token.text)

    return doc

def delete_stop_words(doc):
    # we are working tutututu
    for entity in doc.ents:
        print(entity.text, entity.label_)
    return doc


if __name__ == '__main__':
    texto = "Este es un ejemplo simple de cómo eliminar las stop words de un texto."
    stop_words_spanish = get_stop_words('spanish')

    tokenizer(texto)





