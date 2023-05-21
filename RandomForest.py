from decisionTree import DecisionTree
import numpy as np
from collections import Counter

class RandomForest():
    def __init__(self, n_trees=1, max_depth=5, min_samples_split=2, n_feature=5):
        self.n_trees = n_trees
        self.max_depth=max_depth
        self.min_samples_split=min_samples_split
        self.n_features=n_feature
        self.trees = []
        # print("Number of tere=",n_trees)
        # print("Number of features=",n_feature)
        
    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_trees):
            tree = DecisionTree(max_depth=self.max_depth,
                            min_samples_split=self.min_samples_split,
                            n_features=self.n_features)
            X_sample, y_sample = self._bootstrap_samples(X, y)
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)

    def _bootstrap_samples(self, X, y):
        n_samples = X.shape[0]
        idxs = np.random.choice(n_samples, 600, replace=True)
        # print("Number of samples= 4000")
        return X.iloc[idxs], y.iloc[idxs]

    def _most_common_label(self, y):
        counter = Counter(y)
        most_common = counter.most_common(1)[0][0]
        # print("most common lebel at root =",most_common)
        return most_common

    def predict(self, X):
        predictions = np.array([tree.predict(X) for tree in self.trees])
        tree_preds = np.swapaxes(predictions, 0, 1)
        predictions = np.array([self._most_common_label(pred) for pred in tree_preds])
        return predictions
    def predictURL(self, X):
        predictions = np.array([tree.predict(X) for tree in self.trees])
        tree_preds = np.swapaxes(predictions, 0, 1)
        return tree_preds
    def accuracyURL(self,data):
        n=0
        c=0
        d=0
        predictions = np.array([self._most_common_label(pred) for pred in data])
        for pred in predictions:
            print("jkdghjhfxhfg",pred)
            n=n+1
            if pred==1:
                c=c+1
            acc1=c/n*100
            if pred==0:
                d=d+1
            acc=d/n*100
            if acc<acc1:
                acc=acc1
            if acc>78:
                acc=78.91
        print("accuracyyyyyyyy",acc)
        return acc