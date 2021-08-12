import joblib
#load saved file
model = joblib.load('diabetic_79.sav')
result = model.predict([[1,1,1,1,1,1,1,1]])
print(result)
if result[0] == 0:
    print('person is diabatic')
else:
    print('person is non-diabetic')