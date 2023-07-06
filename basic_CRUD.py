from flask import Flask, request, render_template

app = Flask(__name__)
my_data = {}

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        my_data[key] = value

    return render_template('create.html')


@app.route('/', methods=['POST', 'GET'])
def welcome():

    return render_template('welcome.html')


@app.route('/read')
def read():
    return render_template('read.html', data = my_data)

@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        if key in my_data:
            my_data[key] = value
    return render_template('update.html')

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in my_data:
            del my_data[key]
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True)