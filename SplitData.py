from DataPrepossessing import f_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from decisionTree import DecisionTree
from RandomForest import RandomForest
from test import featureExtraction

import numpy as np
import pandas as pd

y = f_data['Label']
x = f_data.drop('Label', axis=1)


print("start\n")
print("data",x.shape)
    
# print(y.head())
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=27)
#print(y_train[2])

print("train",X_train.shape)
print("test",X_test.shape)

# clf = DecisionTree()
# clf.fit(X_train, y_train)
# predections = clf.predict(X_test)

# def accuracy(y_test, y_pred):
#     return np.sum(y_test == y_pred) / len(y_test)


# acc = accuracy(y_test, predections)
# print("ACCURACY=",acc*100)




def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy



#------------------------------------------------------------------
clf = RandomForest(n_trees=25)
clf.fit(X_train, y_train)
# print(type(X_test))
# dataq = pd.read_csv("Book2.csv")
# dataqq=dataq.drop(['Domain'],axis=1)
def createmodel(n_trees=1, max_depth=5, min_samples_split=2, n_feature=5):
    clf = RandomForest(n_trees, max_depth, min_samples_split, n_feature)
    clf.fit(X_train, y_train)    

predictions = clf.predict(X_train)
# print(predictions)


acc =  accuracy(y_train, predictions)
def retAccu():
    return acc

print(acc)
cm = confusion_matrix(y_train, predictions)
print(cm)
# Calculate recall from confusion matrix
true_positives = cm[1, 1]
false_negatives = cm[1, 0]
recall = true_positives / (true_positives + false_negatives)

print("Recall:", recall)

# class checkURL():
#     def __init__(self):
#         data=[]
#         url ="http://179.185.89.94/"


#         data.append(featureExtraction(url))
#         print("data=",data)

#         # # # Convert the array to a DataFrame
        
#         df = pd.DataFrame(data,columns=['Have_IP', 'Have_At', 'URL_Length', 'URL_Depth','Redirection', 
#                       'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic', 
#                       'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards'])
#         # print(df)
#         # print(df.shape)
#         predictions = clf.predictURL(df)
#         print("pre=",predictions)

# c= checkURL()

from joblib import dump

dump(clf, './model.joblib')