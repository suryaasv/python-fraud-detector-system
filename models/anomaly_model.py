from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.2)

def train(X):
    model.fit(X)

def score(X):
    return -model.decision_function(X)