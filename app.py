from flask import Flask, render_template, request
import joblib 
app = Flask(__name__)
model = joblib.load('diabetic_79.sav')
@app.route('/')
def hello():
    return render_template('landing.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/feedback')
def feedback():
    return render_template('Feedback.html')

@app.route('/gallary')
def gallary():
    return render_template('gallery.html')

@app.route('/model')
def model():
    return render_template('model.html')

@app.route('/data' , methods = ['Post'])
def data():
    first_name = request.form.get('First_Name')
    second_name = request.form.get('second_Name')
    phone = request.form.get('Number')
    email = request.form.get('email')

    print(first_name)
    print(second_name)
    print(phone)
    print(email)
    return "Form Submitted"

@app.route('/modeldata' , methods = ['Post'])
def modeldata():
    print('Hello World')
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    print(preg)
    print(plas)
    print(pres)
    print(skin)
    print(test)
    print(mass)
    print(pedi)
    print(age)
    
    
    #result = model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])
    result = model.predict([[1,1,1,1,1,1,1,1]])
    if result[0] == 0:

        print('person is diabatic')
    else:
        print('person is non-diabetic')

if __name__ =='__main__':
    app.run(debug = True)

