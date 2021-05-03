import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV

tokens_df = pd.read_csv('../csvs/redacted_tokens.csv')

y = tokens_df.podcast
x = tokens_df.Redacted_tokens


tfidf_model = TfidfVectorizer()
nb_model = MultinomialNB()

pipe = Pipeline(steps=[('tfidf', tfidf_model), ('nb', nb_model)])

parameters = {
    'tfidf__max_features': [10000],
    'tfidf__stop_words': ['english'],
    'tfidf__lowercase': [True],
    'tfidf__ngram_range': [(1, 2)],
    'nb__alpha': [0.25],
    'nb__fit_prior': [True]
}

search = GridSearchCV(pipe, parameters, n_jobs=5, cv=5)
search.fit(x, y)

print('best parameters:', search.best_params_)    
print('best mean accuracy:', search.best_score_)
print(search.cv_results_['mean_test_score'])

