import numpy as np
from collections import Counter


class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None


class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=15, n_features=15):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None

    def fit(self, X, y):

        self.n_features = X.shape[1] if not self.n_features else min(X.shape[1], self.n_features)
        print("NUmber of features=",self.n_features)
        self.root = self._grow_tree(X, y)  #return value from root node of _grow_tree as 0 or 1

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_feats = X.shape
        n_labels = len(np.unique(y))
        # check the stopping criteria
        if (depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split  ):

            leaf_value = self._most_common_label(X,y)
            return Node(value=leaf_value)
        
        feat_idxs = np.random.choice(n_feats, self.n_features, replace=False)   #selects randon features index


        # find the best split
        best_feature, best_thresh = self._best_split(X, y, feat_idxs)


        # create child nodes
        left_idxs, right_idxs = self._split(X.iloc[:, best_feature], best_thresh)
        t1=np.any(left_idxs)
        t2=np.any(right_idxs)

        

        if (t1==False or t2==False):

            leaf_value = self._most_common_label(X,y)
            return Node(value=leaf_value)
        left = self._grow_tree(X.iloc[left_idxs, :], y.iloc[left_idxs], depth + 1)
        right = self._grow_tree(X.iloc[right_idxs, :], y.iloc[right_idxs], depth + 1)
        # print("depth of tree=",depth)
        # print("best feature",best_feature)
        return Node(best_feature, best_thresh, left, right)

    def _best_split(self, X, y, feat_idxs):
        best_gain = -1
        # print("ujjwal",X.shape)
        split_idx, split_threshold = None, None

        for feat_idx in feat_idxs:
            # print("selected feature=",feat_idx)
            X_column = X.iloc[:, feat_idx]  #selects 1 column of a feature at a itme ie having @ symbol column
            
            thresholds = np.unique(X_column) # returns unique values of each column...uniques values i having @ symbol ie 0 or 1
            for thr in thresholds: #one time for 0 one time for 1
                # calculate the information gain
                gain = self._information_gain(y, X_column, thr)
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_threshold = thr
            # print("best feature=",split_idx)
            
        return split_idx, split_threshold

    def _information_gain(self, y, X_column, threshold):
        # parent entropy
        parent_entropy = self._entropy(y)
        # print("entropy of parent=",parent_entropy)

        # create children
        left_idxs, right_idxs = self._split(X_column, threshold)  #one column with its possible value ie 0 or 1

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0

        # calculate the weighted avg. entropy of children
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        e_l, e_r = self._entropy(y.iloc[left_idxs]), self._entropy(y.iloc[right_idxs])
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r
        # print("child entropy",child_entropy)
        # calculate the IG
        # print("difference=",parent_entropy,"bvhdfb",child_entropy)
        information_gain = parent_entropy - child_entropy
        # print("Information Gain =",information_gain)
        return information_gain

    def _split(self, X_column, split_thresh):
        # print("split=",split_thresh)
        left_idxs = np.argwhere(X_column.to_numpy() <=split_thresh).flatten() #returns index of X_column values that satisfies the condition
        # print(left_idxs.shape)
        right_idxs = np.argwhere(X_column.to_numpy() > split_thresh).flatten()
        # print(right_idxs.shape)
        return left_idxs, right_idxs

    def _entropy(self, y):
        hist = np.bincount(y)#counts thne number of occurance from 0  to max number in the list...ie counts the number of 0 and 1 in y
        ps = hist / len(y)   #ps=[0.534 0.4353]
        # print("entropy",-np.sum([p * np.log(p) for p in ps if p > 0]))
        return -np.sum([p * np.log(p) for p in ps if p > 0]) #is sum([no of ot times 0 occured/length of y  *   np log(....)+[no of ot times 1 occured/length of y  *   np log(....)])

    def _most_common_label(self,X, y):

        counter = Counter(y)
        value = counter.most_common(1)[0][0]
        return value

    def predict(self, X):
        return np.array([self._traverse_tree(q, self.root) for q in X.iloc])

    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)