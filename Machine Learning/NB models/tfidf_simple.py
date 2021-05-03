# tfidf and multinomial nb pipeline NO GRIDSEARCH
import pandas as pd
import numpy as np
import pickle5 as pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, accuracy_score

tokens_df = pd.read_csv('../csvs/redacted_tokens.csv')

y = tokens_df.podcast
x = tokens_df.Redacted_tokens

tfidf_model = TfidfVectorizer()
nb_model = MultinomialNB()

pipe = make_pipeline(TfidfVectorizer(max_features=20000, ngram_range=(1, 2), stop_words='english', lowercase=True),
                     MultinomialNB(alpha=0.25, fit_prior=True))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0, stratify=y)

pipe.fit(x_train, y_train)
y_pred = pipe.predict(x_test)

print('Predictions:')
print(list(y_pred))
print()
print('Actual:')
print(list(y_test))