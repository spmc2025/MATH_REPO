from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 + num2
        except ValueError:
            result = 'Invalid input! Please enter numbers only.'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
