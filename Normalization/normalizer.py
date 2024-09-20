import spacy as sp
from stop_words import get_stop_words
import pandas as pd

def normalizer(string):
    if not isinstance(string, str):
        return ""

    nlp = sp.load("es_core_news_sm")
    doc = nlp(string)

    no_stop_words_string = ""

    for token in doc:
        if (not token.lemma_.lower() in stop_words_spanish) and (token.pos_ != "PUNCT"):
            no_stop_words_string += token.lemma_ + " "
        elif token.pos_ == "PUNCT" and token.i == len(doc) - 1:
            no_stop_words_string = no_stop_words_string[:-1]
            no_stop_words_string += token.lemma_

    return no_stop_words_string

def clean_data(df):
    empty_df = df[0:0]
    empty_df.to_csv('raw data corpus.csv', index=False)

def add_data():
    df = pd.read_csv('../Script/raw data corpus.csv')
    df['Title'] = df['Title'].apply(normalizer)
    df['Content'] = df['Content'].apply(normalizer)

    df.to_csv('normalized data corpus.csv', index=False)


if __name__ == '__main__':
    stop_words_spanish = get_stop_words('spanish')

    add_data()
