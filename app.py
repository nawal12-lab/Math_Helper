from flask import Flask, render_template
app = Flask (__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/templates/addition.html')
def addition():
    return render_template('addition.html')
@app.route('/templates/multiplication.html')
def multiplication():
    return render_template('multiplication.html')
@app.route('/templates/subtract.html')
def subtract():
    return render_template('subtract.html')
@app.route('/templates/divide.html')
def divide():
    return render_template('divide.html')
@app.route('/templates/sqrt.html')
def sqrt():
    return render_template('sqrt.html')
if __name__ == ('__main__'):
    app.run(debug=True)