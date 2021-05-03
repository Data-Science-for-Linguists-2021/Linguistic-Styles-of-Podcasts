import pandas as pd
import pickle5 as pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import confusion_matrix, accuracy_score


num_df = pd.read_csv('num_df.csv')


# train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)


lr_model = LogisticRegression() # initialize model
lr_model.fit(X_train, y_train) # train model
y_pred = lr_model.predict(X_test) # save model predictions of test data


# function to show confusion matrix
def plot_cm(y_test, y_pred, model_name, ticks):
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, square=True, annot=True, fmt='d', cmap='Blues', annot_kws={"size": 14},
                xticklabels=ticks, yticklabels=ticks)
    plt.xlabel('predicted score')
    plt.ylabel('true score')
    plt.title(f'{model_name} accuracy: {accuracy_score(y_test, y_pred)*100:0.4f}%')
    plt.show()
    
plot_cm(y_test, y_pred, 'Logistic Regression', y.value_counts())

