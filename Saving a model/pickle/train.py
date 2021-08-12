import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = pd.read_csv(url , names = names)
print(dataframe)
X = dataframe.iloc[:,:8]
Y = dataframe.iloc[:,8]
X_train,X_test,Y_train,Y_test = model_selection.train_test_split(X,Y,test_size=0.2,random_state=101)
#fit the model
model = LogisticRegression()
model.fit(X_train,Y_train)

#accuracy
result = model.score(X_test,Y_test)
print(result)

#saving the model (pkl,sav)
pickle.dump(model,open('diabetic_79.sav','wb'))