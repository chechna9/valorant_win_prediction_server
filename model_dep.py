import pandas as pd
from sklearn.model_selection import GridSearchCV,KFold
from sklearn.pipeline import Pipeline,FunctionTransformer
from sklearn.linear_model import LogisticRegression
kfold = KFold(n_splits=5,shuffle=True,random_state=12)
def m2_feature_selection(X:pd.DataFrame):
  features = ['t1_duelist', 't1_sentinel', 't1_initiator', 't1_controller',
              't2_duelist', 't2_sentinel', 't2_initiator', 't2_controller','Map',
              'Team1_SideFirstHalf']
  return X[features]