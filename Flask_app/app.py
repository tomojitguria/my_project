from flask import Flask, render_template
app = Flask(__name__)

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


if __name__ =='__main__':
    app.run(debug = True)