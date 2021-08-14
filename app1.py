from flask import Flask, render_template, request
import joblib 
app = Flask(__name__)

@app.route('/')
def model():
    return render_template('model.html')
    
@app.route('/modeldata' , methods = ['Post'])
def modeldata():
    model = joblib.load('diabetic_79.sav')
    
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')  
    
    #result = model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])
    #result = model.predict([[1,1,1,1,1,1,1,1]])
    result = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if result[0] == 0:

        result = 'person is diabatic'
    else:
        result = 'person is non-diabetic'
    return render_template('Result.html',output = result)

if __name__ =='__main__':
    app.run(debug = True)