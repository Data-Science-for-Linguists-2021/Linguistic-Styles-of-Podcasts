import pandas as pd
import pickle5 as pickle
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score



# get rid of all the dictionary columns, clean up list columns, make all data numerical
num_df = pd.read_csv('../csvs/tal_numeric_df.csv')

y = num_df['Episode']
X = num_df.drop(['Episode', 'Unnamed: 0'], axis=1)


# specify grid search parameters
parameters = {
    'penalty': ['l1','l2','elsticnet','none'],
    'C': [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100, 500, 1000, 5000],
    'class_weight': [None, 'balanced'],
    'solver': ['sag','saga','lbfgs','newton-cg']
}

lr_model = LogisticRegression()
grid_search = GridSearchCV(lr_model, parameters, cv=3, n_jobs=5, verbose=1)

grid_search.fit(X, y)

print(grid_search.best_params_)
print(grid_search.best_score_)
print(grid_search.cv_results_['mean_test_score'])

for i in range(5):                        # 0, 1, 2, 3, 4
    print(f'CV run #{i} accuracies:\n', 
          grid_search.cv_results_[f'split{i}_test_score'])