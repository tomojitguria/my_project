import pickle
#load saved file
model = pickle.load(open('diabetic_79.sav','rb'))
result = model.predict([[1,1,1,1,1,1,1,1]])
print(result)
if result[0] == 0:
    print('person is diabatic')
else:
    print('person is non-diabetic')